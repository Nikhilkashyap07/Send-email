import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)

ob.ehlo()
ob.starttls()

ob.login('gmail','password')
subject = "test python"
body = "this is a test mail sent from python"
msg = "Subject: {}\n\n{}".format(subject,body)

listadd = ["xyzgmail.com"]

ob.sendmail("@gmail.com",listadd,msg)

print("send mail")

ob.quit()