from selenium.webdriver.common.by import By
# from jlc.src.common.ConfigHandler import ConfigHandler
# from jlc.src.common.RequestsHandler import RequestsHandler
# import pytest
import requests
# import allure
import time
from zhongxinhua.page2.HtmlHandler import HtmlHandler
from lxml import etree
import csv
import yaml
import os

# from selenium import webdriver
# profile = webdriver.ChromeOptions()
# prefs = {'profile.default_content_settings.popups': 0}
# profile.add_experimental_option('prefs', prefs)
# extension_path1 = r'E:\automated-testing\plugin' + '\谷歌插件_2_0_4.crx'
# profile.add_extension(extension_path1)
# a = webdriver.Chrome(chrome_options=profile)
# a.get('http://test.zxhgroup.com:8080/loginAction!gotoLogin.action')
# token = a.find_element_by_xpath('/html/body/form/input[2]').get_attribute('value')

# testdata = {'url': 'https://test.zxhgroup.com/home/customerLogin.html',
#             'method': 'post',
#             'body': {'loginType': 'code', 'username': '18889K', 'password': 'DC483E80A7A0BD9EF71D8CF973673924', 'phoneNumber': '12345678911', 'loginValidateCode': ''},
#             'type': 'data',
#             'headers': None,
#             'params': None}
# s = requests.session()
# res = RequestsHandler(session=s, testdata=testdata).send_requests()
# print(res['statuscode'])
# print(res['text'])
# def datatest(url,method='get',body=None):
#     testdata = dict()
#     testdata['url'] = url
#     testdata['method'] = method
#     testdata['body'] = body
#     testdata['type'] = 'data'
#     testdata['headers'] = None
#     testdata['params'] = None
#     return testdata
config_path = os.path.join(os.path.join(os.path.abspath('..'),'data'),'config.yml')

