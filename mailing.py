#!/usr/bin/python
import datetime
import os
import glob
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

# mail info about run
FILEPATH = r'/home/mvrchota/Documents/Assignments/Mark/170531/compare'
MAILFILEPATH = r'/home/mvrchota/Documents/Assignments/Mark/170531/compare/output'
if not os.path.exists(MAILFILEPATH):
    os.makedirs(MAILFILEPATH)
datestamp = str(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
# mail info about script run
f = open('%s/mailto/mailto.txt' % MAILFILEPATH, 'w+')
f.write("Welcome to PP BU Milestone comparison script v01\n")
f.write("Script has succesfully ran at \n")
f.write('%s' %datestamp)
f.write("\nNo further action required\n")
msg = MIMEMultipart(f.read())
f.close()
# mail properties, sender, receiver, body
print('Trying to send an email')
mailSender = 'mvrchota.mailing@gmail.com'
mailReciever = 'mvrchota@redhat.com,myarboro@redhat.com'
msg['Subject'] = 'The script finished successfully (ppBetaGA.py)'
msg['From'] = mailSender
msg['To'] = mailReciever
body = 'Script ppBetaGA has finished (%s). Attachments enclosed.' %datestamp
content = MIMEText(body)
# looking for latest output file to be attached
latestOutput = max(glob.glob('%s/*.txt' % MAILFILEPATH), key = os.path.getctime)
lOutputFile = latestOutput.replace('%s/' % MAILFILEPATH,"")
print('Latest output file found - %s' % lOutputFile)
# attaching output files
docs1 = MIMEBase('application', "octet-stream")
docs2 = MIMEBase('application', "octet-stream")
docs1.set_payload(open("%s/%s" % (MAILFILEPATH, lOutputFile), "rb").read())
docs2.set_payload(open("%s/mailto/mailto.txt" % MAILFILEPATH, "rb").read())
Encoders.encode_base64(docs1)
Encoders.encode_base64(docs2)

docs1.add_header('Content-Disposition', 'attachment; filename="Output.txt"')
docs2.add_header('Content-Disposition', 'attachment; filename="mail-info.txt"')
print('Files attached')
msg.attach(content)
msg.attach(docs1)
msg.attach(docs2)
# connecting to the server and sending the mail
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('mvrchota.mailing@gmail.com','mattytestingmail')
server.sendmail(mailSender, mailReciever.split(','), msg.as_string())
print('Mail sent to %s at %s' %(mailReciever, datestamp))
server.quit()
