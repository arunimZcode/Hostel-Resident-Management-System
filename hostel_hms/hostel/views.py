from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages
from .models import Hostel, Room, Student, Authority, Complaint, LeaveRequest, InOutRecord, Facility, Guardian
from .forms import StudentRegistrationForm, ComplaintForm, LeaveRequestForm, AuthorityRegistrationForm
from datetime import timedelta
from .utils.predictive import detect_critical_blocks, predict_mess_demand

# ... imports ...

def landing_page(request):
    return render(request, "landing.html")

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            try:
                # Create User
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                
                # Create Guardian
                guardian = Guardian.objects.create(
                    first_name=form.cleaned_data['guardian_first_name'],
                    last_name=form.cleaned_data['guardian_last_name'],
                    relation=form.cleaned_data['guardian_relation'],
                    contact_number=form.cleaned_data['guardian_contact'],
                    email=form.cleaned_data['guardian_email'],
                    address=form.cleaned_data['guardian_address']
                )
                
                # Create Student
                student = form.save(commit=False)
                student.user = user
                student.email = form.cleaned_data['email'] # Ensure email matches
                student.guardian = guardian
                student.admission_date = timezone.now().date() # Default to today
                student.save()
                
                # Update Room Occupancy
                room = student.room
                if room:
                    room.current_occupancy += 1
                    room.save()
                
                login(request, user)
                messages.success(request, "Registration successful!")
                return redirect('student_home')
            except IntegrityError:
                messages.error(request, "An error occurred during registration. The username or USN might already exist.")
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'register_student.html', {'form': form})

def register_authority(request):
    if request.method == 'POST':
        form = AuthorityRegistrationForm(request.POST)
        if form.is_valid():
            try:
                # Create User
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                
                # Create Authority
                authority = form.save(commit=False)
                authority.user = user
                authority.save()
                
                login(request, user)
                messages.success(request, "Registration successful!")
                return redirect('authority_home')
            except IntegrityError:
                messages.error(request, "An error occurred during registration. The username or ID might already exist.")
    else:
        form = AuthorityRegistrationForm()
        
    return render(request, 'register_authority.html', {'form': form})

@csrf_protect
def login_view(request):
    role = request.GET.get("role", "Student")  # Default to 'Student' for display
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, "login.html", {
                "error": "Invalid username or password. Please try again.",
                "role": role
            })

        login(request, user)

        if hasattr(user, "student"):
            return redirect("student_home")
        elif hasattr(user, "authority"):
            return redirect("authority_home")
        else:
            return redirect("/admin/")

    return render(request, "login.html", {"role": role})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def student_home(request):
    student = get_object_or_404(Student, user=request.user)
    
    # Dashboard Data
    complaints = Complaint.objects.filter(student=student).order_by('-complaint_date')
    leaves = LeaveRequest.objects.filter(student=student).order_by('-start_date')
    in_out_logs = InOutRecord.objects.filter(student=student).order_by('-timestamp')[:10] # Last 10
    
    # Current Movement Status
    latest_log = InOutRecord.objects.filter(student=student).order_by('-timestamp').first()
    current_status = latest_log.event_type if latest_log else 'N/A'
    
    # Stats for Graphs
    complaint_stats = {
        'total': complaints.count(),
        'solved': complaints.filter(status='Solved').count(),
        'pending': complaints.filter(status='Pending').count()
    }
    
    leave_stats = {
        'total': leaves.count(),
        'approved': leaves.filter(approval_status='Approved').count(),
        'rejected': leaves.filter(approval_status='Rejected').count(),
        'pending': leaves.filter(approval_status='Pending').count()
    }

    context = {
        "student": student,
        "complaints": complaints,
        "leaves": leaves,
        "logs": in_out_logs,
        "current_status": current_status,
        "complaint_stats": complaint_stats,
        "leave_stats": leave_stats,
    }
    return render(request, "student_home.html", context)

