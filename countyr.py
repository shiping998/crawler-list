#图形化分析movie250.py爬取下来的国家地区信息
import pymongo
from string import punctuation
import charts

client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
movie = walden['movie']

area_list = []
for i in movie.find():
    area_list.append(i['content'])
area_index = list(set(area_list))
print(area_index)

post_times = []
for index in area_index:
    post_times.append(area_list.count(index))
print(post_times)


def data_gen(types):
    length = 0
    if length <= len(area_index):
        for area,times in zip(area_index,post_times):
            data = {
                'name':area,
                'data':[times],
                'type':types
            }
            yield data
            length += 1
			
data_gen('column')

for i in data_gen('column'):
    print(i)
	

series = [data for data in data_gen('column')]
charts.plot(series, show='inline', options=dict(title=dict(text='豆瓣电影top250出产国家和地区分析')))