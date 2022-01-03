import smtplib
import EmailConfiguration
import Servers

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Start server
host = "smtp.office365.com"
port = "587"
login = EmailConfiguration.login
password = EmailConfiguration.password

def send(ip):

    server = smtplib.SMTP(host,port)

    server.ehlo()
    server.starttls()
    server.login(login,password)

    # Email structure
    body = f"""
           <h3>Atenção!</h3>
           <p>O seguinte servidor se encontra offline: <b>{ip}</b></p>
           <p>Atenciosamente,</p>
           <p><font size="3" face="Verdana"><i><b>
           Severs Monitoring
           </b></i></font></p>
    """
    recipients = Servers.usersList()

    email_message = MIMEMultipart()
    email_message['From'] = login
    email_message['To'] = ", ".join(recipients)
    # Priority - 1 (Highest)|2 (High)|3 (Normal)|4 (Low)|5 (Lowest)
    email_message['X-Priority'] = '2'
    email_message['Subject'] = "!ALERT! - Server Offline!"
    email_message.attach(MIMEText(body,'html'))

    server.sendmail(email_message['From'],recipients,email_message.as_string())
    print("Email enviado para", recipients)

    server.quit()
