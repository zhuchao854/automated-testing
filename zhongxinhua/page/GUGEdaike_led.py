# import Image
from decimal import *
from zhongxinhua.page2.zxh_commad1 import PLACE_ORFER
# import tesserocr
# import document as document
from base.base_page import BasePage
from base.box_driver import BoxDriver,BoxBrowser
import os
import re
from time import sleep
import requests
# from lxml import etree
import csv
original_name = 'daike_testtextt1'#上传文件的初始名字（以后上传将自动改名字：名字末尾由数字组成）

class Zxh_houtai_LED(PLACE_ORFER):
    def daikexiadan_led(self,dict,leixing='LED'):
        dr = self.incaidan('代客下单')
        dr.types('n,customerCode',dict['客编'])
        dr.wait_selenium('link,LED').click()
        if leixing == '线路板':self.leixing = '玻纤板'
        elif leixing == 'LED':self.leixing = 'LED套件'
        else:self.leixing = leixing
        self.valet_order_led(dict['生产编号'], dict['下单数量'])


if __name__ == '__main__':
    data = {'user': 'jlsdev', 'pwd': 'jls123'}
    dict = {'客编': '0001y','代客单': '0',
            '生产编号':'2SH2636A',
            '下单数量': '1000',
            '库存调整':'10000'}

    b = Zxh_houtai_LED(BoxDriver(BoxBrowser.Chrome))
    # 登陆后台
    b.login_zxh(data)
    # 代客下单
    b.daikexiadan_led(dict)
    # 总经理审核订单
    b.general_manager_review_order()
    # 合同的生成,上传附件,代客确认
    hetong_text = b.hetonglc()
    # 填写款到通知单
    b.kuandaofahuo(hetong_text)
    #调整led库存
    b.led_inventory(dict)
    # 开单发货
    b.kaidaofahuo_led(hetong_text)
    #审核送货单
    b.shsonghuodan(hetong_text)
    # 备货
    b.beihuo(hetong_text, '10')
    # 确认发货
    b.qrfahuo(hetong_text)
    print('完成流程')