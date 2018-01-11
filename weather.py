import requests
from bs4 import BeautifulSoup
from time import ctime
def getpm(city):
    url='http://www.pm25.com/'+city+'.html'
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    city = soup.find(class_='bi_loaction_city')  # 城市名称
    aqi = soup.find("a", {"class", "bi_aqiarea_num"})  # AQI指数
    quality = soup.select(".bi_aqiarea_right span")  # 空气质量等级
    result = soup.find("div", class_='bi_aqiarea_bottom')  # 空气质量描述

    print(city.text + u'AQI指数：' + aqi.text + u'\n空气质量：' + quality[0].text + result.text)
    print('*' * 20 + ctime() + '*' * 20)
    result=city.text + u'AQI指数：' + aqi.text + u'\n空气质量：' + quality[0].text + result.text
    return result
# getpm('shanghai')
# getpm('beijing')
getpm('baoding') #此处输入城市名字