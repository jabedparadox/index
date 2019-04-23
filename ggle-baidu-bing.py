#!/usr/bin/python
#!/usr/bin/python3
#!/usr/bin/env python
#!/usr/bin/env python3
# -*- coding: utf8 -*-

# updated language.
# date                 :-  
# author               :- Md Jabed Ali(jabed)

import random
from json import loads
import requests
from bs4 import BeautifulSoup
import argparse
import re
#import aiohttp
import argparse
import os
import sys
#from google.cloud import translate

print("******************************** Md Jabed Ali(jabed) **********************************\n************************************ Translator ***************************************\n******** Example:- Translate to: Enter 1 for Afrikaans / Enter 2 for Albanian  ********\n\n1-Afrikaans~af   2-Albanian~sq       3-Amharic~am         4-Arabic~ar     5-Armenian~hy\n6-Azerbaijani~az 7-Basque~eu         8-Belarusian~be      9-Bengali~bn    10-Bosnian~bs\n11-Bulgarian~bg  12-Catalan~ca       13-Cebuano~ceb       14-Chichewa~ny  15-Chinese~zh-CN\n16-Corsican~co   17-Croatian~hr      18-Czech~cs          19-Danish~da    20-Dutch~nl\n21-English~en    22-Esperanto~eo     23-Estonian~et       24-Filipino~tl  25-Finnish~fi\n26-French~fr     27-Frisian~fy       28-Galician~gl       29-Georgian~ka  30-German~de\n31-Greek~el      32-Gujarati~gu      33-Haitian Creole~ht 34-Hausa~ha     35-Hawaiian~haw\n36-Hebrew~iw     37-Hindi~hi         38-Hmong~hmn         39-Hungarian~hu 40-Icelandic~is\n41-Igbo~ig       42-Indonesian~id    43-Irish~ga          44-Italian~it   45-Japanese~ja\n46-Javanese~jw   47-Kannada~kn       48-Kazakh~kk         49-Khmer~km     50-Korean~ko\n51-Kurdish~ku    52-Kyrgyz~ky        53-Lao~lo            54-Latin~la     55-Latvian~lv\n56-Lithuanian~lt 57-Luxembourgish~lb 58-Macedonian~mk     59-Malagasy~mg  60-Malay~ms\n61-Malayalam~ml  62-Maltese~mt       63-Maori~mi          64-Marathi~mr   65-Mongolian~mn\n66-Myanmar~my    67-Nepali~ne        68-Norwegian~no      69-Pashto~ps    70-Persian~fa\n71-Polish~pl     72-Portuguese~pt    73-Punjabi~pa        74-Romanian~ro  75-Russian~ru\n76-Samoan~sm     77-Scots Gaelic~gd  78-Serbian~sr        79-Sesotho~st   80-Shona~sn\n81-Sindhi~sd     82-Sinhala~si       83-Slovak~sk         84-Slovenian~sl 85-Somali~so\n86-Spanish~es    87-Sundanese~su     88-Swahili~sw        89-Swedish~sv   90-Tajik~tg\n91-Tamil~ta      92-Telugu~te        93-Thai~th           94-Turkish~tr   95-Ukrainian~uk\n96-Urdu~ur       97-Uzbek~uz         98-Vietnamese~vi     99-Welsh~cy     100-Xhosa~xh\n101-Yiddish~yi   102-Yoruba~yo       103-Zulu~zu\n\n*********************************** Translator **************************************\n")

# different headers.
def random_useragent():
    #http://useragentstring.com/pages/useragentstring.php
    url = "https://fake-useragent.herokuapp.com/browsers/0.1.8"
    r = requests.get(url)
    randomuseragent = loads(r.text)['browsers']
    #print(random.choice(randomuseragent[random.choice(list(randomuseragent))]))
    return random.choice(randomuseragent[random.choice(list(randomuseragent))])

u_a = random_useragent()
headers = {'User-Agent': u_a,
           #'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
           #':authority': 'translate.google.com',
           #':scheme': 'https',
           'X-Requested-With': 'XMLHttpRequest',
           'Upgrade-Insecure-Requests': '1',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,application/json,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           #'Origin': ' ',
           #'Host': ' ',
}

# Which lang.
def translateto():
     while True:
          trnslt_to = input("Translate to: ")
          if trnslt_to.isdigit():
               return trnslt_to
               break
          else:
               print ("Enter a digit.")

# Translating frm baidu.
#def baidu_translate():
     #trnslt_to = input("Translate to: ")

