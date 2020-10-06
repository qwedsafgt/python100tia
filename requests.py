from time import time
from threading import Thread

import requests#该requests模块允许您使用Python发送HTTP请求


# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()#继承自父类，覆盖初始化化def init，并继承初始化属性
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]#Python字符串方法rfind（）返回找到子字符串str的最后一个索引；如果不存在这样的索引，则返回-1
        resp = requests.get(self.url)#尝试获取一个网页
        with open('/Users/Hao/' + filename, 'wb') as f:
            f.write(resp.content)#resp.content返回的是bytes型也就是二进制的数据,读取图片，文件


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=APIKey&num=10')#获取天行网页
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()
