from selenium.webdriver.common.keys import Keys
from lxml import etree
from zhongxinhua.page2.zxh_commad import ZXH_COMMAD
from time import sleep
from decimal import *
import yaml
import csv
import os
from base.box_driver import BoxDriver,BoxBrowser
from zhongxinhua.page2.zxh_commad import ZXH_COMMAD
# import Image
import re

class ZXH_COMMAD_LIUCHENG(ZXH_COMMAD):
    with open('..//data/config.yml',mode='r',encoding='utf8') as f:
        config = yaml.load(f)
    PATH = eval(config['PATH'])
    shangchaunpath = PATH + '/上传文件'
    zuankong_path = PATH + '/MI钻孔模板.xls'
    xiadan_path = PATH + '/上传文件'
    wuliaonumber = config['wuliaonumber']
    # 共用变量
    handles =  config['handles']  # 用于关闭新开窗口参数
    leixing =  config['leixing']  # 下单的板子的类型
    jiaa = config['jiage']  #用于价格对象0
    versions = config['versions']#用于执行的新后台判断作用

    def login_zxh(self,data,handle=None):
        dr = self.base_driver
        dr.maximize_window()
        if self.versions != 'new':
            # url = '192.168.2.151:7022'
            dr.navigate("http://%s/loginAction!gotoLogin.action" % self.config['erp_url'])
            URL_SUESS = 'http://%s/homeAction.action' % self.config['erp_url']
            while dr.get_url() != URL_SUESS:
                dr.type('id,account_id', data['user'])
                dr.types('id,old_password_id', data['pwd'])
                try:
                    dr.accept_alert()
                except:
                    pass
                dr.get_url()
                sleep(1)
            sleep(1)
        elif self.versions == 'new':
            url_1 = 'https://%s/#/desktopAction.action' % self.config['new_erp_url']
            while url_1 not in dr.get_url():
                dr.navigate('https://%s/#/login' % self.config['new_erp_url'])
                dr.refresh()
                handel_1 = dr.window_handles()
                dr.type('x,//input[@placeholder="用户名"]', data['user'])
                dr.types('x,//input[@placeholder="密码"]', data['pwd'])
                sleep(3)
                handel_2 = dr.window_handles()
                for row in handel_2:
                    if row not in  handel_1:
                        dr.switch_to_window(row)
        if handle is None:
            dr.remove_window()
        else:
            dr.remove_window(handle)
        houtai_handle = dr.current_window_handle()
        return houtai_handle
    def kehu_login(self,kehu_user,kehu_pwd):
        dr = self.base_driver
        dr.maximize_window()
        dr.navigate('https://%s/home/login.html'% self.config['font_url'])
        dr.type('id,username',kehu_user)
        dr.clear_cookies()
        dr.types('id,password',kehu_pwd)
        a =dr.get_cookies()
        sleep(1)
    def kehu_fukuan(self):
        dr = self.base_driver
        dr.switch_to_window(self.handles)
        dr.click_by_text('— 订单确认')
        dr.switch_to_frame('id,client_context_frame')
        dr.click('s,input[value="确定"]')
        hh1 = dr.window_handles()
        dr.accept_alert()
        sleep(1)
        hh2 = dr.window_handles()
        for hh in hh2:
            if hh not in hh1:
                dr.switch_to_window(hh)
                dr.close_browser()
        dr.switch_to_window(self.handles)
        dr.switch_to_frame('id,client_context_frame')
        dr.click('s,input[value="确定"]')
        dr.click('id,paymentBtn')
        dr.click('s,input[value="立即支付"]')
    def hetonglc(self):
        # dr = self.incaidan('客户等级设置')
        # dr.types('n,customerCode','0001AW')
        # sleep(1)
        # dr.select_by_value('n,customerRateList','A')
        # dr.accept_alert()
        # dr.switch_to_default()
        # sleep(1)
        #
        dr = self.incaidan('由订单生成合同')
        if self.leixing == '玻纤板': self.leixing = '线路板'
        dr.select_by_visible_text('n,productCategory',self.leixing)#0铝基板;1玻钎板;2LED;3全部
        dr.wait_selenium('x,//input[@name="orderIdList"]').click()
        dr.click('s,input[value="生成合同"]')
        sleep(1)
        if dr.get_value('x,//*[@id="deliveryMode"]') == '':
            ye = dr.open_new_window('x,//*[@id="deliveryMode"]')
            dr.click('x,//*[@id="tr_1"]/td[3]/a')
            dr.switch_to_window(ye)
            if self.versions == 'new':
                dr.switch_to_frame('id,iframeEle')
            else:
                dr.switch_to_frame('n,fram_work')
        dr.click_wait('id,save_btn')
        dr.accept_alert()
        dr.dismiss_alert()
        dr.switch_to_default()
        #上传附件到合同
        self.incaidan('合同查询')
        self.hetong_text = dr.get_text('x,//tr[@id="tr_0"]/td[2]')
        print('合同号：'+self.hetong_text)
        dr.click_index('n,contractList',0)
        html = dr.open_new_window('s,input[value="上传合同回执"]')
        dr.switch_to_frame('id,submsg')
        sleep(0.5)
        dr.click_index('c,btn_href',0)
        dr._locate_element('id,uploadForm_fileUploadVO_uploadFile').send_keys(os.path.abspath(os.path.join(os.getcwd(), ".."))+r'/zxh_photo/全屏图.png')
        dr.click('id,sub_btn')#点击上传
        sleep(1)
        dr.close_browser()
        dr.switch_to_window(html)
        #代客确认合同
        self.incaidan('代客确认合同')
        dr.select_by_value('n,selectContract','2')#2客户已确认;3客户已取消
        sleep(0.5)
        dr.accept_alert()
        dr.switch_to_default()
        return self.hetong_text
    def kuandaofahuo(self,hetong_text):
        dr = self.incaidan('填写款到发货通知单')
        dr.types('n,contractCode',hetong_text)
        sleep(1)
        dr.click_index('n,contractList',0)
        dr.click('s,input[value="填写款到发货通知单"]')
        sleep(1)
        dr.type('id,advanceCashAmount','1')#输入到账金额
        dr.select_by_value('id,bankName','现金户')#银行账号
        dr.type('id,remark','1')#备注
        dr.click_index('c,btn_href',0)#点击保存
        dr.switch_to_default()
        #审核款到发货通知单
        self.incaidan('审核款到发货通知单')
        dr.types('n,contractCode',self.hetong_text)
        sleep(1)
        dr.click_index('link,审核',0)
        sleep(1)
        dr.click_index('c,btn_href',0)#点击通过审核
        dr.switch_to_default()
    def hetongcx(self):
        '''
        合同查询
        :return:
        '''
        dr = self.incaidan('合同查询')
        hetong_text = dr.get_text('x,//tr[@id="tr_0"]/td[2]')
        print('合同号：'+hetong_text)
        dr.switch_to_default()
        return hetong_text
    def shenghe(self,kehu_user):
        '''
        市场部审核流程
        :return:
        '''
        dr = self.incaidan('市场部审核客户订单')
        if self.leixing == '线路板': self.leixing = '玻纤板'
        dr.select_by_visible_text('x,//select[@id="productCategory"]',self.leixing)#选择类型
        page = dr.get_text('x,//*[@id="pageTable"]/tbody/tr[1]/td/span[2]').strip() #获取总页数
        if int(page) > 1:
            dr.click('x,//*[@id="pageTable"]/tbody/tr[1]/td/a[4]')          #点击尾页
        els = []
        for aa in range(21):
            try:kebian = dr.get_text('x,//tr[@id="tr_%s"]//td[3]' %str(aa))
            except:break
            if kehu_user.upper() in kebian:
                el = dr._locate_element('x,//tr[@id="tr_%s"]//td[1]/input[1]' %str(aa))
                els.append(el)
        els[-1].click()
        dr.wait_selenium('id,auditBtn').click()  # 点击审核
        hejijine = float(dr.reserved_string(dr.get_text('x,//td[contains(text(),"合") and contains(text(),"计")]/following-sibling::td'),'d'))
        if self.jiaa == hejijine:pass
        else:input('后台审核价格计算错误')
        dr.click_index('x,//*[@onclick="auditRecord(4,this.form)"]',0)#点击通过
        # 弹框确认
        try:dr.accept_alert()
        except:pass
    def xiadantzd(self,hetong_text,handle=None):
        '''
        下单通知单
        :return:
        '''
        dr = self.incaidan('生成下单通知单')
        dr.types('n,contractCode',hetong_text)
        dr.click('x,//tr[@id="tr_0"]//td[1]//input')
        sleep(1)
        dr.switch_to_frame('id,submsg')
        try:dr.click('x,//a[text()="新单"]')
        except:dr.click('x,//a[text()="返单"]');print('下返单')
        dr.switch_to_default()
        sleep(2)
        if self.versions == 'new':
            dr.switch_to_frame('id,iframeEle')
        else:
            dr.switch_to_frame('n,fram_work')
        self.xiadan_text = dr.get_attribute('n,orderNoticetbl.noticeCode', 'value');print('下单号：'+self.xiadan_text)
        self.banhao = dr.get_text('x,//td[contains(text(),"特殊板号")]').split('：')[-1]#获取版号
        self.biaomian = dr.get_text('x,//td[text()="表面处理"]/following-sibling::td[1]').strip()[0:2]#获取表面处理
        self.gongyi = dr.get_text('x,//td[text()="特殊工艺"]/following-sibling::td[1]').strip()#获取特殊工艺
        ck = dr.get_text('x,//td[text()="规格尺寸"]/following-sibling::td[1]')
        q = str(ck).split('/')[0].strip().split('*')
        self.banchang = str(Decimal(q[0])*10);self.bankuan = str(Decimal(q[1])*10)
        # 点击保存通知单
        dr.click('id,sub_btn')
        if handle is None:
            dr.remove_window()
        else:
            dr.remove_window(handle)
        dr.switch_to_default()
        return self.xiadan_text
    def gcs_zg_sh(self):
        '''
        工程师审核
        :param :
        :return:
        '''
        dr = self.incaidan('工程师审核')
        # 下单号查询
        dr.types('id,noticeCode',self.xiadan_text)
        self.xiadanleixing = dr.get_text('x,//*[@id="tr_0"]/td[3]').strip()
        dr.click('x,//img[@title="审核"]')
        Information_way = dr.get_text('x,//*[contains(@id,"productType") and @checked="checked"]/..').strip()
        production_number = dr.get_text('x,//td[text()="生产编号"]/following-sibling::td[1]').strip();print('内编：' + production_number)
        dr.click('c,btn_href')
        dr.switch_to_default()
        print('工程师审核:'+dr.wait_selenium('x,//*[@id="plugin_operate_result_wrap"]/table/tbody/tr[2]/td/font').text)
        #=========================== 主管审核=============================
        if self.xiadanleixing == '返单' and Information_way == '不需要工程处理':
            print('返单不需主管审核')
        else:
            dr = self.incaidan('主管审核')
            dr.types('id,noticeCode', self.xiadan_text)
            dr.click('x,//img[@title="审核"]')
            dr.click('c,btn_href')
            dr.switch_to_default()
            try:
                print('主管审核:' + dr.wait_selenium('x,//*[@id="plugin_operate_result_wrap"]/table/tbody/tr[2]/td/font').text)
            except:
                raise NameError('无主管审核的数据')
        return production_number
    def gcgl(self,dict,shangchaunpath,zuankong_path):
        '''
        工程管理
        :return:
        '''
        dr = self.incaidan('工程制作进度查询')
        dr.type('id,noticeCode', self.xiadan_text)
        dr.select_by_value('id,execStatus', '-1')
        #开始特殊制作
        if(1):
            dr.wait_selenium('x,//input[@name="idList"]').click()
            dr.click('id,updateExecNotice-11')
        #  获取订单信息
        mianji = float(dr.get_text('x,//*[@id="tr_0"]/td[11]'));print('订单面积:'+str(mianji))#总面积
        muju = dr.get_text('x,//*[@id="tr_0"]/td[39]').strip();print('模具:'+muju)#是否生成模具
        cesi = dr.get_text('x,//*[@id="tr_0"]/td[40]').strip();print('测试架:'+cesi)#是否生成测试架
        # xiadanleixing = dr.wait_selenium('x,//*[@id="tr_0"]/td[9]').text.strip()#获取下单类型如：新单，返单
        self.cengshu = dr.get_text('x,//*[@id="tr_0"]/td[17]').strip()#获取板子层数
        #  申请开模开测
        if (1):
            if muju == '待生成' or cesi == '待生成':
                dr.wait_selenium('x,//input[@name="idList"]').click()
                dr.click('x,//*[@id="addMoudleTest1"]')#申请开模开测
                if muju == '待生成':
                    dr.click('x,//*[@id="mould"]')#申请开模
                if cesi == '待生成':
                    dr.click('x,//*[@id="test"]')#申请开测
                for two in range(len(dr._locate_elements('x,//img[@title="点击上传文件"]'))):
                    if dr._locate_elements('x,//img[@title="点击上传文件"]')[two].is_displayed() == True:
                        op = dr.open_new_window('x,//img[@title="点击上传文件"]',two)
                        dr.switch_to_default()
                        dr.switch_to_frame('id,submsg')
                        dr.click('x,//*[@onclick="createAnnex()"]')
                        dr.wait_selenium('x,//*[@id="uploadForm_fileUploadVO_uploadFile"]').send_keys(dr.change_name(shangchaunpath))
                        dr.click('x,//*[@id="sub_btn"]')
                        dr.close_browser()
                        dr.switch_to_window(op)
                        if self.versions == 'new':
                            dr.switch_to_frame('id,iframeEle')
                        else:
                            dr.switch_to_frame('n,fram_work')
                dr.click('x,//*[@onclick="addMouldTestOrderRecord();" ]')#点击保存开模开测
                    #重置界面条件
                dr.type('id,noticeCode', self.xiadan_text)
                dr.select_by_value('id,execStatus', '-1')
        #开始制作完成
        if (1):
            dr.wait_selenium('x,//input[@name="idList"]').click()
            dr.click('id,makeComplete1')# 点击制作完成
            if self.xiadanleixing == '新单':
                dr.wait_selenium('id,mi_unit_length')
                dr.type('id,mi_unit_length',self.banchang)
                dr.type('id,mi_unit_width', self.bankuan)
                dr.type('id,mi_shipment_length', self.banchang)
                dr.type('id,mi_shipment_width', self.bankuan)
                dr.type('id,mi_lineWidth','1')
                dr.type('id,mi_lineDistance', '1')
                if self.cengshu in ['2','4']:
                    dr.type('id,gtl', '1')
                    dr.type('id,gbl', '1')
                dr.type('id,vcutSetTransverse','1')
                dr.type('id,vcutSetEndLong', '1')
                if self.cengshu == '4':
                    dr.type('x,//*[@id="inner_line_thred_width"]','1')
                    dr.type('x,//*[@id="inner_line_distance"]','1')
                    dr.click('x,//*[@id="writePressJoinMsg"]')#点击压合信息进入编辑页面
                    sleep(1)
                    dr.select_by_value('x,//*[@id="model"]','2116')
                bss=dr.open_new_window('s,input[value="上传拼板资料"]')
                pcb_text = dr.change_name(shangchaunpath)
                dr._locate_element('id,uploadForm_fileUploadVO_uploadFile').send_keys(pcb_text)
                # 点击上传
                dr.wait_selenium('id,sub_btn').click()
                dr.close_browser()
                dr.switch_to_window(bss)
                if self.versions == 'new':
                    dr.switch_to_frame('id,iframeEle')
                else:
                    dr.switch_to_frame('n,fram_work')
            dr.wait_selenium('s,input[value="保存"]').click()# 点击保存制作完成
            try:dr.accept_alert()
            except:pass
        # 制作MI
        if(1):
            if self.xiadanleixing == '新单':
                dr.wait_selenium('x,//input[@name="idList"]').click()
                dr.click('s,input[value="制作MI"]')#点击制作MI
                dr.wait_selenium('id,spellNumberA').send_keys('1')
                # try:
                sleep(1)
                dr.execute_script_element('x,//td[text()="注意事项"]')
                try:dr.click('x,//td[text()="二钻"]/following-sibling::td[4]/input')
                except:print('二钻选项没去除或无二钻')
                dr.click('x,//*[@id="div2"]/input[1]')#点击开料钻孔
                handless = dr.current_window_handle()
                dr.open_new_window('s,input[value="导入钻1"]')
                dr.wait_selenium('id,allProjectFrom_myFile').send_keys(zuankong_path)
                dr.click('x,//*[@id="allProjectFrom"]/table/tbody/tr/td/div/table/tbody/tr[3]/td/input[2]')#点击导入
                sleep(1)
                dr.close_browser()
                sleep(1)
                dr.switch_to_window(handless)
                if self.versions == 'new':
                    dr.switch_to_frame('id,iframeEle')
                else:
                    dr.switch_to_frame('n,fram_work')
                dr.wait_selenium('x,//*[contains(@value,"刷") and contains(@value,"新")]').click()#点击刷新
                while dr.get_displayed('id,numberXA') == False:
                    dr.click('x,//*[@id="div3"]/input[1]')
                dr.type('id,numberXA','1')
                dr.type('id,numberYA','1')
                dr.type('id,distanceXA','1')
                dr.type('id,distanceYA','1')
                dr.type('id,leaveBrimXA','1')
                dr.type('id,leaveBrimYA','1')
                dr.click('id,crossXA')
                dr.click('id,endlongYA')
                dr.type('id,setNumberA','1')
                dr.type('id,pcsNumberA','1')
                dr.type('id,pnlNumberA','1')
                dr.type('id,useRatioA','1')
                dr.click('id,sbtn')#开料
                dr.wait_selenium('id,noticeCode')
                dr.type('id,noticeCode',self.xiadan_text)
                sleep(1)
                dr.select_by_value('id,execStatus','-1')
        ##分配审核
        if(1):
            if mianji<float('3') and muju=='不允许' and cesi=='不允许' and self.banhao not in ('车载板,表贴板,电表板') and self.gongyi == '' and self.xiadanleixing != '返单':pass
            else:
                dr.wait_selenium('x,//input[@name="idList"]').click()
                dr.click('s,input[value="分配审核"]')# 分配审核
                sleep(1)
                dr.select_by_index('id,selectAuditMan','1')
                dr.accept_alert()
                dr.wait_selenium('x,//input[@name="idList"]').click()
                dr.click('id,makeupAuditNotice1')# 点击审核制作
                if self.xiadanleixing == '返单':
                    dr.wait_selenium('x,//*[@id="projectDataStatus0"]').click()#返单选择不需要替换
                try:
                    dr.wait_selenium('x,//span[@id="makeupAuditFinish"]/input[2]').click()
                    dr.accept_alert()
                except:pass
        # 拼版完成
        dr.wait_selenium('x,//input[@name="idList"]').click()
        dr.click('id,updateExecNotice1011')# 点击拼版完成
        # 工程下单
        dr.wait_selenium('x,//input[@name="idList"]').click()
        dr.click('id,updateExecNotice1001')# 点击工程下单
    def jicai(self):
        '''
        生成基材领料单
        :param xiadan_text:
        :return:
        '''
        dr = self.incaidan('生成基材领料单')
        dr.types('id,noticeCode',self.xiadan_text)
        dr.click('n,idList')
        dr.click('s,input[value="直接生成"]')
        dr.click('id,sbtn')
        sleep(1)
    def lingliaochuku(self,wuliaonumber):
        '''
        基材领料出库
        :param wuliaonumber:
        :return:
        '''
        dr = self.incaidan('基材领料出库')
        dr.types('id,noticeCode', self.xiadan_text)
        diqu = dr.wait_selenium('x,//*[@id="tr_0"]/td[9]').text.strip()#获取地区
        # dr.click('x,//*[@id="tr_0"]/td[12]/a/img')#大料出库
        dr.click('x,//a[contains(@onclick,"substratePickInit")]')#边料出库
        sleep(1)
        yeqian = dr.open_new_window('id,department')
        dr.click('x,//*[text()="江西三厂"]')
        dr.close_browser()
        dr.switch_to_window(yeqian)
        if self.versions == 'new':
            dr.switch_to_frame('id,iframeEle')
        else:
            dr.switch_to_frame('n,fram_work')
        dr.type('id,picker','领料人')
        # yeqianss = dr.open_new_window('s,img[title="选择板材"][name="materielSelectImg"]')
        # dr.wait_selenium('id,produceCode').send_keys(wuliaonumber[diqu] + Keys.ENTER)#选择物料
        # dr.wait_selenium('x,//*[@id="tr_0"]/td[2]').click()#选中板材
        # dr.wait_selenium('s,input[title="确定物料"]').click()
        # dr.switch_to_window(yeqianss)
        # dr.switch_to_frame('n,fram_work')
        # dr.click('n,ck_data')
        # sleep(1)
        # dr.type('id,aniseedNumbers','1')
        # yeqiansss = dr.current_window_handle()
        # dr.open_new_window('s,img[alt="选择采购记录中单价"]')
        # sleep(1)
        # dr.click('x,//*[@id="tr_0"]//td[8]/a')
        # dr.switch_to_window(yeqiansss)
        # dr.switch_to_frame('n,fram_work')
        dr.click('s,input[value="领料出库"]')
        # 多余操作
        try:
            dr.accept_alert()
            sleep(1)
            dr.dismiss_alert()
        except:pass
    def wip(self):
        '''
        wip
        :param xiadan_text:
        :return:
        '''
        dr = self.incaidan('启动WIP')
        dr.types('id,noticeCode',self.xiadan_text)
        sleep(2)
        factory=dr.get_text_list('s,td[align="left"]')[-1].strip()
        # dr.click('x,//*[@id="tr_0"]/lable[1]/td[14]/img[1]')
        dr.click('s,img[alt="启动/关闭wip流程，打印生产条码"]')
        sleep(1)
        saomiao = []
        for a in range(100):
            try:
                ll = dr.get_attribute('x,//tr[@id="tr_%s"]//td[1]/input[1]' %str(a),'barCode')
                # ll = dr.get_attribute('n,areaIdList', 'barCode')
                # dr.click('x,//tr[@id="tr_%s"]//td[1]/input[1]' %str(a))
                dr.click('x,//tr[@id="tr_%s"]//td[2]' % str(a))
                # dr.click('n,areaIdList')
                dr.click('s,input[value="启动WIP"]')
                sleep(1)
                saomiao.append(ll)
            except:
                break
        print('条码号：',saomiao)
        # dr.switch_to_default()
        # if self.versions == 'new':
        #     dr.click('x,//*[@aria-haspopup="list"]')
        #     dr.wait_selenium('x,//li[text()="退出" and @class="el-dropdown-menu__item"]').click()
        # else:
        #     dr.switch_to_frame('n,MM_FrameTop')
        #     dr.click('x,/html/body/table/tbody/tr/td/table/tbody/tr/td[5]/img')
        #     dr.accept_alert()
        return saomiao, factory
    def gysaomiao(self,saomiao,factory,handle=None):
        '''
        工程扫描
        :return:
        '''
        dr = self.base_driver
        csv_file = open("..\\data\\use.csv", mode='r', encoding='utf8')
        csv_reader = csv.reader(csv_file)
        lls = True
        for row in csv_reader:
            if lls == True:
                lls = False
                continue
            data = {'user': row[0], 'pwd': row[1], 'username': row[2]}
            if self.cengshu in ['1','2'] and data['username'].__contains__ ('内层压合'):
                continue
            elif self.biaomian[0:2] not in data['username'] and data['username'].__contains__('表面处理'):
                continue
            else:
                self.login_zxh(data, handle)
                if self.versions == 'new':
                    dr.types('x,//input[@placeholder="请输入搜索内容"]', 'WIP工艺扫描窗口')
                else:
                    dr.switch_to_frame('id,tree_frame')
                    dr.types('id,word', 'WIP工艺扫描窗口')
                if self.biaomian[0:2] in data['username']:
                    if self.versions == 'new':
                        dr.click('x,//li[contains(text(),"WIP工艺扫描窗口") and contains(text(),"%s")]' % self.biaomian)
                    else:
                        dr.click('x,//a[contains(text(),"WIP工艺扫描窗口") and contains(text(),"%s")]' % self.biaomian)
                else:
                    if self.versions == 'new':
                        dr.click('x,//li[contains(text(),"WIP工艺扫描窗口")]')
                    else:
                        dr.click('x,//a[text()="WIP工艺扫描窗口"]')
                sleep(1)
                if self.versions == 'new':
                    dr.switch_to_frame('id,iframeEle')
                else:
                    dr.switch_to_default()
                    if self.versions == 'new':
                        dr.switch_to_frame('id,iframeEle')
                    else:
                        dr.switch_to_frame('n,fram_work')
                for b in saomiao:
                    if data['user'] == 'jx13':  # 测试清点
                        dr.type('id,barCode', b)
                        dr.click('id,button2')
                        sleep(1)
                        text = dr.get_attribute('id,curCanConfirmNumber', 'value')
                        dr.type('id,confimNumber', text)
                        dr.click('id,button2')
                        sleep(1)
                    elif data['user'] == '15':  # 包装
                        dr.type('id,barCode', b)
                        dr.click('id,button2')
                        sleep(1)
                        text = dr.get_attribute('id,curCanConfirmNumber', 'value')
                        dr.type('id,confimNumber', text)
                        dr.select_by_value('id,areaId','1')
                        dr.select_by_visible_text('id,areaId', factory)
                        dr.click('id,button2')
                        sleep(1)
                    else:
                        dr.type('id,barCode', b)
                        sleep(0.5)
                        dr.click('id,button2')
                        sleep(0.5)
                        try:
                            dr.accept_alert()
                        except:
                            pass
                dr.switch_to_default()
                print(data['username'] + '：',dr.wait_selenium('x,//*[@id="plugin_operate_result_wrap"]/table/tbody/tr[2]/td/font').text)
                if self.versions == 'new':
                    dr.click('x,//*[@aria-haspopup="list"]')
                    dr.wait_selenium('x,//li[text()="退出" and @class="el-dropdown-menu__item"]').click()
                else:
                    dr.switch_to_frame('n,MM_FrameTop')
                    dr.click('x,/html/body/table/tbody/tr/td/table/tbody/tr/td[5]/img')
                    dr.accept_alert()
    def shbaozhaung(self):
        '''
        待审核包装记录
        :return:
        '''
        dr = self.incaidan('待审核包装记录')
        dr.types('n,queryOrderCode',self.xiadan_text)
        dr.click_wait('n,all')#全选中选项
        dr.click('s,input[value=" 审核 "]')
        dr.click_wait('''x,//input[@onclick="auditConfirmRecord('pass','0')"]''')#点击审核通过
        dr.accept_alert()
        print('审核包装完成')
    def kaidaofahuo(self,diqu):
        '''
        开单发货
        :param diqu: 选择地区
        :return:
        '''
        dr = self.incaidan('开单发货')
        dr.select_by_visible_text('n,queryFilterAreaId',diqu)
        dr.types('id,noticeCode',self.xiadan_text)
        dr.click_wait('n,contractProductId')
        dr.click('s,input[title="开单发货"]')
        sleep(1)
        dr.type('n,noticeCodeStr',self.xiadan_text)
        sleep(1)
        dr.click('x,//*[@id="cashForm"]/table/tbody/tr/td/div/table[1]/tbody/tr[2]/td[1]/input[4]')#点击查询
        dr.click_wait('n,detailsIds')
        dr.click('id,sub_btn')#点击保存发货
        print('开单发货完成')
    def beihuo(self,hetongtext,ses):
        '''
        仓库备货
        :param hetongtext:
        :param ses:
        :return:
        '''
        dr = self.incaidan('仓库备货')
        dr.types("name,contractCode",hetongtext)
        sleep(1)
        dr.wait_selenium('id,tr_1').click()
        dr.switch_to_frame('id,submsg')
        dr.type('x,//input[@id="productAmount"]',ses)
        dr.click_wait('id,submitButon')#点击备货确认
        print('仓库备货完成')
    def shsonghuodan(self,hetongtext):
        '''
        审核送货单
        :param hetongtext: 合同号
        :return:
        '''
        dr = self.incaidan('审核送货单')
        dr.types('id,contractCode',hetongtext)
        try:
            dr.wait_selenium('x,//a[text()="审核"]').click()
            dr.wait_selenium('''x,//input[@onclick="cashAudit('pass')"]''').click()
            print('审核送货单完成')
        except:
            print('未找到审核送货单')

    def qrfahuo(self,hetongtext):
        '''
        确认发货
        :param hetongtext:
        :return:
        '''
        dr = self.incaidan('确认发货')
        dr.types('id,contractCode',hetongtext)
        dr.wait_selenium('n,idList').click()
        dr.switch_to_frame('id,submsg')
        dr._locate_elements('s,input[value="确认发货"]')[-1].click()
        print('确认发货完成')
    def pcbruku(self,production_number):
        '''
        PCB入库
        :param production_number:生产编号
        :return:
        '''
        dr = self.incaidan('PCB入库')
        dr.click_wait('id,new_radio')
        dr.types('x,//*[@id="idForm"]/table/tbody/tr/td/div/table[2]/tbody/tr[2]/td[2]/span/input[3]',production_number)
        sleep(1)
        dr.select_by_index('id,noticeCode',1)
        sleep(1)
        a = dr.get_attribute('x,//*[@id="orderNumber_0"]','value')
        dr.type('n,inputNumber',a)
        dr.select_by_visible_text('i,areaId','深圳')
        dr.click('i,addMoeny')
    def fandan(self,production_number,leixing):
        '''
        返单
        :param production_number:
        :param leibie:
        :return:
        '''
        self.leixing = leixing
        dr = self.incaidan('复制订单')
        dr.select_by_visible_text('x,//*[@id="allProjectFrom_productCategory"]', leixing)
        dr.types('x,//*[@id="allProjectFrom_produceCode"]',production_number)
        dr.wait_selenium('x,//*[text()="复制"]').click()
        dr.wait_selenium('x,//*[@id="cal_total_btn"]').click()#点击计算费用
        dr.wait_selenium('x,//*[@id="sub_audit_btn"]').click()#点击提交审核
    def gongyipeizhi(self, name, bianma, cangfang, cengshu, biaomian, leixing, xianlu, cesi, erzuan):
        dr = self.incaidan('工艺流程类型设置')
        # a= dr._locate_elements('x,//*[@id="allProjectFrom_notAuthority"]/option')
        # for b in a:
        #     print(b.text)
        dr.click('x,//*[@onclick="initAdd()"]')  # 点击新增
        dr.type('x,//*[@id="techTypeName"]', name)
        dr.type('x,//*[@id="techTypeCode"]', bianma)
        dr.select_by_visible_text('x,//*[@id="areaId"]', cangfang)
        dr.select_by_visible_text('x,//*[@id="boardLayer"]', cengshu)  # 1,2,请选择
        dr.select_by_visible_text('x,//*[@id="surfaceCode"]', biaomian)  # 喷锡,沉金,OSP,请选择
        dr.select_by_visible_text('x,//*[@id="boardType"]', leixing)  # 玻纤板,铝基板,请选择
        dr.select_by_visible_text('x,//*[@id="circuit"]', xianlu)  # 曝光,丝印,全部,请选择
        dr.select_by_visible_text('x,//*[@id="testTypeCode"]', cesi)  # 飞针测试,其他,请选择
        dr.select_by_visible_text('x,//*[@id="needTwoDrill"]', erzuan)  # 有,无,请选择
        data = ['钻孔(锣有铜槽）', '导电胶', '外层线路', '图形转移（2铜）', '二钻', 'AOI扫描/蚀刻检查/中测', '防焊',
                '字符', '表面处理', '成型', 'E-T测试FQC', '包装']
        for a in data:
            if erzuan == '无' and a == '二钻':
                continue
            dr.select_by_visible_text('x,//*[@id="allProjectFrom_alreadyAuthority"]', a)
            dr.click('x,//*[@id="allProjectFrom"]/table[2]/tbody/tr/td[2]/input[1]')
        dr.click('x,//*[@onclick="save()"]')  # 保存


