#!.env/bin/python3

from bs4 import BeautifulSoup
from lxml import html
import requests,csv
from urllib.parse import urlparse

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'    
}

url1="https://www.accuweather.com/en/id/jayapura/205373/weather-forecast/205373"
#url2="https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jayapura&AreaID=501447&Prov=24"
link=requests.get(url1,headers=header)
#print(BeautifulSoup(link.content,'lxml'))
sup=BeautifulSoup(link.content,'lxml')
#tmp=sup.find_all('div',class_='kiri')
#print(sup)
location_=''
temp_=''
page=sup.find_all('div',class_='temp')
for pg in page:
       #print(pg)
       l=pg.find('span',class_='after-temp').text
       if l=='C':
           temp_=pg.text

loc=sup.find('h1',class_='header-loc')
location_=loc.text
print()
#--------------------
print('AccuWeather Web Scrapping')
print('----------------------------')
print('Location   : '+location_)
print('Temperature: '+temp_)
print()
