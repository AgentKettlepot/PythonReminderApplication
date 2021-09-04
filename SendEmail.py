import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime as dt
import time
import SecretInfo
def SendEmail(Toaddr, MessageFromField, date, bigger_message):
    fromaddr = SecretInfo.getUser()
    toaddr = Toaddr
    # Reading in the HTML doc
    html = open("G:\VSCode Transfer\Virtual_Assistant\ReminderTemplate.html")
    tempMes = html.read()
    tempMes = str(tempMes).replace('{code}', MessageFromField)
    tempMes = str(tempMes).replace('{date}', date)
    tempMes = str(tempMes).replace('{Big_Mes}', bigger_message)
    message = MIMEText(tempMes, 'html')
    #message = MIMEText(html.read(), 'html')
    message['From']=SecretInfo.getUser()
    message['To']=toaddr
    message['Subject']="Reminder from VA-K"

    debug = False
    if debug:
        print(message.as_string())
    else:   
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(SecretInfo.getUser(), SecretInfo.getPassword())
        text = message.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

