# 爬取行政区划代码并生成对应的json文件
import requests
from bs4 import  BeautifulSoup
import re
import json
url='http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201703/t20170310_1471429.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
wb=requests.get(url, headers=headers)
wb.encoding = wb.apparent_encoding
soup=BeautifulSoup(wb.text,'lxml')
a=soup.find_all('p',{'class','MsoNormal'})
pat1=re.compile('[0-9]+')
# pat2=re.compile('[\u4e00-\u9fa5]+')
list=[]
for i in a:
    n = pat1.match("".join(i.text.split()))
    data={
        'code':n.group(),
        'local':"".join(i.text.split())[6:]
    }
    print(data)
    list.append(data)
    json_str = json.dumps(list)
with open('data.json','w') as f:
    json.dump(list,f,ensure_ascii=False)