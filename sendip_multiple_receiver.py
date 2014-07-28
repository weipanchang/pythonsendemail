#!/usr/bin/python

import urllib2
import sys
import os
import re
import time


from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
from email.MIMEText import MIMEText

def get_ip():    
    return urllib2.urlopen('http://ip.42.pl/raw').read()

time.sleep(30)    
content = str(get_ip())
last_ip = content
SMTPserver = 'outbound.att.net'
sender =     'weipanchang@att.net'
destination = ['changvan@mac.com', 'yangg_yuann@yahoo.com']

USERNAME = "weipanchang@att.net"
PASSWORD = "Taipei0880"

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'
subject="IP Address"


while True:
    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject']=       subject
        msg['From']   = sender # some SMTP servers will do this automatically, not all
    
        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.close()
    
    except Exception, exc:
        sys.exit( "mail failed; %s" % str(exc) ) # give a error message
    
    time.sleep(60)
    #content = str(get_ip())
    while last_ip == content:
        time.sleep(60)
        content = str(get_ip())
        continue
    last_ip = content
    
    
    