class PLACE_ORFER(ZXH_COMMAD_LIUCHENG):
    '''
    代客下单中需要的方法
    '''
    def place_order_Upload_file_to_submit(self,shangchaunpath,original_name):
        '''
        代客下单上传文件到提交审核的流程
        :param shangchaunpath:
        :param original_name:
        :return:
        '''
        dr = self.base_driver
        html = dr.open_new_window('s,img[title="点击上传文件"]')
        txt = dr.change_name(shangchaunpath)
        dr.wait_selenium('id,uploadForm_fileUploadVO_uploadFile').send_keys(txt)
        dr.click_index('c,btn_href',0)#上传文件保存
        sleep(1)
        dr.close_browser()
        dr.switch_to_window(html)
        if self.versions == 'new':
            dr.switch_to_frame('id,iframeEle')
        else:
            dr.switch_to_frame('n,fram_work')
        dr.switch_to_frame('id,submsg')
        dr.click('s,input[value="计算费用"]')
        self.jiaa = float(dr.get_attribute('x,//*[@id="total"]', 'data-value'))
        dr.click('s,input[value="提交审核 "]')
    def valet_order_fiberglass_sheet(self,dict,shangchaunpath,original_name):
        '''
        下玻纤板订单
        :param dict: 订单参数
        :param shangchaunpath: 上传文件路径
        :param original_name: 初始上传文件
        :return:
        '''
        dr = self.base_driver
        dr.select_by_value('id,mold',dict['模具'])
        dr.select_by_value('id,testType',dict['测试架'])
        dr.type('id,detailsLength',dict['板长'])
        dr.type('id,detailsWidth',dict['板宽'])
        dr.type('id,makeupLen',dict['拼版1'])
        dr.type('id,makeupWid',dict['拼版2'])
        dr.type('id,orderNumber',dict['下单数量'])
        self.place_order_Upload_file_to_submit(shangchaunpath,original_name)
    def valet_order_aluminum_substrate(self,shangchaunpath,original_name):
        '''
        下铝基板订单
        :param shangchaunpath:
        :param original_name:
        :return:
        '''
        dr = self.base_driver
        dr.select_by_visible_text('id,solderColor','绿')
        dr.select_by_value('x,//select[@id="mold"]','铣边')
        dr.select_by_value('x,//select[@id="testType"]','飞针测试')
        dr.type('x,//*[@id="boardLength"]','10')#长
        dr.type('x,//*[@id="boardWidth"]','15')#宽
        dr.type('x,//*[@id="makeupLen"]','1')
        dr.type('x,//*[@id="makeupWid"]','1')
        dr.type('x,//*[@id="orderNumber"]','100')
        self.place_order_Upload_file_to_submit(shangchaunpath,original_name)
    def valet_order_led(self,internal_number,quantity_ordered):
        '''
        led
        :param internal_number:
        :param quantity_ordered:
        :return:
        '''
        dr = self.base_driver
        dr.wait_selenium('x,//*[@id="innerCode"]').send_keys(internal_number)
        dr.click('x,//input[@onclick="searchOrder()" and @class="btn_href"]')#点击查询
        dr.wait_selenium('x,//input[@name="productList"]').click()
        dr.wait_selenium('x,//*[@id="orderNumber"]').send_keys(quantity_ordered)
        dr.click('x,//*[@id="deliveryTime"]')
        dr.switch_to_frame('id,__calendarIframe');dr.wait_selenium('x,//*[@id="selectTodayButton"]').click();dr.switch_to_parent_frame()
        dr.click('x,//*[@id="sub_audit_btn"]')#提交审核
        sleep(1)
        dr.accept_alert()
    def general_manager_review_order(self,leixing='LED套件'):
        '''
        总经理审核订单
        :param leixing: 订单的类型
        :return:
        '''
        dr = self.incaidan('总经理审核订单')
        dr.select_by_visible_text('id,productCategory',leixing)
        dr.wait_selenium('x,//a[text()="审核"]').click()
        dr.wait_selenium('id,sub_btn_access').click()
    def led_inventory(self,dict):
        '''
        LED库存盘点
        :return:
        '''
        dr = self.incaidan('LED库存盘点')
        dr.types('x,//*[@id="produceCode"]',dict['生产编号'])
        dr.wait_selenium('n,hidedepotId').click()
        yemian = dr.open_new_window('s,input[value="调整库存"]')
        dr.type('id,changgeDepotNumber',dict['库存调整'])
        dr.click('x,//*[@id="addMoeny"]')
        dr.switch_to_window(yemian)
    def kaidaofahuo_led(self,hetong_text):
        '''
        led开单发货
        :param hetong_text:
        :return:
        '''
        dr = self.incaidan('开单发货')
        dr.select_by_visible_text('x,//*[@id="isLedProduct"]','LED套件')
        dr.select_by_visible_text('n,queryFilterAreaId','深圳')
        dr.types('x,//*[@id="contractCode"]',hetong_text)
        dr.wait_selenium('n,contractProductId').click()
        dr.click('s,input[title="开单发货"]')
        sleep(1)
        dr.type('x,//*[@id="contractCode"]',hetong_text)
        sleep(1)
        dr.wait_selenium('x,//*[@id="cashForm"]/table/tbody/tr/td/div/table[1]/tbody/tr[2]/td[1]/input[4]').click()#点击查询
        sleep(1)
        shuliang=BoxDriver.reserved_string(dr.get_text('x,//*[@id="tr_1"]/td[13]'),'d')
        dr.type('x,//input[@name="billNumber"]',shuliang)
        dr.wait_selenium('n,detailsIds').click()
        dr.click('id,sub_btn')#点击保存发货



