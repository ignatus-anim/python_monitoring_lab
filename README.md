# 24/7 System Monitoring Script

This Python script monitors your system's CPU usage, RAM usage, and disk space and sends email alerts when any of these metrics exceed predefined thresholds. It's useful for maintaining system health and ensuring timely intervention during resource overuse.

---

## Features
- **Monitors System Metrics**:
  - CPU usage
  - RAM usage
  - Disk space availability
- **Customizable Thresholds**:
  - Set thresholds for CPU, RAM, and disk space alerts.
- **Email Alerts**:
  - Automatically sends alerts via email using the Mailjet API.
- **Readability and Error Handling**:
  - Includes modular functions for better readability and maintainability.
  - Error handling ensures smooth execution.

---

## Prerequisites

1. **Python**:
   - Ensure Python 3.x is installed on your machine.
2. **Packages**:
   - Install required Python packages:
     ```bash
     pip install psutil python-dotenv mailjet-rest
     ```
3. **Mailjet API Credentials**:
   - Create a Mailjet account at [Mailjet](https://www.mailjet.com/).
   - Generate your API key and secret.

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a `.env` File**:
   - Add your Mailjet credentials to a `.env` file in the project directory:
     ```
     API_KEY=your_mailjet_api_key
     API_SECRET=your_mailjet_api_secret
     ```

3. **Customize Thresholds**:
   - Adjust the thresholds in the script as needed:
     ```python
     CPU_THRESHOLD = 10  # CPU usage in percentage
     RAM_THRESHOLD = 10  # RAM usage in percentage
     DISK_THRESHOLD = 50  # Free disk space in percentage
     ```

4. **Run the Script**:
   ```bash
   python monitor.py
   ```

---

## Configuration Details

### Email Configuration
- **Sender Details**:
  - From Email: `ignatus.anim@amalitech.com`
  - Sender Name: `24/7 SysMon`
- **Recipient Details**:
  - To Email: `nanaakwasi632@gmail.com`
  - Recipient Name: `Admin`

You can customize these in the `send_email_alert` function.

---

## How It Works

1. **System Monitoring**:
   - The script retrieves the current CPU, RAM, and disk usage using the `psutil` library.
   
2. **Threshold Checks**:
   - Compares the metrics against the defined thresholds.

3. **Alert Generation**:
   - If any threshold is breached, a formatted email alert is sent to the configured recipient.

4. **Execution**:
   - Logs the current status to the console:
     - "All system metrics are within normal limits." when everything is fine.
     - Sends an email and logs "Email sent: [status code]" when thresholds are breached.

---

## Example Output

### Normal Metrics:
```
All system metrics are within normal limits.
```

### Breached Thresholds:
Email subject:
```
System Monitoring Alert - 2024-11-25 14:34:56
```
Email body:
```html
<h3>
CPU usage is high: 15% (Threshold: 10%)<br>
RAM usage is high: 45% (Threshold: 10%)<br>
Disk space is low: 48% free (Threshold: 50% free)
</h3>
```
Console:
```
Email sent: 200
```

---

## Extending the Script
1. **Add More Metrics**:
   - Use `psutil` to monitor additional metrics like network I/O or processes.
2. **Integrate with Other Email Services**:
   - Replace the Mailjet integration with another email API like SMTP or SendGrid.
3. **Periodic Monitoring**:
   - Use a scheduler like `cron` (Linux) or `Task Scheduler` (Windows) to run the script periodically.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Author
**Ignatus Anim**  
Email: [ignatus.anim@amalitech.com](mailto:ignatus.anim@amalitech.com)  
Maintainer: **24/7 SysMon Team**