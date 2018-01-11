#下载有声小说 天龙八部
import requests
import urllib.request
import time
from urllib.parse import quote
urls=[]
for i in range(1,51):
    url='http://psf.ysts8.com:8000/武侠小说/天龙八部/武侠小说_天龙八部_%02d.mp3?126553692138x1514646101x127016304892-05e5d568e042d0f0772b2cfd3242a17b?2'%i
    urls.append(url)
# print(urls)

j=1
for u in urls:
    r=requests.get(u)
    path = 'C:\\Users\\samuel\\Desktop\\test\\'+'天龙八部_%02d'%j+'.mp3'
    with open(path, 'wb') as fd:
        fd.write(r.content)
    # urllib.request.urlretrieve(u,path)
    print('下载武侠小说_天龙八部_%02d.mp3'%j)
    time.sleep(1)
    j=j+1





