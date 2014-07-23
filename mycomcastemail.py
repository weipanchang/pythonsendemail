#!/usr/bin/python

import smtplib

FROMADDR = "weipanchang@comcast.net"
LOGIN    = FROMADDR
PASSWORD = "nov18168"
TOADDRS  = ["weipanchang@yahoo.com"]
SUBJECT  = "Test"

msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
msg += "This is only a test\r\n"

server = smtplib.SMTP('smtp.comcast.net', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg)
server.quit()