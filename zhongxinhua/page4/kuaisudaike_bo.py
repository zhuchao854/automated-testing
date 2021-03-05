# import Image
from decimal import *
from zhongxinhua.page2.zxh_commad1 import ZXH_COMMAD_LIUCHENG
# import tesserocr
# import document as document
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

class Zxh_houtai(ZXH_COMMAD_LIUCHENG):

    def daikexiadan(self,dict,shangchaunpath,leixing='线路板'):
        dr = self.incaidan('代客下单')
        dr.types('n,customerCode', dict['客编'])
        dr.click('link,%s' % leixing)
        if leixing == '线路板':self.leixing = '玻纤板'
        else:self.leixing = leixing
        sleep(2)
        dr.click('x,//*[@id="tr_%s"]//input[1]' %dict['代客单'])
        dr.switch_to_frame('id,submsg')
        dr.select_by_value('id,mold',dict['模具'])
        dr.select_by_value('id,testType',dict['测试架'])
        dr.type('id,detailsLength',dict['板长'])
        dr.type('id,detailsWidth',dict['板宽'])
        dr.type('id,makeupLen',dict['拼版1'])
        dr.type('id,makeupWid',dict['拼版2'])
        dr.type('id,orderNumber',dict['下单数量'])
        html = dr.open_new_window('s,img[title="点击上传文件"]')
        txt = dr.change_name(shangchaunpath)
        dr.wait_selenium('id,uploadForm_fileUploadVO_uploadFile').send_keys(txt)
        dr.click_index('c,btn_href',0)#上传文件保存
        dr.close_browser()
        dr.switch_to_window(html)
        if self.versions == 'new':
            dr.switch_to_frame('id,iframeEle')
        else:
            dr.switch_to_frame('n,fram_work')
        dr.switch_to_frame('id,submsg')
        dr.click('s,input[value="计算费用"]')
        self.jiaa = float(dr.get_attribute('x,//*[@id="total"]','data-value'))
        dr.click('s,input[value="提交审核 "]')
        dr.switch_to_default()

if __name__ == '__main__':
    kuaisu = ''#pcb入库快速开单（数量为‘1’时执行）
    data = {'user': 'jlsdev', 'pwd': 'jls123'}
    dict = {'客编': '0077M','代客单': '5','模具': '铣边','测试架': '飞针测试',
            '板长': '15','板宽': '25',
            '拼版1': '1',
            '拼版2': '1',
             '下单数量': '300'}

    b = Zxh_houtai(BoxDriver(BoxBrowser.Chrome))
    # 登陆后台
    b.login_zxh(data)
    # 代客下单
    b.daikexiadan(dict,b.shangchaunpath)
    # # 审核订单
    b.shenghe(dict['客编'])
    # # 合同的生成,上传附件,代客确认
    hetong_text = b.hetonglc()
    # # 填写款到通知单
    b.kuandaofahuo(hetong_text)
    # # 下单通知单
    b.xiadantzd(hetong_text)
    # # 工程师审核
    production_number = b.gcs_zg_sh()
    # # 主管审核
    b.incaidan('通知单进度查询')
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