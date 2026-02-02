from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# -------------------------
# HOSTEL & INFRASTRUCTURE
# -------------------------

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100)
    hostel_id = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()
    warden_name = models.CharField(max_length=100, blank=True, null=True)
    sharing_type = models.IntegerField(default=1, help_text="Number of students allowed per room")
    location = models.TextField()

    def __str__(self):
        return self.hostel_name


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_id = models.CharField(max_length=20, unique=True)
    hod = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Room(models.Model):
    room_id = models.CharField(max_length=20, unique=True)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50) # Keep for descriptive purposes (e.g. AC/Non-AC)
    current_occupancy = models.IntegerField(default=0)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    @property
    def is_vacant(self):
        return self.current_occupancy == 0

    @property
    def is_full(self):
        return self.current_occupancy >= self.hostel.sharing_type

    def __str__(self):
        return f"Room {self.room_number} ({self.hostel.hostel_name})"


# -------------------------
# PEOPLE
# -------------------------

class Guardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    relation = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    usn = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    admission_date = models.DateField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.usn})"


class Authority(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    auth_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=30)  # Warden / Admin / Maintenance

    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} ({self.role})"


class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# -------------------------
# CORE FUNCTIONALITY
# -------------------------

class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    complaint_date = models.DateTimeField(auto_now_add=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True)
    description = models.TextField()

    status = models.CharField(max_length=20, default="Pending")

    solved_by = models.ForeignKey(
        Authority, null=True, blank=True, on_delete=models.SET_NULL
    )
    solved_date = models.DateTimeField(null=True, blank=True)
    resolution_note = models.TextField(blank=True)

    def __str__(self):
        return f"Complaint {self.id} - {self.issue_category}"


class LeaveRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    authority = models.ForeignKey(Authority, on_delete=models.CASCADE)

    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    approval_status = models.CharField(max_length=20, default="Pending")
    approval_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Leave {self.id} - {self.student.usn}"


class InOutRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    event_type = models.CharField(max_length=10)  # IN / OUT
    timestamp = models.DateTimeField(auto_now_add=True)
    purpose = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.usn} - {self.event_type}"


class Announcement(models.Model):
    authority = models.ForeignKey(Authority, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    details = models.TextField()

    post_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
