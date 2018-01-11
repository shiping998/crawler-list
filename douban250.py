# 爬取豆瓣top250的图书
import requests
from bs4 import BeautifulSoup
import time
import pymongo
# url='https://book.douban.com/top250'
client=pymongo.MongoClient('localhost',27017)
walden=client['walden']
douban=walden['douban']
def get(url):
    wb=requests.get(url)
    soup=BeautifulSoup(wb.text,'lxml')
    titles=soup.find_all('div',{'class':'pl2'})
    authors=soup.find_all('p','pl')
    stars=soup.find_all('span','rating_nums')
    for title,author,star in zip(titles,authors,stars):
        data={
            'content':info(title.a['href']),
            'title':title.a['title'],
            'author':author.text,
            'star':star.text
        }
        print(data)
        douban.insert_one(data)
def urls():
    url_list=[]
    for i in range(0,226,25):
        url='https://book.douban.com/top250?start=%d'%i
        url_list.append(url)
    return url_list
def info(url2):
    wb = requests.get(url2)
    soup = BeautifulSoup(wb.text, 'lxml')
    try:
        content=soup.find('div',{'class':'intro'}).text
    except:
        content =" "
    return content


for u in urls():
    get(u)
    time.sleep(2)


