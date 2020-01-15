import json
import requests
"""
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""

def main():
    my_dict = {
        'name':'chenliang',
        'age':'45',
        'wechat':'j0uliang',
        'firends':['junbao','yankui'],
        'home':[
            {'hometown':'jiuquan','mile':'1020km'},
            {'school':'daqing','mile':'539km'},
            {'work':'beijing','mile':'6km'}
        ]
    }
    try:
        with open('chenliang.json', 'w', encoding= 'utf-8') as fs:
            json.dump(my_dict,fs)
    except Exception as e:
        print("错误是" + e)
    print("ending")
#查ip
def main():
    url = 'http://api.avatardata.cn/IpLookUp/LookUp?key=35c539e4fd3548998e5f6a35de412eae&ip=123.150.174.180'
    ref = requests.get(url)
    date_model = json.loads(ref.text)
    print(date_model)
#国内新闻
def main():
    resp = requests.get('http://api.avatardata.cn/GuoNeiNews/Query?key=c8f7884dc943439ba2493e4c1143419b&page=1&rows=10')
    data_model = json.loads(resp.text)
    for news in data_model['result']:
        print(news['title'])

if __name__ == '__main__':
    main()