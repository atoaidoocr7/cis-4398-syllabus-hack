import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_emails):
    #email configuration
    email_user = 'cis4398bot@outlook.com'
    email_password = 'cis4398cis'

    #Construct the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_user
    recipients_string = ', '.join(to_emails)
    msg['To'] = recipients_string

    try:
        #this line set up connection to outlook service, the number is the port number for outlook
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)

        #security check make sure we only takling to outllok
        server.starttls()

        #greet the server
        server.ehlo()

        #login to the reminderr bot enmail account
        server.login(email_user, email_password)

        #set up the email
        server.sendmail(email_user, to_emails, msg.as_string())

        #close serice after sent
        server.close()
        print('Email sent!')

    except Exception as e:
        print(f'Error sending email: {e}')

