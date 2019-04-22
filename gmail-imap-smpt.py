#!/usr/bin/python
#!/usr/bin/python3
# -*- coding: utf8 -*-

# Gmail smpt & IMAP4_SSL.
# Allow less secure apps.
# Date                 : 16/07/2017
# Author               : Md Jabed Ali(jabed)

import smtplib
import time
from random import randint
import random
import string
import imaplib, email
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#import *
#from antigate import AntiGate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#For Selenium/Panthom.
#driver.find_element_by_id('submitbutton').submit()
#url_captcha = driver.find_element_by_id('recaptcha_challenge_image').get_attribute("src")
#

#def password(self):
        #return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))

#Split address into name,address.
#def splitaddrs(add):
    #if not(add): return []

def random_useragent():
    #http://useragentstring.com/pages/useragentstring.php
    url = "https://fake-useragent.herokuapp.com/browsers/0.1.8"
    r = requests.get(url)
   randomuseragent = loads(r.text)['browsers']
    #print(random.choice(randomuseragent[random.choice(list(randomuseragent))]))
    return random.choice(randomuseragent[random.choice(list(randomuseragent))])

#ua = random_useragent()

#Gmail IMAP4_SSL.
'''userid   = ''
password   = ''
mail=imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(userid,password)
mail.select("INBOX")
result,data= mail.search(None,"ALL")
ids=data[0].split()
msgs = mail.fetch(','.join(ids),'(BODY.PEEK[HEADER])')[1][0::2]
addr=[]'''

#Retrieving email.
#for x,msg in msgs:
    #msgobj = email.message_from_string(msg)
    #addr.extend(splitaddrs(msgobj['to']))

#Email credential.
addr_to   = ''
addr_from = 'jabed.akcc@gmail.com'
#smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_user   = 'jabed.akcc@gmail.com'
smtp_pass   = ''
 
#Construct email
msg = MIMEMultipart('alternative')
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Subject'
 
#Body of the message (a plain-text and an HTML version).
text = "This is a test message.\nText and html."
html = """\
<!DOCTYPE html> 
<html lang="en">
     html message.
</html>
"""
 
#MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')  #Preferred.
 
#Attach both into message container.
msg.attach(part1)
msg.attach(part2)

#Send mail with SMTP.
def mailing():
    for i in range():
        time.sleep()
        try:
            m = smtplib.SMTP('smtp.gmail.com', 587)
            m.ehlo()
            m.starttls()
            m.login(smtp_user,smtp_pass)
            m.sendmail(addr_from, addr_to, msg.as_string())
            m.quit()
            print (i, "Sent")
        except:
            print(i, "There was an error sending the email. Check the smtp settings.")
if __name__ == "__main__":
    mailing()
    
