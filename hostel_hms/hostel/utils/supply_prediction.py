from datetime import timedelta
from django.utils import timezone
from hostel.models import Student, LeaveRequest, InOutRecord

def predict_next_week_occupancy():
    today = timezone.now().date()
    next_week = today + timedelta(days=7)

    total_students = Student.objects.count()

    leaves = LeaveRequest.objects.filter(
        approval_status="Approved",
        start_date__lte=next_week,
        end_date__gte=today
    ).count()

    out_students = InOutRecord.objects.filter(
        out_date__gte=today,
        in_date__isnull=True
    ).count()

    expected_occupancy = total_students - leaves - out_students

    return {
        "total": total_students,
        "leaves": leaves,
        "out": out_students,
        "expected": expected_occupancy
    }
