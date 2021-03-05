import Image
from decimal import *
from zhongxinhua.page2.zxh_commad1 import PLACE_ORFER
# import tesserocr
import document as document
from base.base_page import BasePage
from base.box_driver import BoxDriver,BoxBrowser
import os
import re
from time import sleep
import requests
from bs4 import BeautifulSoup
# from lxml import etree
import csv
PATH = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")),'zxh_path')#中信华上传文件目录
original_name = 'daike_testtextt1'#上传文件的初始名字（以后上传将自动改名字：名字末尾由数字组成）

class Zxh_houtai(PLACE_ORFER):
    def daikexiadan_lv(self,dict,shangchaunpath,leixing='铝基板'):
        dr = self.incaidan('代客下单')
        dr.types('n,customerCode',dict['客编'])
        dr.wait_selenium('link,%s'%leixing).click()
        if leixing == '线路板':self.leixing = '玻纤板'
        else:self.leixing = leixing
        sleep(1)
        dr.wait_selenium('x,//*[@id="tr_%s"]//input[1]'%dict['代客单']).click()
        sleep(1)
        dr.switch_to_frame('id,submsg')
        self.valet_order_aluminum_substrate(shangchaunpath,original_name)


if __name__ == '__main__':
    kuaisu = ''#pcb入库快速开单（数量为‘1’时执行）
    data = {'user': 'jlsdev', 'pwd': 'jls123'}
    dict = {'客编': '0077M','代客单': '0','模具': '铣边','测试架': '飞针测试',
            '板长': '15','板宽': '12',
            '拼版1': '1',
            '拼版2': '1',
             '下单数量': '150'}

    b = Zxh_houtai(BoxDriver(BoxBrowser.Chrome))
    # 登陆后台
    b.login_zxh(data)
    # 代客下单
    b.daikexiadan_lv(dict,b.shangchaunpath)
    # # 审核订单
    b.shenghe(dict['客编'])
    # # 合同的生成,上传附件,代客确认
    hetong_text = b.hetonglc()
    # # 填写款到通知单
    b.kuandaofahuo(hetong_text)
    # # 下单通知单
    b.xiadantzd(hetong_text)
    # # 工程师审核
    production_number = b.gcs_sh()
    # # 主管审核
    b.zgsh()
    # PCB入库
    b.pcbruku(production_number)
    # 开单发货
    b.kaidaofahuo(diqu='深圳')
    #审核送货单
    b.shsonghuodan(hetong_text)
    # 备货
    b.beihuo(hetong_text, '10')
    # 确认发货
    b.qrfahuo(hetong_text)
    print('完成快单流程')