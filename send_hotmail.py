#!/usr/bin/env python

import smtplib
  
smtpserver = 'smtp.live.com'
AUTHREQUIRED = 1 # if you need to use SMTP AUTH set to 1
smtpuser = 'weipanchang@hotmail.com'  # for SMTP AUTH, set SMTP username here
smtppass = 'nov18168'  # for SMTP AUTH, set SMTP password here
    
RECIPIENTS = 'wchang@pingshow.net'
SENDER = 'weipanchang@hotmail.com'
mssg =  "Subject: Hello\n\nThis is the body of the message."
s = mssg  
 
server = smtplib.SMTP(smtpserver,587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(smtpuser,smtppass)
server.set_debuglevel(1)
server.sendmail(SENDER, [RECIPIENTS], s)
server.quit()