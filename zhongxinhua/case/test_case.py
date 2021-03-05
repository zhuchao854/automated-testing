import unittest
import parameterized
import time
import csv
from ddt import data,ddt
from base.box_driver import BoxDriver,BoxBrowser
from zhongxinhua.page_case.zxh_case import zxh_test
from zhongxinhua.page2.zxh_commad import ZXH_COMMAD
import os
import shutil



@ddt
class Tap_Menu_Test(unittest.TestCase):
    '''测试报告'''
    case_config_copy = ZXH_COMMAD.csv_list('..\\data\\casedata\\CaseDataCopy.csv')#后台复制订单-用例场景数据集
    case_config_backstage_bo = ZXH_COMMAD.csv_dict("..\\data\\casedata\\CaseDataBackstageBo.csv")#后台下单玻纤板-用例场景数据集
    case_config_online_kf = ZXH_COMMAD.csv_dict("..\\data\\casedata\\CaseDataOnlineKf.csv")#客户在线下单-用例场景数据集
    case_config_backstage_lv = ZXH_COMMAD.csv_dict("..\\data\\casedata\\CaseDataBackstageLv.csv")#后台下单铝基板-用例场景数据集
    case_config_led = ZXH_COMMAD.csv_dict("..\\data\\casedata\\CaseDataLed.csv")  # 后台下单LED-用例场景数据集

    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    screenshot_path = os.path.join(path, 'screenshot')
    shutil.rmtree(screenshot_path)#强制删除
    os.makedirs(screenshot_path)


    def setUp(self):
        '''
        实例化类，打开浏览器
        :return:
        '''
        print('开始')
        self.drive = zxh_test(BoxDriver(BoxBrowser.Chrome))
        self.drive.base_driver.implicitly_wait(1)
    def tearDown(self):
        '''
        关闭浏览器
        :return:
        '''
        try:self.drive.base_driver.save_window_snapshot("..//screenshot/%s%s.png"% (self.name,time.strftime('%Y-%m-%d %H_%M_%S',time.localtime())))
        except:
            self.drive.base_driver.accept_alert()
            self.drive.base_driver.save_window_snapshot("..//screenshot/%s,%s.png"% (self.name,time.strftime('%Y-%m-%d %H_%M_%S',time.localtime())))
        self.drive.base_driver.quit()
        print(self.cofig)
        print('结束')

    def test0_buliao(self):
        '''补料流程'''
        self.name = '补料流程'
        data = {'user': 'jlsdev', 'pwd': 'jls123'}
        self.drive.buliao(data)
        self.cofig = ''

    @data(*case_config_backstage_bo)
    def test1_bo(self,case_config_backstage_bo):
        '''代客下单-玻纤板'''
        # self.name = sys._getframe().f_code.co_name
        self.name = '代客下单-玻纤板'
        self.cofig = case_config_backstage_bo
        self.drive.backstage_bo(dict=case_config_backstage_bo)
        globals()['a'] = [['123','uiu'],['1234','uiu']]


    @data(*case_config_led)
    def test2_led(self,case_config_led):
        '''代客下单-LED'''
        # self.name = sys._getframe().f_code.co_name
        self.name = '代客下单-LED'
        self.cofig = case_config_led
        data = dict = case_config_led
        self.drive.backstage_led(data,dict)


    @data(*case_config_backstage_lv)
    def test3_lv(self,case_config_backstage_lv):
        '''代客下单-铝基板'''
        # self.name = sys._getframe().f_code.co_name
        self.name = '代客下单-铝基板'
        self.cofig = case_config_backstage_lv
        data = dict = case_config_backstage_lv
        self.drive.backstage_lv(data,dict)


    @data(*case_config_online_kf)
    def test4_online_kf(self,case_config_online_kf):
        '''客户在线下单'''
        # self.name = sys._getframe().f_code.co_name
        self.name = '客户在线下单'
        self.cofig = case_config_online_kf
        dict = data = case_config_online_kf
        kehu_user = case_config_online_kf['kehu_user'];kehu_pwd = case_config_online_kf['kehu_pwd']
        self.drive.online_kf(kehu_user,kehu_pwd,data,dict)

    @data(*case_config_copy)
    def test5_copy(self,case_config_copy):
        '''代客下单-复制'''
        # self.name = sys._getframe().f_code.co_name
        self.name = '代客下单-复制'
        self.cofig = case_config_copy
        data = {'user': 'jlsdev', 'pwd': 'jls123'}
        self.drive.backstage_copy(data,case_config_copy)

