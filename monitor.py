import time
import os
import psutil
from mailjet_rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Email configuration
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
FROM_EMAIL = "ignatus.anim@amalitech.com"
TO_EMAIL = "nanaakwasi632@gmail.com"
FROM_NAME = "24/7 SysMon"
TO_NAME = "Admin"

# Thresholds
CPU_THRESHOLD = 10  # CPU usage in percentage
RAM_THRESHOLD = 10  # RAM usage in percentage
DISK_THRESHOLD = 50  # Free disk space in percentage

def get_formatted_time():
    """Get the current time in a readable format."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def send_email_alert(subject, message):
    """Send an email alert via Mailjet."""
    try:
        mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')
        data = {
            "Messages": [
                {
                    "From": {"Email": FROM_EMAIL, "Name": FROM_NAME},
                    "To": [{"Email": TO_EMAIL, "Name": TO_NAME}],
                    "Subject": subject,
                    "HTMLPart": f"<h3>{message}</h3>"
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print(f"Email sent: {result.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_system_metrics():
    """Retrieve system metrics for CPU, RAM, and disk usage."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        return cpu_usage, ram_usage, disk_usage
    except Exception as e:
        print(f"Error retrieving system metrics: {e}")
        return None, None, None

def check_thresholds_and_alert():
    """Check system metrics against thresholds and send alerts if necessary."""
    cpu_usage, ram_usage, disk_usage = get_system_metrics()
    if cpu_usage is None:
        return

    alert_messages = []

    if cpu_usage > CPU_THRESHOLD:
        alert_messages.append(f"CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)")
    if ram_usage > RAM_THRESHOLD:
        alert_messages.append(f"RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)")
    if disk_usage > DISK_THRESHOLD:
        free_disk_space = 100 - disk_usage
        alert_messages.append(f"Disk space is low: {free_disk_space}% free (Threshold: {DISK_THRESHOLD}% free)")

    if alert_messages:
        alert_message = "\n".join(alert_messages)
        formatted_time = get_formatted_time()
        send_email_alert(f"System Monitoring Alert - {formatted_time}", alert_message)
    else:
        print("All system metrics are within normal limits.")

# Main execution
if __name__ == "__main__":
    check_thresholds_and_alert()
