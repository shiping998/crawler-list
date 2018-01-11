#批量下载《读者》文章
from bs4 import BeautifulSoup
import requests
import os

# url='http://www.52duzhe.com/'+time+'/index.html'
def urlbs(url):
    wb_data = requests.get(url)
    wb_data.encoding = wb_data.apparent_encoding
    soup = BeautifulSoup(wb_data.text,'lxml')
    return soup
def main(url):
    soup=urlbs(url)
    link=soup.select('.booklist a')
    path=os.getcwd()+u'/读者文章/'
    if not os.path.isdir(path):
        os.mkdir(path)
    for item in link:
        newurl='http://www.52duzhe.com/' + time +'/'+item.get('href')
        print(newurl)
        result=urlbs(newurl)
        title=result.find('h1').string
        # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
        writer=result.find(id='pub_date').string.strip()
        print(writer)
        filename=path+title+'.txt'
        print(filename)
        new=open(filename,'w')
        new.write("<<" + title + ">>\n\n")
        new.write(writer+"\n\n")
        text = result.select('.blkContainerSblkCon p')
        for p in text:
            context = p.text
            new.write(context)
        new.close()
time = '2017_08'
firsturl='http://www.52duzhe.com/'+time+'/index.html'
main(firsturl)
