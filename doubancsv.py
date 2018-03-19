#将豆瓣读书250信息写入csv文件
import csv
import requests
from bs4 import BeautifulSoup
fp=open('D://1.csv','w+',newline='',encoding='utf-8')
writer=csv.writer(fp)
urls=['https://book.douban.com/top250?start={}'.format(i)for i in range(0,250,25)]
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}
try:
    for url in urls:
        wb=requests.get(url,headers=headers)
        soup=BeautifulSoup(wb.text,'lxml')
        names=soup.find_all('div',{'class':'pl2'})
        us=soup.find_all('div',{'class':'pl2'})
        authors=soup.find_all('p',{'class':'pl'})
        publishers=soup.find_all('p',{'class':'pl'})
        dates=soup.find_all('p',{'class':'pl'})
        prices=soup.find_all('p',{'class':'pl'})
        rates=soup.find_all('span',{'class':'rating_nums'})
        comments=soup.find_all('span',{'class':'inq'})
        for name,u,author,publisher,date,price,rate,comment in zip(names,us,authors,publishers,dates,prices,rates,comments):
            print(name.a['title'],u.a['href'],author.text.split('/')[0],publisher.text.split('/')[-3],date.text.split('/')[-2],price.text.split('/')[-1],rate.text,comment.text)
            writer.writerow((name.a['title'],u.a['href'],author.text.split('/')[0],publisher.text.split('/')[-3],date.text.split('/')[-2],price.text.split('/')[-1],rate.text,comment.text))
except:
    pass
fp.close()