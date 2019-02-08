import requests
from bs4 import BeautifulSoup as bs
import re
from time import sleep
import os
from filename import filename

url = 'http://kcm.co.kr/bible/korea.html'
path = os.path.dirname(os.path.abspath(__file__))
index = requests.get(url).content.decode('euc-kr')
in_bs = bs(index,'html.parser')
bibles = in_bs.find_all(text=re.compile(".*[0-9][0-9]?장"))
if os.path.exists(path+'/bible'):
    pass
else:
    os.makedir(path+'/bible')
for bible in bibles:
   n_url = bible.parent['href']
   n_name = str(n_url).split('/')[-1]
   if os.path.isfile(path_+'/bible/'+n_name):
       pass
   else:
       try:
           n_bs = bs(requests.get('http://kcm.co.kr'+n_url).content,'html.parser')
       except:
           n_bs =bs('','html.parser')
       f = open(path+'/bible/'+n_name, 'a')
       for table in n_bs.find_all('table'):
           f.write(table.get_text())
       for footnote in n_bs.find_all('a',attrs={'name':'bottom'}):
           text = footnote.get_text()
           text = text.replace('Previous chapter,','')
           text = text.replace('Next chapter,','')
           text = text.replace('Previous Book,','')
           text = text.replace('Next Book,','')
           text = text.replace('KJV','')
           f.write(text)
       f.close()
       print('saved '+n_name)
       sleep(1)

filename()
