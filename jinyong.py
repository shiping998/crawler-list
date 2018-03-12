#利用正则表达式爬取金庸小说
import re
import requests
import time
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}
# f=open('C:\\Users\\samuel\\Desktop\\ttbb.txt','a+')
def get_info(url):
    res=requests.get(url,headers=headers)
    # res.encoding = res.apparent_encoding
    # print(res.content.decode('gb18030'))
    if(res.status_code==200):
        contents=re.findall('<br>(.*?)<br>',res.content.decode('gb18030'),re.S)
        for content in contents:
            print(content)
            # f.write(content+'\n')
    else:
        pass
if __name__ == '__main__':

    urls=['http://www.my285.com/wuxia/jinyong/tlbb/{:0>3d}.htm'.format(i)for i in range(11,20)]
    for url in urls:
        # print(url)
        get_info(url)
        time.sleep(1)
# f.close()