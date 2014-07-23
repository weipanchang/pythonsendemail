#!/usr/bin/python

import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP

FILENAME="Allen.jpg"
FROMADDR = "weipanchang@comcast.net"
LOGIN    = FROMADDR
PASSWORD = "nov18168"
TOADDRS  = ["weipanchang@yahoo.com", "weipanchang@comcast.net"]

#==========================================
msg = MIMEMultipart()
msg['Subject'] = 'Email with Attachemnt'
msg['From'] = FROMADDR
msg['Reply-to'] = LOGIN
msg['To'] = TOADDRS[0]

filename = "array.py"
# Read a file and encode it into base64 format
msg.preamble = 'Multipart massage.\n'

# This is the textual part:
part = MIMEText("Hello im sending an email from a python program")
msg.attach(part)

# This is the binary part(The Attachment):
part = MIMEApplication(open(FILENAME,"rb").read())
part.add_header('Content-Disposition', 'attachment', filename=FILENAME)
msg.attach(part)

server = smtplib.SMTP('smtp.comcast.net', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg.as_string())
server.quit()