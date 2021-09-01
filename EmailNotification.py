import smtplib
import email.message

import EmailConfiguration

def send(ip):

    #Data Email
    body = f"""
    <p>Prezados,</p>
    <p>O(s) serguinte(s) servidore(s) se encontra(m) off-line no momento: {ip}</p>
    """
    message = email.message.Message()
    message['Subject'] = "Test"
    message['From'] = EmailConfiguration.email
    message['To'] = EmailConfiguration.list
    password = EmailConfiguration.password
    message.add_header('Content-Type','text/html')
    message.set_payload(body)

    #MailServer Configuration
    send = smtplib.SMTP('smtp.office365.com: 587')
    send.starttls()

    #Login
    send.login(message['From'], password)
    send.sendmail(message['From'], [message['To']], message.as_string().encode('utf-8'))
    print('!Email Sent!')

ip = "8.8.8.8"
send(ip)