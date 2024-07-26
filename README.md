# Python Script To Automate Sending Daily Email Reports

Make sure you have Python installed on your system. You’ll also need to install the **schedule library**, which helps in scheduling tasks, and **smtplib** for sending emails.

## Customize and Configure

**Email Configuration:** Replace **email_sender, email_receiver, and 'your_email_password'** with your actual email credentials and recipient's email.
**Message Content:** Customize text and html variables to include the content of your daily report.
**### Scheduling:** Adjust the time in **schedule.every().day.at("08:00").do(send_email)** to the desired time of day when you want the report to be sent.
