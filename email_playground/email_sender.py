import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'tsmithdeveloper@hotmail.com'
email['to'] = 'newnoodogs@hotmail.com'
email['subject'] = 'You are something...'

email.set_content(html.substitute({'name':'Megatron'}), 'html')

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('tsmithdeveloper@hotmail.com','Chimp@nZee!1977')
    smtp.send_message(email)
    print('Yup. Uh-huh.')
