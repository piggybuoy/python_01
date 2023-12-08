import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'tsmithdeveloper@hotmail.com'
email['to'] = 'newnoodogs@hotmail.com'
email['subject'] = 'You are something...'

email.set_content('The tron is all mega up in here.')

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('tsmithdeveloper@hotmail.com','Chimp@nZee!1977')
    smtp.send_message(email)
    print('Yup. Uh-huh.')
