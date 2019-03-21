#! python3
#1601_retrieving_deleting_email.py - Retrieving and Deleting Emails with IMAP

#############
#   IMAP    #
#############

#Just as SMTP is the protocol for sending email, the Internet Message Access
#Protocol (IMAP) specifies how to communicate with an email provider’s
#server to retrieve emails sent to your email address. Python comes with an
#imaplib module, but in fact the third-party imapclient module is easier to
#use. This chapter provides an introduction to using IMAPClient; the full
#documentation is at http://imapclient.readthedocs.org/.
#The imapclient module downloads emails from an IMAP server in a
#rather complicated format. Most likely, you’ll want to convert them from
#this format into simple string values. The pyzmail module does the hard job
#of parsing these email messages for you. You can find the complete documentation for PyzMail at http://www.magiksys.net/pyzmail/.
#Install imapclient and pyzmail from a Terminal window. Appendix A has
#steps on how to install third-party modules.

##########################################
#Retrieving and Deleting Emails with IMAP#
##########################################

#requires both the imapclient and pyzmail third-party modules. Just to give
#you an overview, here’s a full example of logging in to an IMAP server,
#searching for emails, fetching them, and then extracting the text of the
#email messages from them:

#>>> import imapclient
#>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#>>> imapObj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')
#'my_email_address@gmail.com Jane Doe authenticated (Success)'
#>>> imapObj.select_folder('INBOX', readonly=True)
#>>> UIDs = imapObj.search(['SINCE 05-Jul-2014'])
#>>> UIDs
#[40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
#>>> rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
#>>> import pyzmail
#>>> message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
#>>> message.get_subject()
#'Hello!
#>>> message.get_addresses('from')
#[('Edward Snowden', 'esnowden@nsa.gov')]
#>>> message.get_addresses('to')
#[(Jane Doe', 'jdoe@example.com')]
#>>> message.get_addresses('cc')
#[]
#>>> message.get_addresses('bcc')
#[]
#>>> message.text_part != None
#True
#>>> message.text_part.get_payload().decode(message.text_part.charset)
#'Follow the money.\r\n\r\n-Ed\r\n'
#>>> message.html_part != None
#True
#>>> message.html_part.get_payload().decode(message.html_part.charset)
#'<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-
#Al<br></div>\r\n'
#>>> imapObj.logout()

##############################
#Connection to an IMAP server#
##############################
#you need an IMAPClient object to connect to an IMAP server and
#receive email. First you’ll need the domain name of your email provider’s
#IMAP server. This will be different from the SMTP server’s domain name. 

#GMX
#                   Posteingang (IMAP)	        Postausgang (SMTP)
#Server	            imap.gmx.net	            mail.gmx.net
#Port	            993	                        587
#Verschlüsselung	SSL oder Verschlüsselung	STARTTLS, TLS oder Verschlüsselung

import imapclient
imapObj = imapclient.IMAPClient('imap.gmx.net',port=993, ssl=True)

#the imapObj variable will contain an IMAPClient object returned from the
#imapclient.IMAPClient() function. In this context, a client is the object that
#connects to the server

###############################
#Logging in to the IMAP Server#
###############################
# IMAPClient object, call its login() method, passing in the
#username (this is usually your email address) and password as strings.
email = input('Mailadresse: ')
password = input('Passwort: ')
imapObj.login(email,password)
#b'LOGIN completed'

#Python will raise an imaplib.error exception. For Gmail accounts, you may
#need to use an application-specific password; for more details, see “Gmail’s
#Application-Specific Passwords” on page 365.

#####################
#Searching for Email#
#####################
#Once you’re logged on, actually retrieving an email that you’re interested
#in is a two-step process. First, you must select a folder you want to search
#through. Then, you must call the IMAPClient object’s search() method, passing in a string of IMAP search keywords.

