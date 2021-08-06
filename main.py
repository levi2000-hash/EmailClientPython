import smtplib,ssl
from getpass import getpass

mailAddress = input("Enter your e-mail address: ")
password = getpass()
receiver = input("Receiver address: ")
serverAddress = "smtp.gmail.com"
port = 587
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
message = input("Type your message here:\n")

with smtplib.SMTP(serverAddress,port) as server:
	server.ehlo()
	server.starttls(context=context)
	server.ehlo()
	server.login(mailAddress,password)
	server.sendmail(mailAddress,receiver,message)