# Translating frm googel.
def googel_translate():
     while True:
          trnslt_to = translateto()
          #trnslt_to = input("Translate to: ")
          if trnslt_to == '1':
               tl = 'Afrikaans~af'
          elif trnslt_to == '2':
               tl = 'Albanian~sq'
          elif trnslt_to == '3':
               tl = 'Amharic~am'
          elif trnslt_to == '4':
               tl = 'Arabic~ar'
          elif trnslt_to == '5':
               tl = 'Armenian~hy'
          elif trnslt_to == '6':
               tl = 'Azerbaijani~az'
          elif trnslt_to == '7':
               tl = 'Basque~eu'
          elif trnslt_to == '8':
               tl = 'Belarusian~be'
          elif trnslt_to == '9':
               tl = 'Bengali~bn'
          elif trnslt_to == '10':
               tl = 'Bosnian~bs'         
          elif trnslt_to == '21':
               tl = 'en'    
          inputtext = input("Enter text: ")
          url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=' + tl.split('~')[-1] + '&dt=t&q=' + inputtext
          res = requests.get(url, headers=headers).text
          print ("Translating to " + tl.split('~')[0] + " .....")
          print ('\n' + inputtext + ' <-> ' + re.findall('"(.*?)"', str(res), re.DOTALL)[0] + '\n')
          agn = input("Want to translate again? (Y/N): ")
          if agn == 'Y':
               pass
          else:
               sys.exit()

if __name__ == '__main__':
     googel_translate()

#https://api.fanyi.baidu.com , https://fanyi.baidu.com/
#https://translation.googleapis.com/language/translate/v2/?q={}&source={}&target=en&key={}
#https://www.bing.com/ttranslationlookup?&IG={}&IID={}, https://www.bing.com/ttransliterate?&IG={}&IID={}
#https://translate.yandex.net/api/v1/tr.json/translate?id={}&srv=tr-text&lang=en-bn&reason=auto
#https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=en&srv=tr-text&sid=b3588136.5cbebd2e.54a55b9f&text={}&dict=&flags=

#yandex
'''
text: synchronized
options: 4
'''

#bing.
'''from: en
to: bn-BD
text: best /
language: 
toScript: 
text: 
'''

# googleapis.
'''
'q': '',
'source': 'en',
'target': 'es',
'format': 'text'
'''

# baidu.
'''
from: zh
to: en
query:  
transtype:  
simple_means_flag:  
sign:  
token:  '''

'''print("1-Afrikaans~af   2-Albanian~sq       3-Amharic~am         4-Arabic~ar     5-Armenian~hy
         6-Azerbaijani~az 7-Basque~eu         8-Belarusian~be      9-Bengali~bn    10-Bosnian~bs
         11-Bulgarian~bg  12-Catalan~ca       13-Cebuano~ceb       14-Chichewa~ny  15-Chinese~zh-CN
         16-Corsican~co   17-Croatian~hr      18-Czech~cs          19-Danish~da    20-Dutch~nl
         21-English~en    22-Esperanto~eo     23-Estonian~et       24-Filipino~tl  25-Finnish~fi
         26-French~fr     27-Frisian~fy       28-Galician~gl       29-Georgian~ka  30-German~de
         31-Greek~el      32-Gujarati~gu      33-Haitian Creole~ht 34-Hausa~ha     35-Hawaiian~haw
         36-Hebrew~iw     37-Hindi~hi         38-Hmong~hmn         39-Hungarian~hu 40-Icelandic~is
         41-Igbo~ig       42-Indonesian~id    43-Irish~ga          44-Italian~it   45-Japanese~ja
         46-Javanese~jw   47-Kannada~kn       48-Kazakh~kk         49-Khmer~km     50-Korean~ko
         51-Kurdish~ku    52-Kyrgyz~ky        53-Lao~lo            54-Latin~la     55-Latvian~lv
         56-Lithuanian~lt 57-Luxembourgish~lb 58-Macedonian~mk     59-Malagasy~mg  60-Malay~ms
         61-Malayalam~ml  62-Maltese~mt       63-Maori~mi          64-Marathi~mr   65-Mongolian~mn
         66-Myanmar~my    67-Nepali~ne        68-Norwegian~no      69-Pashto~ps    70-Persian~fa
         71-Polish~pl     72-Portuguese~pt    73-Punjabi~pa        74-Romanian~ro  75-Russian~ru
         76-Samoan~sm     77-Scots Gaelic~gd  78-Serbian~sr        79-Sesotho~st   80-Shona~sn
         81-Sindhi~sd     82-Sinhala~si       83-Slovak~sk         84-Slovenian~sl 85-Somali~so
         86-Spanish~es    87-Sundanese~su     88-Swahili~sw        89-Swedish~sv   90-Tajik~tg
         91-Tamil~ta      92-Telugu~te        93-Thai~th           94-Turkish~tr   95-Ukrainian~uk
         96-Urdu~ur       97-Uzbek~uz         98-Vietnamese~vi     99-Welsh~cy     100-Xhosa~xh
         101-Yiddish~yi   102-Yoruba~yo       103-Zulu~zu")'''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