###Selecting a folder
#Almost every account has an INBOX folder by default, but you can also get a
#list of folders by calling the IMAPClient object’s list_folders() method. This
#returns a list of tuples. Each tuple contains information about a single
#folder.

import pprint
pprint.pprint(imapObj.list_folders())
#[((b'\\Archive', b'\\HasNoChildren'), b'/', 'Archiv'),
# ((b'\\HasNoChildren',), b'/', 'Archivieren'),
# ((b'\\Drafts', b'\\NoInferiors'), b'/', 'Entwürfe'),
# ((b'\\Trash', b'\\HasNoChildren'), b'/', 'Gelöscht'),
# ((b'\\Sent', b'\\NoInferiors'), b'/', 'Gesendet'),
# ((b'\\HasNoChildren',), b'/', 'INBOX'),
# ((b'\\NoInferiors',), b'/', 'OUTBOX'),
# ((b'\\Junk', b'\\NoInferiors'), b'/', 'Spamverdacht')]

#•A tuple of the folder’s flags. (Exactly what these flags represent is beyond the scope of this book, and you can safely ignore this field.)
#•The delimiter used in the name string to separate parent folders and subfolders.
#•The full name of the folder.

#To select a folder to search through, pass the folder’s name as a string
#into the IMAPClient object’s select_folder() method.

imapObj.select_folder('INBOX', readonly=True)

#You can ignore select_folder()’s return value. If the selected folder does
#not exist, Python will raise an imaplib.error exception.
#The readonly=True keyword argument prevents you from accidentally
#making changes or deletions to any of the emails

###Performing the Search
#With a folder selected, you can now search for emails with the IMAPClient
#object’s search() method. The argument to search() is a list of strings, each
#formatted to the IMAP’s search keys. 

#Search keys
#Search key          Meaning
#'ALL'               Returns all messages in the folder. You may run in to imaplib
#                    size limits if you request all the messages in a large folder. See
#                    “Size Limits” on page 371.
#'BEFORE date',
#'ON date',
#'SINCE date'        These three search keys return, respectively, messages that
#                    were received by the IMAP server before, on, or after the
#                    given date. The date must be formatted like 05-Jul-2015.
#                    Also, while 'SINCE 05-Jul-2015' will match messages on
#                    and after July 5, 'BEFORE 05-Jul-2015' will match only messages before July 5 but not on July 5 itself.
#'SUBJECT string',
#'BODY string',
#'TEXT string'       Returns messages where string is found in the subject, body,
#                    or either, respectively. If string has spaces in it, then enclose
#                    it with double quotes: 'TEXT "search with spaces"'.
#'FROM string',
#'TO string',
#'CC string',
#'BCC string'        Returns all messages where string is found in the “from”
#                    emailaddress, “to” addresses, “cc” (carbon copy) addresses,
#                    or “bcc” (blind carbon copy) addresses, respectively. If there
#                    are multiple email addresses in string, then separate them
#                    with spaces and enclose them all with double quotes:
#                    'CC "firstcc@example.com secondcc@example.com"'.
#'SEEN',
#'UNSEEN'            Returns all messages with and without the \Seen flag, respectively. An email obtains the \Seen flag if it has been accessed
#                    with a fetch() method call (described later) or if it is clicked
#                    when you’re checking your email in an email program or web
#                    browser. It’s more common to say the email has been “read”
#                    rather than “seen,” but they mean the same thing.
#'ANSWERED',
#'UNANSWERED'        Returns all messages with and without the \Answered flag,
#                    respectively. A message obtains the \Answered flag when it
#                    is replied to.
#'DELETED',
#'UNDELETED'         Returns all messages with and without the \Deleted flag, respectively. Email messages deleted with the delete_messages()
#                    method are given the \Deleted flag but are not permanently
#                    deleted until the expunge() method is called (see “Deleting
#                    Emails” on page 375). Note that some email providers, such
#                    as Gmail, automatically expunge emails.
#'DRAFT',
#'UNDRAFT'           Returns all messages with and without the \Draft flag, respectively. Draft messages are usually kept in a separate Drafts
#                    folder rather than in the INBOX folder.
#'FLAGGED',
#'UNFLAGGED'         Returns all messages with and without the \Flagged flag,
#                    respectively. This flag is usually used to mark email messages as “Important” or “Urgent.”
#'LARGER N',
#'SMALLER N'         Returns all messages larger or smaller than N bytes, respectively.
#'NOT search-key'    Returns the messages that search-key would not have returned.
#'OR search-key1 search-key2'    Returns the messages that match either the first or second search-key.

