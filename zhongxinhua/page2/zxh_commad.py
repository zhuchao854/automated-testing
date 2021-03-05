from base.base_page import BasePage
from time import sleep
# import Image
import csv
import re
import yaml
class ZXH_COMMAD(BasePage):
    with open('..//data/config.yml',mode='r',encoding='utf8') as f:
        config = yaml.load(f)
    versions = config['versions']
    def yanzheng_login(self,data):
        '''
        验证码登陆后台
        :param data:
        :return:
        '''
        dr = self.base_driver
        # 窗口最大化
        dr.maximize_window()
        # 输入后台网址
        # dr.navigate("http://192.168.2.151:7022/loginAction!gotoLogin.action")
        # URL_SUESS = 'http://192.168.2.151:7022/homeAction.action'
        dr.navigate("http://test.zxhgroup.com:8080/loginAction!gotoLogin.action")
        URL_SUESS = 'http://test.zxhgroup.com:8080/homeAction.action'
        URL = ''
        while URL != URL_SUESS:
            dr.type('id,account_id', data['user'])
            dr.type('id,old_password_id', data['pwd'])
            #
            dr.save_window_snapshot('..//zxh_photo/%s.png' %'全屏图')
            bai = dr._locate_element('id,validaImg')
            left = bai.location['x']
            top = bai.location['y']
            elementWidth = bai.location['x'] + bai.size['width']
            elementHeight = bai.location['y'] + bai.size['height']
            picture = Image.open('..//zxh_photo/%s.png' %'全屏图')
            picture = picture.crop((left, top, elementWidth, elementHeight))
            picture.save('..//zxh_photo/%s.png' %'指定区域图')
            image = Image.open('..//zxh_photo/%s.png' %'指定区域图')
            image = image.convert('L')
            # 这个是二值化阈值
            threshold = 150
            table = []
            for i in range(256):
                if i < threshold:
                    table.append(0)
                else:
                    table.append(1)
            # 通过表格转换成二进制图片，1的作用是白色,不然就全部黑色
            image = image.point(table, "1")
            # result = tesserocr.image_to_text(image)
            # print(result)
            image.save('..//zxh_photo/%s.png' %'指定区域图')
            # 截取指定图
            import pytesseract
            text = pytesseract.image_to_string(Image.open('..//zxh_photo/%s.png' %'指定区域图'), lang='eng')  # 设置为英文或阿拉伯字母的识别
            if text == ''or text.__contains__(' '):
                dr.click('id,validaImg')
            txty = re.findall('(\w*[0-9]+)\w*', text)
            txt = ''
            for q in range(len(txty)):
                txt = txt + txty[q]
            # print(txt)
            #
            dr.type('id,j_code', txt)
            dr.click('x,/html/body/form/div/div/div[2]/div[1]/div/input[1]')
            sleep(1)
            URL = dr.get_url()
        dr.remove_window()
    @staticmethod
    def csv_dict(path):
        '''将csv数据转成字典调用，把字典存放在列表中'''
        dict = []
        with open(path, 'r', encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)
            for rows in csv_reader:
                d = {}
                for k, v in rows.items():
                    d[k] = v
                dict.append(d)
        return dict
    @staticmethod
    def csv_list(path):
        '''将csv数据转成列表调用，跳过第一行'''
        list = []
        with open(path, mode='r', encoding='utf8') as f:
            casedata = csv.reader(f)
            num = True
            for row in casedata:
                if num == True:
                    num = False
                    continue
                list.append(row)
        return list
    def incaidan(self, caidan):
        """
        进入中信华后台菜单界面并进入嵌套
        :param caidan: 菜单名称
        :return:
        """
        dr = self.base_driver
        dr.switch_to_default()
        if self.versions == 'new':
            dr.type('x,//input[@placeholder="请输入搜索内容"]', caidan)
            dr.click('x,//*[@id="app"]/div/div[1]/div[3]/div/ul[2]/div/li/ul/li')
            sleep(1)
            dr.switch_to_frame('id,iframeEle')
        else:
            dr.switch_to_frame('id,tree_frame')
            dr.types('id,word', caidan)
            dr.click('x,//*[text()="%s"]' % caidan)
            dr.switch_to_default()
            dr.switch_to_frame('n,fram_work')
        return dr
    def circulation(self):
        '''
        循环点击菜单
        :return:
        '''
        dr = self.base_driver
        dr.switch_to_frame('id,tree_frame')
        dr.click_by_text('展开')
        for a in range(200):
            a = a + 1
            try:
                for b in range(200):
                    b = b + 1
                    try:
                        dr.click('x,//*[@id="dd%s"]/div[%s]/a' % (str(a), str(b)))
                        dr.switch_to_default()
                        dr.switch_to_frame('id,tree_frame')
                    except:
                        break
            except:
                break
    def jiage_xiadan(self):
        '''
        获取客户在线下单价格计算和验证订单金额以及物流费用和总价
        :return:
        '''
        dr = self.base_driver
        pingmijia = float(dr.get_text('x,//*[@id="rightBar-areaMoney"]'))
        mianji = float(dr.get_text('x,//*[@id="rightBar-totalArea"]'))
        gongchengfei = float(dr.get_text('x,//*[@id="rightBar-projectPrice"]'))
        xianbianfei = float(dr.get_text('x,//*[@id="rightBar-mouldMoney"]'))
        cesifei = float(dr.get_text('x,//*[@id="rightBar-testMoney"]'))
        # shuifei = float(dr.get_text('x,//*[@id="rightBar-invoiceForShow"]'))#因系统的税费是计算在单价里的
        guanghuifei = float(dr.get_text('x,//*[@id="rightBar-gerberPrice"]'))
        dingdanfei = float(dr.get_text('x,//*[@id="rightBar-orderMoney-2"]'))
        zongfei = float(dr.get_text('x,//*[@id="rightBar-totalMoney"]'))
        zongfei_1 = round(pingmijia*mianji+gongchengfei+xianbianfei+cesifei+guanghuifei,2)
        if zongfei_1 == zongfei and zongfei == dingdanfei:pass
        else:raise NameError('价格计算错误')
        dr.click_by_text('立即下单')
        return dingdanfei
    def jiage2(self):
        '''
        获取客户下单付款界面金额，用于验证金额的是否准确
        :return:
        '''
        dr = self.base_driver
        try:kuaidifei = float(dr.reserved_string(dr.get_text('x,//h5[text()="需要运费"]/span'),'d'))
        except:
            kuaidifei = float(0)
            print('快递方式：到付')
        dingdanfei1 = float(dr.reserved_string(dr.get_text('x,//h5[contains(text(),"订单费用")]/parent::td/following-sibling::td[1]/span'),'d'))
        wuliufei1 = float(dr.reserved_string(dr.get_text('x,//h5[contains(text(),"快递费用")]/parent::td/following-sibling::td[1]/span'),'d'))
        youhuijuan = float(dr.reserved_string(dr.get_text('x,//td/h5[@class="couponPrice ng-binding"]'), 'd'))
        feiyongheji = float(dr.reserved_string(dr.get_text('x,//h5[contains(text(),"费用总计")]/parent::td/following-sibling::td[1]/span'),'d'))
        if kuaidifei == wuliufei1 and round(dingdanfei1+kuaidifei-youhuijuan,2) == feiyongheji:pass
        else:raise NameError('在线下单订单第二页面费用核对有误')
        return dingdanfei1,feiyongheji