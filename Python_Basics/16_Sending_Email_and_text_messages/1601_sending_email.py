#! python3
#1601_sending_email.py - Sending Email

#############
#	SMTP	#
#############
#Much like HTTP is the protocol used by computers to send web pages across
#the Internet, Simple Mail Transfer Protocol (SMTP) is the protocol used for
#sending email. SMTP dictates how email messages should be formatted,
#encrypted, and relayed between mail servers, and all the other details that
#your computer handles after you click Send. You don’t need to know these
#technical details, though, because Python’s smtplib module simplifies them
#into a few functions.
#SMTP just deals with sending emails to others. A different protocol,
#called IMAP, deals with retrieving emails sent to you.

###############
#Sending Email#
###############
#You may be familiar with sending emails from Outlook or Thunderbird
#or through a website such as Gmail or Yahoo! Mail. Unfortunately, Python
#doesn’t offer you a nice graphical user interface like those services. Instead,
#you call functions to perform each major step of SMTP, as shown in the following interactive shell example.

#Example code:
#>>> import smtplib
#>>> smtpObj = smtplib.SMTP('smtp.example.com', 587)
#>>> smtpObj.ehlo()
#(250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\
#n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
#>>> smtpObj.starttls()
#(220, b'2.0.0 Ready to start TLS')
#>>> smtpObj.login('bob@example.com', 'MY_SECRET_PASSWORD')
#(235, b'2.7.0 Accepted')
#>>> smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So
#long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
#{}
#>>> smtpObj.quit()
#(221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')

#In the following sections, we’ll go through each step, replacing the placeholders with 
#your information to connect and log in to an SMTP server, send an email, and disconnect from the server.

##############################
#Connecting to an SMTP Server#
##############################
# These settings will be different for each email provider, but a web search for <your provider> smtp settings 
#should turn up the server and port to use.

#The domain name for the SMTP server will usually be the name of
#your email provider’s domain name, with smtp. in front of it. For example,
#Gmail’s SMTP server is at smtp.gmail.com. Table 16-1 lists some common
#email providers and their SMTP servers. (The port is an integer value and
#will almost always be 587, which is used by the command encryption standard, TLS.)

#GMX
#					Posteingang (POP3)			Postausgang (SMTP)
#Server				pop.gmx.net					mail.gmx.net
#Port				995							587
#Verschlüsselung	SSL oder Verschlüsselung	STARTTLS, TLS oder Verschlüsselung

#create an SMTP object by calling smptlib.SMTP(), passing the domain
#name as a string argument, and passing the port as an integer argument.
#The SMTP object represents a connection to an SMTP mail server and has
#methods for sending emails. 

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpObj = smtplib.SMTP('mail.gmx.net', 587)
print(type(smtpObj))
#<class 'smtplib.SMTP'>

#You’ll need this SMTP object in order to call the methods that log you
#in and send emails. If the smptlib.SMTP() call is not successful, your SMTP
#server might not support TLS on port 587. In this case, you will need to
#create an SMTP object using smtplib.SMTP_SSL() and port 465 instead.

##################################
#Sending the SMTP “Hello” Message#
##################################
#Once you have the SMTP object, call its oddly named ehlo() method to “say
#hello” to the SMTP email server. This greeting is the first step in SMTP and
#is important for establishing a connection to the server. You don’t need to
#know the specifics of these protocols. Just be sure to call the ehlo() method
#first thing after getting the SMTP object or else the later method calls will
#result in errors.

smtpObj.ehlo()
#(250, b'gmx.com Hello PC-34.aitc.local [80.64.142.158]\n8BITMIME\nAUTH LOGIN PLAIN\nSIZE 69920427\nSTARTTLS')

#########################
#Starting TLS Encryption#
#########################
#If you are connecting to port 587 on the SMTP server (that is, you’re
#using TLS encryption), you’ll need to call the starttls() method next. Thisidle
#required step enables encryption for your connection. If you are connecting
#to port 465 (using SSL), then encryption is already set up, and you should
#skip this step.

smtpObj.starttls()
#(220, b'OK')

#starttls() puts your SMTP connection in TLS mode. The 220 in the
#return value tells you that the server is ready.

###############################
#Logging in to the SMTP Server#
###############################
#Once your encrypted connection to the SMTP server is set up, you can log
#in with your username (usually your email address) and email password by
#calling the login() method.

email = input('enter mail:')
password = input('enter password')
smtpObj.login(email, password)
#(235, b'Authentication succeeded')

#Gmail’s Appl ication-Specific Passwords
#Gmail has an additional security feature for Google accounts called applicationspecific passwords. If you receive an Application-specific password required
#error message when your program tries to log in, you will have to set up one
#of these passwords for your Python script. Check out the resources at http://
#nostarch.com/automatestuff/ for detailed directions on how to set up an application-specific password for your Google account.

#Pass a string of your email address as the first argument and a
#string of your password as the second argument. The 235 in the return
#value means authentication was successful. Python will raise an smtplib
#.SMTPAuthenticationError exception for incorrect passwords.

##################
#Sending an Email#
##################
#Once you are logged in to your email provider’s SMTP server, you can call
#the sendmail() method to actually send the email. 

#The sendmail() method requires three arguments.
#•	 Your email address as a string (for the email’s “from” address)
#•	 The recipient’s email address as a string or a list of strings for multiple
#		recipients (for the “to” address)
#•	 The email body as a string

#The return value from sendmail() is a dictionary. There will be one
#key-value pair in the dictionary for each recipient for whom email delivery
#failed. An empty dictionary means all recipients were successfully sent the email.

toMail = 'michael.czurda@alpha-itc.com'

#Bulding email Body with mime
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = toMail
msg['Subject'] = 'Test Mail'

emailText = 'Test Mail'
msg.attach(MIMEText(emailText, 'html'))

text = msg.as_string()
smtpObj.sendmail(email, toMail, text)

####################################
#Disconnecting from the SMTP Server#
####################################

smtpObj.quit()
# This will disconnect your program from the SMTP server.