class api_sac:
    with open(config_path,mode='r',encoding='utf8') as f:
        config = yaml.load(f)
    def requestedd(self,session,data):
        res = {}
        r = session.request(method=data['method'],
                           url=data['url'],
                           params=data['params'],
                           headers=data['headers'],
                           data=data['body'],
                           verify=False)
        res['statuscode'] = str(r.status_code)
        res['text'] = r.content.decode('utf-8')
        res['time'] = str(r.elapsed.total_seconds())
        return res
    def aaa(self,tzdlist):
        list = []
        with open('..//data/useapi.csv', mode='r', encoding='utf8') as f:
            casedata = csv.reader(f)
            num = True
            for row in casedata:
                if num == True:
                    num = False
                    continue
                list.append(row)

        url_host = self.config['erp_url']

        for user,userid,pwd,username in list:
            newsession = requests.session()
            data = {'url':'http://%s/loginAction!toLogin.action'%url_host,
                        'method': 'get',
                        'body':None,
                        'type': 'data',
                        'headers': None,
                        'params': None}
            rrr= self.requestedd(newsession,data)
            # r = RequestsHandler(session=s, testdata=data).send_requests()
            q = HtmlHandler(rrr['text'])
            token_xpath = '/html/body/form/input[2]'
            randomChallenge_xpath = '//*[@id="randomChallenge"]'
            token = q.getElementAttr(token_xpath,'value')
            randomChallenge = q.getElementAttr(randomChallenge_xpath,'value')

            body = {
                    'struts.token.name':	'token',
                    'token':	token,
                    'cpuId'	:'',
                    'password'	:'c71dd40e8d1a0021ede76a9ee263d381',
                    'macAddress'	:'',
                    'testType'	:'copy',
                    'loginType'	:'normalLogin',
                    'IsTestSystem'	:'yes',
                    'randomChallenge'	:randomChallenge,
                    'oldPassword'	:pwd,
                    'j_code'	:'',
                    'smsNumberCheckCode':	'',
                    }
            body['account'] = user
            testdata = {'url': 'http://%s/loginAction.action'%url_host,
                        'method': 'post',
                        'body':body,
                        'type': 'data',
                        'headers': None,
                        'params': None}
            res1 = self.requestedd(newsession,testdata)
            # res = RequestsHandler(session=s, testdata=testdata).send_requests()
            if res1['text'].__contains__('财务'):
                print('-----------------------成功登陆后台--------------------------')
            else:print('-----------------------登陆后台失败--------------------------')

            body2 = dict()
            body2['basicTechId'] = userid
            for tzd in tzdlist:
                body2['barCode'] = tzd
                body3 = dict()
                if user == 'jx13' or user == '15':
                    data2 = {
                        'url': 'http://%s/technicsprocess/produceWipAction!queryCurCheckNumberInfo.action'%url_host,
                        'method': 'post',
                        'body': body2,
                        'type': 'data',
                        'headers': None,
                        'params': None}
                    rrr12 = self.requestedd(newsession,data2)
                    if user == 'jx13':
                        feedNumber = eval(rrr12['text'])['feedNumber']
                        testerConfirmNum = eval(rrr12['text'])['testerConfirmNum']
                        body3['confimNumber']  = str(feedNumber-testerConfirmNum)
                        body3['lackReason'] = ''
                    elif user == '15':
                        feedNumber = eval(rrr12['text'])['feedNumber']
                        packerConfirmNum = eval(rrr12['text'])['packerConfirmNum']
                        body3['confimNumber'] = str(feedNumber - packerConfirmNum)
                        body3['lackReason'] = ''
                        body3['area'] = '深圳'
                        body3['areaId'] = '1'
                        body3['addStoreType'] = 'fix'#板子类型
                body4 = {**body2,**body3}
                data3 = {'url':'http://%s/technicsprocess/produceWipAction!wipscan.action'%url_host,
                            'method': 'post',
                            'body':body4,
                            'type': 'data',
                            'headers': None,
                            'params': None}
                rrr2 = self.requestedd(newsession,data3)
                # res2 =RequestsHandler(session=s,testdata=data2).send_requests()
                html = HtmlHandler(rrr2['text'])
                text = html.getElementText('//*[@id="plugin_operate_result_wrap"]/table//font')
                print('用户:'+user+' , '+'用户名:'+username+' , '+'生产条码号:'+tzd+' , '+'扫描结果:'+text.strip())
            print('*******************************************************************************************************')
            newsession.close()
    def login_api_front(self,session):
        body = dict()
        body['loginType'] = 'code'
        body['username'] = '18889K'
        body['password'] = 'DC483E80A7A0BD9EF71D8CF973673924'
        data = dict()
        data['url'] = 'http://test.zxhgroup.com/home/customerLogin.html'
        data['method'] = 'post'
        data['body'] = body
        data['type'] = 'data'
        data['headers'] = None
        data['params'] = None
        r= self.requestedd(session,data)
        if r['text'].__contains__('欢迎您'):
            print('------------登录客户前台成功------------')
        else:print('------------登录客户前台失败------------')
        return session
    def testdata(self,url,method='post',body=None):
        data = dict()
        data['url'] = url
        data['method'] = method
        data['body'] = body
        data['type'] = 'data'
        data['headers'] = None
        data['params'] = None
        return data
    def online(self,session):
        body = {'type': '', 'oldMold': '', 'oldMouldingType': '', 'orderDetailsId': '401CD9AE6F844D96',
                'testArea': '10', 'oldTestType': '', 'peculiarPlankMark': '', 'makeupStyleCount': '', 'isCopy': '',
                'shippingTypeCode': '', 'makeupDataSource': '1', 'makeupLen': '1', 'makeupWin': '1',
                'makeupNumber': '1', 'processEdgeWidth': '', 'processEdgeWidthSelect': '',
                'makeupSpaceWidth': '', 'makeupSpaceWidthSelect': '', 'detailsLength': '4',
                'detailsWidth': '2', 'orderNumber': '5', 'detailsLayer':'2', 'plate': 'FR-4',
                'thinkness': '1.6', 'surfaceCode': 'No_Tin', 'minLine': '1001', 'seulHole': '',
                'copperThickness': '1.0', 'solderColor': '绿色',
                'characterColor': '白色', 'characterType': '',
                'throughHoleProcess': '盖油', 'testType': '目测',
                'electrTestType': '', 'testPriceType': '', 'oldPcb': '', 'mold': '铣边',
                'mouldingType': '1000', 'moldOldPcb': '', 'moldTestTypeCode': '', 'charMark': '',
                'invoice': '0', 'printPeriod': '0', 'specialProcess': '', 'shipmentReport': '',
                'impedance': 'no', 'BGA': 'no', 'orderUrgent': 'no'}
        url='http://test.zxhgroup.com/customerOrder/preOrder.action'
        data=self.testdata(url,body=body)
        r = self.requestedd(session,data)
        print(r['text'])


if __name__ == '__main__':
    session1 = requests.session()
    session = api_sac().login_api_front(session1)
    api_sac().online(session)

