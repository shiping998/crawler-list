#监测电影更新，有更新给我发微信
import requests
from bs4 import BeautifulSoup
import os.path
import filecmp
def gettitle():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    url='http://www.aicili.pw/'
    data=requests.get(url,headers=headers)
    data.encoding = data.apparent_encoding
    soup=BeautifulSoup(data.text,'lxml')
    title=soup.find_all('h2',{'class','entry-title'})
    d=''
    for i in title:
        d=d+i.text+'\n'
    return d

print(gettitle())

if(not os.path.exists('old.txt')):
    with open('old.txt', 'w') as f:
        f.write(gettitle())


with open('new.txt','w') as f:
        f.write(gettitle())

r=filecmp.cmp('old.txt', 'new.txt')
if(r):
    print('相同')
else:
    print('不同')
    payload = {'text': '最新电影', 'desp': gettitle()}
    requests.get('http://sc.ftqq.com/SCU18154Tdda79a78a4b0ff6192e351192347b1545a3320ff21690.send', params=payload)
    with open('old.txt', 'w') as f:
        f.write(gettitle())





