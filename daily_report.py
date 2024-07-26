import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
email_sender = 'your_email@gmail.com'
email_receiver = 'recipient_email@example.com'
email_subject = 'Daily Report'

# Function to send email
def send_email():
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = email_subject
    msg['From'] = email_sender
    msg['To'] = email_receiver

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hello,\n\nHere is your daily report.\n\nRegards,\nAutomated System"
    html = """\
    <html>
      <body>
        <p>Hello,<br><br>
           Here is your daily report.<br><br>
           Regards,<br>
           Automated System
        </p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via SMTP server.
    try:
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.starttls()
        smtp_obj.login(email_sender, 'your_email_password')  # Replace with your email password or use environment variables
        smtp_obj.sendmail(email_sender, email_receiver, msg.as_string())
        smtp_obj.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: unable to send email. {e}")

# Schedule the daily report to be sent at a specific time
schedule.every().day.at("08:00").do(send_email)  # Adjust the time as per your requirement

# Main loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
