from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Q
from hostel.models import Complaint, LeaveRequest, InOutRecord, Student

THRESHOLD = 5          # number of complaints
TIME_WINDOW = 24       # hours


def detect_critical_blocks():
    """
    Detects hostels/facilities with high complaint volume in a short time.
    """
    since_time = timezone.now() - timedelta(hours=TIME_WINDOW)

    # Group by hostel and facility
    critical_issues = Complaint.objects.filter(
        complaint_date__gte=since_time,
        status="Pending"
    ).values(
        'student__room__hostel__hostel_name',
        'facility__name'
    ).annotate(
        count=Count('id')
    ).filter(
        count__gte=THRESHOLD
    )

    alerts = []
    for issue in critical_issues:
        hostel_name = issue['student__room__hostel__hostel_name']
        facility_name = issue['facility__name']
        count = issue['count']
        
        # In a real app, this would trigger SMS/Email
        # from hostel.utils.alerts import send_maintenance_alert
        # send_maintenance_alert(hostel_name, facility_name, count)
        
        alerts.append({
            "hostel": hostel_name,
            "facility": facility_name,
            "count": count,
            "level": "CRITICAL" if count >= THRESHOLD * 2 else "HIGH"
        })

    return alerts


def predict_mess_demand():
    """
    Predicts student occupancy for the upcoming week based on leaves and current status.
    """
    today = timezone.now().date()
    next_week = today + timedelta(days=7)
    
    total_students = Student.objects.count()
    if total_students == 0:
        return {"predicted_occupancy": 0, "reduction_percentage": 0}

    # 1. Analyze Leaves
    # Count students who have approved leaves covering any part of the next week
    leaves_next_week = LeaveRequest.objects.filter(
        approval_status="Approved",
        start_date__lte=next_week,
        end_date__gte=today
    ).values('student').distinct().count()

    # 2. Factor in current InOut status (students currently OUT)
    # We'll assume students currently OUT but without an approved leave 
    # might still be absent for at least a day (short trip)
    out_students_count = 0
    all_students = Student.objects.all()
    for student in all_students:
        latest_log = InOutRecord.objects.filter(student=student).order_by('-timestamp').first()
        if latest_log and latest_log.event_type == 'OUT':
            # Check if they already have a leave (don't double count)
            has_leave = LeaveRequest.objects.filter(
                student=student,
                approval_status="Approved",
                start_date__lte=today,
                end_date__gte=today
            ).exists()
            if not has_leave:
                out_students_count += 0.5 # probabilistic weight for short-term absence

    predicted_absent = leaves_next_week + out_students_count
    predicted_occupancy = max(0, total_students - int(predicted_absent))
    reduction = (predicted_absent / total_students) * 100 if total_students > 0 else 0

    return {
        "total_students": total_students,
        "predicted_absent": int(predicted_absent),
        "predicted_occupancy": predicted_occupancy,
        "reduction_percentage": round(reduction, 1),
        "trend": "Decreasing" if reduction > 10 else "Stable"
    }
