import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com")
server.login("users gmail","password")
server.sendmail("user gmail","reciepents mail id","message")
server.quit()
