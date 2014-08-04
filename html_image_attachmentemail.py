#!/usr/bin/python

from smtplib import SMTP_SSL as SMTP
import base64
import urllib2
import sys
import os
import re
#import time
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email import Encoders
from HTMLParser import HTMLParser
from email.MIMEBase import MIMEBase

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
def strip_tags(html):
        s = MLStripper()
        s.feed(html)
        return s.get_data()

FROMADDR = 'weipanchang@gmail.com'
LOGIN    = FROMADDR
PASSWORD = "Newp455word"
SMTPserver = 'smtp.gmail.com'
TOADDRS  = ["weipanchang@yahoo.com"]


FILENAME1="multiple_attachment_email.py"
FILENAME2="html_image_attachmentemail.py"
FILES=[FILENAME1, FILENAME2]
IMAGEFILE='test.jpeg'

htmlmsgtext = ""
htmlmsgtext = """
<h2>This is my message body in HTML...</h2>
<p>\
Here is my python script that can send out attachments, embedded image
</p>
<ul>
<li>you are bad/li>
<li>you are bad boy</li>
<li>you are very bad boy</li>
<li>you are very very bad boy</li>
</ul>
<p><strong>Here are my attachments:</strong></p><br />
"""

msg = MIMEMultipart()
msg['Subject'] = 'Email with Attachemnt'
msg['From'] = FROMADDR
msg['Reply-to'] = LOGIN

server = SMTP(SMTPserver)
server.set_debuglevel(1)
server.ehlo()

server.login(LOGIN, PASSWORD)

#==========================================
if htmlmsgtext !="":
    msgtext = htmlmsgtext.replace('</br>',"\r").replace('<br />',"\r").replace('</p>',"\r")
    # Then strip all the other tags out
    msgtext = strip_tags(msgtext)
    body = MIMEMultipart('alternative')
    body.attach(MIMEText(msgtext))
    body.attach(MIMEText(htmlmsgtext, 'html'))
    msg.attach(body)


part = MIMEText("Hello I am sending an email from a python program")
msg.attach(part)

msg.preamble = 'Multipart massage.\n'
msg.epilogue = ''

part = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>image here!', 'html')
msg.attach(part)

fp = open(IMAGEFILE, 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
msgImage.add_header('Content-Disposition', 'inline', filename=IMAGEFILE)
msg.attach(msgImage)

# Read a file and encode it into base64 format
if FILES != []:
# This is the binary part(The Attachment):
    for FILENAME in FILES:
        part = MIMEApplication(open(FILENAME,"rb").read())
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % FILENAME)
        msg.attach(part)

server.sendmail(FROMADDR, TOADDRS, msg.as_string())
print ("Email Sent")
server.quit()