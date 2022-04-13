import random
import smtplib
from sre_constants import SUCCESS
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
password='yctgmsegvlgevkro'
server.login("ssmeduri2006@gmail.com",password)
otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello, Your OTP is '+str(otp)
sender='ssmeduri2006@gmail.com'
rec=input("Enter your mail ID:")
receiver={str(rec)} 
server.sendmail(sender,receiver,msg)
verify=input("Enter the code sent to thee above mail ID:")
if verify == otp:
    print("Verification SUCCESS")
else:
    print("Verification Failed.Try Again")


server.quit()