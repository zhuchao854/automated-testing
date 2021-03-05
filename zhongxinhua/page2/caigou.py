from zhongxinhua.page2.zxh_commad1 import ZXH_COMMAD_LIUCHENG
from base.box_driver import BoxDriver,BoxBrowser

# class CAIGOU(ZXH_COMMAD_LIUCHENG):
#     pass
import yaml
with open('..//use.yml',mode='r',encoding='UTF-8') as f:
    y = yaml.load(f)
print(y)
# import requests
# from bs4 import BeautifulSoup
# url = 'http://test.zxhgroup.com:8080/homeAction.action'
# #
# # # headers = {
# # #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
# res = requests.post(url,data=data) #get方法中加入请求头
# print(res.text)
# #查看下当前requests请求url抓去的数据编码,这里获取的是ISO-8859-1
# print (requests.get(url).encoding)
# #翻阅下要爬去的网站的编码是什么，这里看了下是utf-8，编码不一样会乱码，将requests获取的数据编码改为和目标网站相同，改为utf-8
# res.encoding = 'utf-8'
# soup = BeautifulSoup(res.text, 'html.parser') #对返回的结果进行解析
# print(soup)
# # print (soup.select('body > section > div.wrapbox > div:nth-child(1) > div > ul > li:nth-child(6)'))
# # nth-child 在python中运行会报错，需改为 nth-of-type
# # print (soup.select('body > section > div.wrapbox > div:nth-of-type(1) > div > ul > li:nth-of-type(6)'))
# textlist = soup.select('body > section > div.wrapbox > div > div > ul > li > a')
# for t in textlist:
#     print (t) #获取单条html信息
#     # print (t.get_text()) #获取中间文字信息