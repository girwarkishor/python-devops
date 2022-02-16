import smtplib
import os


password = os.environ["mail_password"]
mail_obj = smtplib.SMTP('smtp.office365.com', 587)
mail_obj.starttls()
mail_obj.login("parameswara.kuna@outlook.com", password)
message = "Hello World"
mail_obj.sendmail("parameswara.kuna@outlook.com", "parameswara.kuna@gmail.com", message)
mail_obj.quit()




