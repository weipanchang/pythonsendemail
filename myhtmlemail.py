#!/usr/bin/python

import smtplib

FROMADDR = "weipanchang@comcast.net"
LOGIN    = FROMADDR
PASSWORD = "nov18168"
TOADDRS  = ["weipanchang@yahoo.com"]
SUBJECT  = "SMTP HTML e-mail test"

message = """From: weipanchang <weipanchang@comcast.net>
To: weipanchang <weipanchang@yahoo.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format
<br><br>
<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

server = smtplib.SMTP('smtp.comcast.net', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, message)
server.quit()