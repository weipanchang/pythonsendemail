#!/usr/bin/env python

import smtplib
fromMy = 'yourMail@yahoo.com' # fun-fact: from is a keyword in python, you can't use it as variable, did abyone check if this code even works?
to  = 'weipanchang@yahoo.com'
subj='ip address'
date='7/16/2014'
message_text='Hello Or any thing you want to send'

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )

username = str('weipanchang')  
password = str('Lonna821')  

try :
    server = smtplib.SMTP("smtp.mail.yahoo.com",465)
    server.login(username,password)
    server.sendmail(fromMy, to,msg)
    server.quit()    
    print 'ok the email has sent '
except :
    print 'can\'t send the Email'