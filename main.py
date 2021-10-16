#!.env/bin/python3

from bs4 import BeautifulSoup
from lxml import html
import requests,csv
from urllib.parse import urlparse

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'    
}

url1="https://www.accuweather.com/en/id/bayangkara/3490311/weather-forecast/3490311"
url2="https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jayapura&AreaID=501447&Prov=24"
link=requests.get(url1,headers=header)
print(BeautifulSoup(link.content,'lxml'))
#sup=BeautifulSoup(link,'html.parser')
#tmp=sup.find_all('div',class_='kiri')
#print(sup)

#page=sup.find_all('p',class_='title')
#for pg in tmp:
#       print(pg)

#print('hello world')

