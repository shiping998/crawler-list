# 豆瓣电影250
import requests
from bs4 import BeautifulSoup
import time
import re
import pymongo
client=pymongo.MongoClient('localhost',27017)
walden=client['walden']
movie=walden['movie']
def get(url):
    wb=requests.get(url)
    soup=BeautifulSoup(wb.text,'lxml')
    titles=soup.select(' div.hd > a > span:nth-of-type(1)')
    stars = soup.find_all('span', 'rating_num')
    contents=soup.select(' div.info > div.bd > p:nth-of-type(1)')
    for title,star,content in zip(titles,stars,contents):
        data = {
            'title': title.text,
            'star': star.text,
            'content':content.text.split('\xa0')[-3].split(' ')[0]
        }
        print(data)
        movie.insert_one(data)
    # for content in contents:
    #     m=content.text.split('\xa0')[-3]
    #     print(m.split(' ')[0])
def urls():
    url_list=[]
    for i in range(0,226,25):
        url='https://movie.douban.com/top250?start=%d'%i
        url_list.append(url)
    return url_list
for u in urls():
    get(u)
    time.sleep(2)
# get('https://movie.douban.com/top250')