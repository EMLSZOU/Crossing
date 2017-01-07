# -*- coding: utf-8 -*-
######### json，天气查询

'''
#### demo1，百度首页内容抓取
import urllib.request
get = urllib.request.urlopen('http://www.baidu.com')
webresponse = get.read()
htmlcontent = webresponse.decode('utf-8')
print(htmlcontent)
f = open('baidu.html', 'w+', encoding='utf-8')
f.write('%s'% htmlcontent)
f.close()
'''

###########  json，天气查询
import urllib.request
import json
cityname = input('你想要查询哪个城市的天气？请输入一个简体中文城市名\n')
## 打开json文件，读取json对象，转为字典，然后查询字典 ########
file = open('city.json', 'r+', encoding='utf-8')  # print('file:%r'% file)
codedic = json.load(file)  # print('cityjson:%r'% codedic)
try:
    citycode = codedic[cityname]  # print('citycode:%r'% citycode)
except:
    print('没有该城市的天气信息')
try:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    print(url)
    response = urllib.request.urlopen(url).read()  # 此时得到的是byte object而不是String
    weatherjson = response.decode('utf-8')  # 从byte解码到String对象(也就是json信息)
    data = json.loads(weatherjson)  # json对象转成字典对象
    result = data['weatherinfo']  # 查询字典，得到的结果再次存成字典
    str_temp = ('%s\n%s ~ %s') % (  # 查询字典，并且格式化成字符串
        result['weather'],
        result['temp1'],
        result['temp2']
    )
    print(str_temp)
except:
    print('有该城市的天气信息，但查询失败')