#!/usr/bin/python

#import smtplib
from smtplib import SMTP_SSL as SMTP 
import base64
import urllib2
import sys
import os
import re
#import time
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
#from smtplib import SMTP


FILENAME1="Cups.mp3"
FILENAME2="test.bat"
FILE=[FILENAME1, FILENAME2]
FROMADDR = 'weipanchang@att.net'
LOGIN    = FROMADDR
PASSWORD = "Taipei0880"
SMTPserver = 'outbound.att.net'
TOADDRS  = ["weipanchang@yahoo.com", "wchang@pingshow.net"]

#==========================================
msg = MIMEMultipart()
msg['Subject'] = 'Email with Attachemnt'
msg['From'] = FROMADDR
msg['Reply-to'] = LOGIN

# Read a file and encode it into base64 format
server = SMTP(SMTPserver)
server.set_debuglevel(1)
server.ehlo()
#server.starttls()
server.login(LOGIN, PASSWORD)
part = MIMEText("Hello im sending an email from a python program")
msg.attach(part)
msg.preamble = 'Multipart massage.\n'
for FILENAME in FILE:

# This is the textual part:

# This is the binary part(The Attachment):
    part = MIMEApplication(open(FILENAME,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=FILENAME)
    msg.attach(part)
    
server.sendmail(FROMADDR, TOADDRS, msg.as_string())
server.quit()