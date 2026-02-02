from django.core.mail import send_mail
from django.conf import settings

# 🔴 EXISTING — DO NOT CHANGE
def send_maintenance_alert(block, issue, count):
    subject = f"🚨 CRITICAL ALERT: {issue} in Block {block}"
    message = (
        f"Block {block} has received {count} complaints "
        f"related to {issue} within the last 24 hours.\n\n"
        "Immediate maintenance action required."
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        ["maintenance@hostel.com"],
        fail_silently=True
    )


# 🟢 NEW — ADD THIS BELOW
def send_supply_alert(data):
    subject = "📊 Weekly Mess Supply Prediction"

    message = (
        f"Total Students: {data['total']}\n"
        f"Approved Leaves: {data['leaves']}\n"
        f"Students Currently Out: {data['out']}\n\n"
        f"Expected Occupancy Next Week: {data['expected']}\n\n"
        "Please adjust mess supplies accordingly."
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        ["warden@hostel.com"],  # demo email
        fail_silently=True
    )
