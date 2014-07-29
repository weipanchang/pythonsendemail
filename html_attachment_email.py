#!/usr/bin/python

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

FILENAME1="multiple_attachment_email.py"
FILENAME2="test.bat"
FILES=[FILENAME1, FILENAME2]
FROMADDR = 'weipanchang@att.net'
LOGIN    = FROMADDR
PASSWORD = "Taipei0880"
SMTPserver = 'outbound.att.net'
TOADDRS  = ["weipanchang@yahoo.com", "wchang@pingshow.net"]

htmlmsgtext = """<h2>This is my message body in HTML...WOW!!!!!</h2>
<p>\
Hey, Hey, Ho, Ho, got a paragraph here. A lovely paragraph it is.\
You've never seen a better paragraph than this.\
I make some of the best paragraphs you have ever seen.\
Hey, Hey, Ho, Ho, got a paragraph here. A lovely paragraph it is.\
You've never seen a better paragraph than this.\
I make some of the best paragraphs you have ever seen.\
</p>
<ul>
<li>This is a list item</li>
<li>This is another list item</li>
<li>And yet another list item, pretty big list</li>
<li>OMG this is a long list!</li>
</ul>
<p><strong>Here are my attachments:</strong></p><br />"""

#==========================================

msgtext = htmlmsgtext.replace('</br>',"\r").replace('<br />',"\r").replace('</p>',"\r")
# Then strip all the other tags out
msgtext = strip_tags(msgtext)

msg = MIMEMultipart()
msg['Subject'] = 'Email with Attachemnt'
msg['From'] = FROMADDR
msg['Reply-to'] = LOGIN

server = SMTP(SMTPserver)
server.set_debuglevel(1)
server.ehlo()

server.login(LOGIN, PASSWORD)
part = MIMEText("Hello im sending an email from a python program")
msg.attach(part)

msg.preamble = 'Multipart massage.\n'
msg.epilogue = ''
body = MIMEMultipart('alternative')
body.attach(MIMEText(msgtext))
body.attach(MIMEText(htmlmsgtext, 'html'))
msg.attach(body)
# Read a file and encode it into base64 format
for FILENAME in FILES:
# This is the binary part(The Attachment):
    part = MIMEApplication(open(FILENAME,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=FILENAME)
    msg.attach(part)

server.sendmail(FROMADDR, TOADDRS, msg.as_string())
print ("Email Sent")
server.quit()