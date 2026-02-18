# import smtplib
# from email.mime.text import MIMEText

# # Gmail account
# sender_email = "kimanimargaret46@gmail.com"
# receiver_email = "kimanimargaret46@gmail.com"
# app_password = "fikouqwfjeejmtlh"

# # Email content
# msg = MIMEText("Hello! This is a test email from Flask.")
# msg["Subject"] = "SMTP Test"
# msg["From"] = sender_email
# msg["To"] = receiver_email

# try:
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(sender_email, app_password)
#         server.send_message(msg)
#         print("Email sent successfully!")
# except Exception as e:
#     print("Error:", e)
