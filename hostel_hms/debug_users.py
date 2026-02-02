import os
import django
import sys

# Add the project directory to sys.path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_hms.settings')
django.setup()

from hostel.models import Student

print("--- STUDENT DATA DUMP ---")
for s in Student.objects.all():
    print(f"ID: {s.id}")
    print(f"First Name: '{s.first_name}'")
    print(f"Last Name: '{s.last_name}'")
    print(f"USN: '{s.usn}'")
    print("-------------------------")