@login_required
def authority_home(request):
    authority = get_object_or_404(Authority, user=request.user)

    # Fetch Data
    students = Student.objects.select_related('room__hostel', 'guardian', 'department').all().order_by('usn')
    hostels = Hostel.objects.prefetch_related('room_set__student_set').all()
    complaints = Complaint.objects.select_related('student__room').all().order_by('-complaint_date')
    leaves = LeaveRequest.objects.select_related('student').all().order_by('-start_date')

    # Stats
    stats = {
        'total_students': students.count(),
        'pending_complaints': complaints.filter(status='Pending').count(),
        'pending_leaves': leaves.filter(approval_status='Pending').count(),
        'total_rooms': Room.objects.count(),
        'occupied_rooms': Room.objects.filter(student__isnull=False).distinct().count()
    }

    # Predictive Insights
    maintenance_alerts = detect_critical_blocks()
    supply_prediction = predict_mess_demand()

    # Chart Data
    complaint_chart = {
        'labels': ['Pending', 'Solved'],
        'counts': [
            complaints.filter(status='Pending').count(),
            complaints.filter(status='Solved').count()
        ]
    }
    
    leave_chart = {
        'labels': ['Approved', 'Rejected', 'Pending'],
        'counts': [
            leaves.filter(approval_status='Approved').count(),
            leaves.filter(approval_status='Rejected').count(),
            leaves.filter(approval_status='Pending').count()
        ]
    }

    # Generate 7-day occupancy trend
    current_occ = stats['occupied_rooms']
    target_occ = supply_prediction.get('predicted_occupancy', current_occ)
    
    trend_series = []
    trend_labels = []
    for i in range(7):
        # Linear interpolation for demonstration
        val = current_occ + (target_occ - current_occ) * (i / 6.0)
        trend_series.append(int(val))
        trend_labels.append((timezone.now() + timedelta(days=i)).strftime('%b %d'))
    
    supply_prediction['trend_series'] = trend_series
    supply_prediction['trend_labels'] = trend_labels

    context = {
        "authority": authority,
        "students": students,
        "hostels": hostels,
        "complaints": complaints,
        "leaves": leaves,
        "stats": stats,
        "maintenance_alerts": maintenance_alerts,
        "supply_prediction": supply_prediction,
        "complaint_chart": complaint_chart,
        "leave_chart": leave_chart,
    }
    return render(request, "authority_dashboard_final.html", context)

@login_required
def trigger_maintenance_alert(request):
    facility = request.GET.get('facility')
    hostel = request.GET.get('hostel')
    
    if facility and hostel:
        subject = f"CRITICAL: Maintenance Required - {facility} ({hostel} Block)"
        message = f"High-priority alert triggered for {facility} in {hostel} block.\nPlease inspect immediately.\n\nHMS Automated Alert"
        # In a real app, you'd use a maintenance team email
        # For now, we'll use a placeholder and rely on console backend in settings
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['maintenance-team@example.com'],
            fail_silently=True,
        )
        messages.success(request, f"High-priority alert for {facility} was sent successfully!")
    
    return redirect('authority_home')

# --- Updated to use forms.py classes ---

@login_required
def create_complaint(request):
    if not Student.objects.filter(user=request.user).exists():
        return redirect("login")

    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.student = request.user.student
            complaint.save()
            # ... kept existing alert logic ...
            return redirect("student_home")
    else:
        form = ComplaintForm()

    return render(request, "create_complaint.html", {"form": form})

@login_required
def create_leave_request(request):
    if not Student.objects.filter(user=request.user).exists():
        return redirect("login")

    if request.method == "POST":
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.student = request.user.student
            leave.save()
            return redirect("student_home")
    else:
        form = LeaveRequestForm()

    return render(request, "create_leave_request.html", {"form": form})
@login_required
def authority_complaints(request):
    authority = get_object_or_404(Authority, user=request.user)
    complaints = Complaint.objects.all().order_by("-complaint_date")
    return render(request, "authority_complaints.html", {"complaints": complaints})


@login_required
def resolve_complaint(request, complaint_id):
    authority = get_object_or_404(Authority, user=request.user)
    complaint = get_object_or_404(Complaint, id=complaint_id)

    complaint.status = "Solved"
    complaint.solved_by = authority
    complaint.solved_date = timezone.now()
    complaint.save()

    return redirect("authority_complaints")
