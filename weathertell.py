import requests
from bs4 import BeautifulSoup
import re
from time import ctime
def getpm(city):
    url='http://www.pm25.com/'+city+'.html'
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    city = soup.find(class_='bi_loaction_city')  # 城市名称
    aqi = soup.find("a", {"class", "bi_aqiarea_num"})  # AQI指数
    quality = soup.select(".bi_aqiarea_right span")  # 空气质量等级
    result = soup.find("div", class_='bi_aqiarea_bottom')  # 空气质量描述

    # print(city.text + 'AQI指数：' + aqi.text + '\n空气质量：' + quality[0].text + result.text)
    # print('*' * 20 + ctime() + '*' * 20)
    result=city.text + 'AQI指数：' + aqi.text + '\n空气质量：' + quality[0].text + result.text
    return result

res=getpm('beijing') #此处输入城市名字
aqi=re.search('\d+',res)
if(int(aqi.group())>100):
    payload = {'text': '空气不好', 'desp': res}
    requests.get('http://sc.ftqq.com/SCU18154Tdda79a78a4b0ff6192e351192347b1545a3320ff21690.send', params=payload)
    fp = open('/home/ubuntu/weathertell/weathertell.log','a')
    fp.write(ctime())
    fp.write('发送空气预警\n')