#You can pass multiple IMAP search key strings in the list argument to
#the search() method. The messages returned are the ones that match all the
#search keys. If you want to match any of the search keys, use the OR search
#key. For the NOT and OR search keys, one and two complete search keys follow
#the NOT and OR, respectively. 

#Examples:
print(imapObj.search(['ALL']))
#Returns every message in the currently selected folder

print(imapObj.search(['UNSEEN']))
#unseen

print(imapObj.search(['ON', '18-Mar-2019']))
#received at

print(imapObj.search([['SINCE', '01-Jan-2019'],['BEFORE','01-Mar-2019']]))

print(imapObj.search(['OR', 'FROM', 'michael.czurda@alpha-itc.com', 'FROM' ,'m.czurda@gmx.at']))
#OR Selection

#The search() method doesn’t return the emails themselves but rather
#unique IDs (UIDs) for the emails, as integer values. You can then pass these
#UIDs to the fetch() method to obtain the email content.

###SIze Limits
#If your search matches a large number of email messages, Python might
#raise an exception that says imaplib.error: got more than 10000 bytes. When
#this happens, you will have to disconnect and reconnect to the IMAP server and try again.
#This limit is in place to prevent your Python programs from eating up
#too much memory. Unfortunately, the default size limit is often too small.
#You can change this limit from 10,000 bytes to 10,000,000 bytes by running
#this code:
import imaplib
imaplib._MAXLINE = 1000000

#######################################
#Fetching an Email and mark it as read#
#######################################

#Once you have a list of UIDs, you can call the IMAPClient object’s fetch()
#method to get the actual email content.
#The list of UIDs will be fetch()’s first argument. The second argument
#should be the list ['BODY[]'], which tells fetch() to download all the body
#content for the emails specified in your UID list.

UIDs = imapObj.search(['ON', '18-Mar-2019'])

import pprint
rawmessages= imapObj.fetch(UIDs, ['BODY[]'])
pprint.pprint(rawmessages)

##When you selected a folder to search through, you called select_folder()
#with the readonly=True keyword argument. Doing this will prevent you from
#accidentally deleting an email—but it also means that emails will not get
#marked as read if you fetch them with the fetch() method. If you do want
#emails to be marked as read when you fetch them, you will need to pass
#readonly=False to select_folder(). If the selected folder is already in 
#readonly mode, you can reselect the current folder with another call to select_
#folder(), this time with the readonly=False keyword argument

############################################
#Getting Email Addresses from a Raw Message#
############################################

#The raw messages returned from the fetch() method still aren’t very useful to 
#people who just want to read their email. The pyzmail module parses
#these raw messages and returns them as PyzMessage objects, which make the
#subject, body, “To” field, “From” field, and other sections of the email easily
#accessible to your Python code.

##=> can't install pyzmail, see book page 373

#################
#Deleting Emails#
#################
UIDs = imapObj.search(['ON', '18-Mar-2019'])
#imapObj.delete_messages(UIDs)

#Calling delete_message() and passing it UIDs returns a dictionary;
#each key-value pair is a message ID and a tuple of the message’s flags, which
#should now include \Deleted

#Calling expunge() then permanently deletes
#messages with the \Deleted flag and returns a success message if there were
#no problems expunging the emails.

# imapObj.expunge()

############
#Disconnect#
############
imapObj.logout()
