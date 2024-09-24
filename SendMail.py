import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

sender = "jovittajov24@gmail.com"
receiver = "ejogabyvh@emlhub.com"
subject = 'Test mail using python'
contents = '''
This is the content side for sending mail
'''

yag = yagmail.SMTP(user=sender, password=os.getenv('password'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email send!")