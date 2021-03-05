# from lxml import etree
# import document as document
# import Image
from base.box_driver import BoxDriver,BoxBrowser
from time import sleep
from zhongxinhua.page2.zxh_commad1 import ZXH_COMMAD_LIUCHENG
from zhongxinhua.api.apisac import api_sac


class Zxh(ZXH_COMMAD_LIUCHENG):

    def kehu_xiadan(self,dict,xiadan_path):
        dr = self.base_driver
        self.handles = dr.current_window_handle()
        dr.open_new_window('l,— 在线下单')
        sleep(1)
        dr.click('s,input[value="单片"]')
        dr.click('s,input[value="%s层"]'%dict['板层'])
        dr.type('id,length',dict['板长'])
        try:
            dr.click('s,input[value="确认"]')
            dr.click('s,input[value="确认"]')
        except:pass
        dr.type('id,width',dict['板宽'])
        try:
            dr.click('s,input[value="确认"]')
            dr.click('s,input[value="确认"]')
        except:pass
        dr.click('id,orderNumberDiv')
        dr.type('id,otherNumber',dict['板数'])
        dr.click_by_text('确认')
        dr.wait_selenium('id,invoice1').click()
    ##点击提交订单
        jia = self.jiage_xiadan()
        #
        sleep(2)
        tongji = self.jiage2()
        self.jiaa = tongji[-1]  #订单付款总价
        if jia == tongji[0]:pass
        else:raise NameError('付款价格计算错误')
        txtpath = dr.change_name(xiadan_path)
        dr.wait_selenium('id,absFile').send_keys(txtpath)
        while dr.wait_selenium('x,//span[contains(text(),"文件名称:")]/following-sibling::span[1]',10).text == '':sleep(1)
        dr.execute_script_element('x,//button[text()="提交订单"]')
        dr.wait_selenium('x,//button[text()="提交订单"]').click()
        dr.wait_selenium('x,//span[contains(text(),"订单提交成功")]')#判断是否下单成功
        dr.close_browser()
        dr.switch_to_window(self.handles)
        self.leixing = '玻纤板'
        return self.handles

if __name__ == '__main__':
    data = {'user': 'jlsdev', 'pwd': 'jls123'}
    dict={'板层': '2', '板长': '16.8','板宽': '14', '板数': '150'}
    kehu_user = '18889K';kehu_pwd = 'a123456'
    # 前台
    b = Zxh(BoxDriver(BoxBrowser.Chrome))
    # 登陆前台
    b.kehu_login(kehu_user, kehu_pwd)
    # 提交订单
    handle = b.kehu_xiadan(dict,b.xiadan_path)
    # 后台,打开新标签
    b.base_driver.add_window('window.open();')
    # 登陆后台
    b.base_driver.implicitly_wait(1)
    houtai_handle = b.login_zxh(data,handle)
    # 审核订单
    b.shenghe(kehu_user)
    # 付款
    b.kehu_fukuan()
    # 切到后台
    b.base_driver.switch_to_window(houtai_handle)
    # 获取订单合同号
    hetong_text = b.hetongcx()
    # 生成下单通知单
    b.xiadantzd(hetong_text,handle)
    # 工程师审核,主管审核
    production_number = b.gcs_zg_sh()
    # 工程制作
    b.incaidan('通知单进度查询')
    b.gcgl(dict,b.shangchaunpath,b.zuankong_path)
    # 生成基材领料单
    b.jicai()
    # 领料出库
    b.lingliaochuku(b.wuliaonumber)
    # 开启wip，获取条码#开启wip，获取条码
    saomiao,factory = b.wip()
    # *******UI扫描***********
    # 扫描工艺
    # b.gysaomiao(saomiao,'深圳',handle)
    # 登录后台
    # *******接口扫描*********
    api_sac().aaa(saomiao)
    # b.login_zxh(data, handle)
    # #审核包装
    b.shbaozhaung()
    #开单发货
    b.kaidaofahuo(diqu='深圳')
    # #备货
    b.beihuo(hetong_text,'10')
    #确认发货
    b.qrfahuo(hetong_text)
    print('完成流程')