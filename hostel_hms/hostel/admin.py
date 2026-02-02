from django.contrib import admin
from .models import (
    Hostel,
    Student,
    Authority,
    Guardian,
    Department,
    Room,
    LeaveRequest,
    Complaint,
    Announcement,
    Announcement,
    InOutRecord,
    Facility,
)

admin.site.register(Hostel)
admin.site.register(Student)
admin.site.register(Authority)
admin.site.register(Guardian)
admin.site.register(Department)   # ✅ FIX
admin.site.register(Room)         # ✅ FIX
admin.site.register(LeaveRequest)
admin.site.register(Complaint)
admin.site.register(Announcement)
admin.site.register(InOutRecord)
admin.site.register(Facility)