@login_required
def authority_leaves(request):
    authority = get_object_or_404(Authority, user=request.user)
    leaves = LeaveRequest.objects.filter(authority=authority)
    return render(request, "authority_leaves.html", {"leaves": leaves})


@login_required
def approve_leave(request, leave_id):
    leave = get_object_or_404(LeaveRequest, id=leave_id)
    leave.approval_status = "Approved"
    leave.approval_date = timezone.now()
    leave.save()
    return redirect("authority_leaves")


@login_required
def reject_leave(request, leave_id):
    leave = get_object_or_404(LeaveRequest, id=leave_id)
    leave.approval_status = "Rejected"
    leave.approval_date = timezone.now()
    leave.save()
    return redirect("authority_leaves")
@login_required
def download_complaint_report(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="complaints.csv"'
    writer = csv.writer(response)

    writer.writerow(["ID", "Student", "Category", "Status", "Date"])

    for c in Complaint.objects.all():
        writer.writerow([
            c.id,
            c.student.user.username,
            c.facility.name if c.facility else "None",
            c.status,
            c.complaint_date,
        ])

    return response


@login_required
def authority_student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    authority = get_object_or_404(Authority, user=request.user)

    # Activity Data
    # Activity Data
    complaints = Complaint.objects.filter(student=student).order_by('-complaint_date')
    leaves = LeaveRequest.objects.filter(student=student).order_by('-start_date')
    logs = InOutRecord.objects.filter(student=student).order_by('-timestamp')[:10]

    # Current Movement Status
    latest_log = InOutRecord.objects.filter(student=student).order_by('-timestamp').first()
    current_status = latest_log.event_type if latest_log else 'N/A'

    # Stats for Charts
    complaint_stats = {
        'solved': complaints.filter(status='Solved').count(),
        'pending': complaints.filter(status='Pending').count()
    }
    
    leave_stats = {
        'approved': leaves.filter(approval_status='Approved').count(),
        'rejected': leaves.filter(approval_status='Rejected').count(),
        'pending': leaves.filter(approval_status='Pending').count()
    }

    context = {
        "authority": authority,
        "student": student,
        "complaints": complaints,
        "leaves": leaves,
        "logs": logs,
        "current_status": current_status,
        "complaint_stats": complaint_stats,
        "leave_stats": leave_stats,
    }
    return render(request, "authority_student_detail.html", context)


@login_required
def download_leave_report(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="leaves.csv"'
    writer = csv.writer(response)

    writer.writerow(["ID", "Student", "From", "To", "Status"])

    for l in LeaveRequest.objects.all():
        writer.writerow([
            l.id,
            l.student.user.username,
            l.start_date,
            l.end_date,
            l.approval_status,
        ])

    return response
@staff_member_required
def run_supply_prediction(request):
    data = predict_next_week_occupancy()
    send_supply_alert(data)
    return render(request, "prediction_result.html", data)

@csrf_exempt
def watchman_view(request):
    if request.method == 'POST':
        usn = request.POST.get('usn').strip().upper()
        event_type = request.POST.get('event_type')
        purpose = request.POST.get('purpose')

        try:
            student = Student.objects.get(usn=usn)
            
            # Create Record
            InOutRecord.objects.create(
                student=student,
                event_type=event_type,
                purpose=purpose
            )
            messages.success(request, f"Recorded {event_type} for {student.first_name} ({usn})")
        except Student.DoesNotExist:
            messages.error(request, f"Student with USN '{usn}' not found.")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
        
        return redirect('watchman_view')

    # Fetch all logs and organize by status
    all_students = Student.objects.all()
    
    out_students = []
    in_students = []
    
    for student in all_students:
        last_log = InOutRecord.objects.filter(student=student).order_by('-timestamp').first()
        
        if last_log and last_log.event_type == 'OUT':
            out_students.append(last_log)
        else:
            if last_log and last_log.event_type == 'IN':
                in_students.append(last_log)
            else:
                # If no log exists, student is considered inside
                in_students.append(None)
    
    # Combine: OUT students first, then IN students
    recent_logs = out_students + in_students
    
    return render(request, 'watchman.html', {'recent_logs': recent_logs})
