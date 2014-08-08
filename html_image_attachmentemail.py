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


FILENAME1="python_send_email.py"
FILENAME2="test3.jpeg"
FILES=[FILENAME1, FILENAME2]
IMAGEFILE1='test.jpeg'
IMAGEFILE2='test2.jpeg'
IMAGES = [IMAGEFILE1, IMAGEFILE2]

htmlmsgtext = ""

htmlmsgtext = """
<h2>This is my message body in HTML...</h2>
<p>\
Here is my python script that can send out attachments, embedded image
</p>
<ul>
<li>my kid got a new car</li>
<li>it is a mazda 6</li>
<li>we need to pay the insurance as sport car rate</li>
<li>more expansive</li>
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

part = MIMEText("The inline images file are show below  ")
msg.attach(part)

msg.preamble = 'Multipart massage.\n'
msg.epilogue = ''

if IMAGES != []:
    for k in range(len(IMAGES)):
        cid = "image" + str(k+1)
        html = """\
            <p>This is an inline image<br/>
                <img src="cid:%s">
            </p>
        """ % cid
        msgHtml = MIMEText(html, 'html')
        img = open(IMAGES[k], 'rb').read()
        msgImg = MIMEImage(img, 'png')
        msgImg.add_header('Content-ID', '<'+cid+'>')
        msgImg.add_header('Content-Disposition', 'inline', filename=IMAGES[k])
        msg.attach(msgHtml)
        msg.attach(msgImg)

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