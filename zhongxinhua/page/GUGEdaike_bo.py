# import Image
from zhongxinhua.page2.zxh_commad1 import ZXH_COMMAD_LIUCHENG
# import tesserocr
# import document as document
from base.box_driver import BoxDriver,BoxBrowser
from time import sleep
# from lxml import etree
from zhongxinhua.api.apisac import api_sac


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
    data = {'user': 'jlsdev', 'pwd': 'jls123'}
    dict = {'客编': '0077M','代客单': '5','模具': '铣边','测试架': '飞针测试',
            '板长': '20','板宽': '20.5',
            '拼版1': '1',
            '拼版2': '1',
             '下单数量': '100'}

    b = Zxh_houtai(BoxDriver(BoxBrowser.Chrome))

    b.login_zxh(data)                                           # 登陆后台

    b.daikexiadan(dict,b.shangchaunpath)                        # 代客下单

    b.shenghe(dict['客编'])                                      # 审核订单

    # b.fandan(production_number='2PW112297A',leixing='玻纤板')  #返单

    hetong_text = b.hetonglc()                                  # 合同的生成,上传附件,代客确认

    b.kuandaofahuo(hetong_text)                               # 填写款到通知单
    # hetong_text = 'ZXH2006181008'

    b.xiadantzd(hetong_text)                                    # 下单通知单

    production_number = b.gcs_zg_sh()                           # 工程师审核,主管审核
    b.incaidan('通知单进度查询')

    b.gcgl(dict,b.shangchaunpath,b.zuankong_path)               # 工程制作

    b.jicai()                                                   # 生成基材领料单

    b.lingliaochuku(b.wuliaonumber)                             # 领料出库

    saomiao,factory = b.wip()                                   # 开启wip，获取条码
    # *******UI扫描***********
    # 扫描工艺
    # b.gysaomiao(saomiao,factory='深圳')
    # # # 登录后台
    # b.login_zxh(data)

    api_sac().aaa(saomiao)                                      #*******接口扫描*********

    b.shbaozhaung()                                             # 审核包装

    b.kaidaofahuo(diqu='深圳')                                   #开单发货

    b.shsonghuodan(hetong_text)                                 # 审核送货单

    b.beihuo(hetong_text, '10')                                 # 备货

    b.qrfahuo(hetong_text)                                      # 确认发货
    print('完成流程')