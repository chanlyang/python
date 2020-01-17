from time import time
from threading import Thread
import requests

#用于继承Thread类实现线程类
class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
    
    def run(self):
        #return super().run()
        file_name = self.url[self.url.rfind('/') + 1:] 
        resp = requests.get(self.url)
        with open('./'+file_name,'wb') as f:
            f.write(resp.content)
    
def main():
    #通过requests模块的get函数获取网络资源
    #使用天行数据的接口
    resp = requests.get('http://api.tianapi.com/meinv/?key=3b7496ab8016b8096aa4cef3700a6c45&num=10')
    #将网络返回的json数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        #通过多线程方式下载图片
        DownloadHanlder(url).start()

if __name__ == '__main__':
    main()