#利用正则表达式爬取糗事百科
import requests
import re
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}
info_lists=[]
def get_info(url):
    res=requests.get(url)
    ids=re.findall('<h2>(.*?)</h2>',res.text,re.S)
    # print(ids)
    levels=re.findall('<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)
    # print(levels)
    sexs=re.findall('<div class="articleGender (.*?)">',res.text,re.S)
    # print(sexs)
    contents=re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    # print(contents)
    laughs=re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',res.text,re.S)
    # print(laughs)
    comments=re.findall('<i class="number">(\d+)</i>',res.text,re.S)
    # print(comments)
    for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
        info={
            'id':id.strip('\n'),
            'level':level,
            'sex':sex,
            'content':content.strip('\n'),
            'laugh':laugh,
            'comment':comment
        }
        info_lists.append(info)
    # print(info_lists)
if __name__ == '__main__':
    url='https://www.qiushibaike.com/8hr/page/1/'
    get_info(url)
    print(info_lists)
    for info_list in info_lists:
        try:
            f=open('E:/new.txt','a+')
            f.write(info_list['id']+'\n')
            f.write(info_list['level']+'\n' )
            f.write(info_list['sex'] +'\n')
            f.write(info_list['content']+'\n' )
            f.write(info_list['laugh']+'\n' )
            f.write(info_list['comment']+'\n\n' )
            f.close()
        except:
            pass