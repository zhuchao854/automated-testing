from zhongxinhua.page2.zxh_commad1 import ZXH_COMMAD_LIUCHENG
from base.box_driver import BoxDriver,BoxBrowser

class BULIAO(ZXH_COMMAD_LIUCHENG):

    def djmrb(self,pcscount):
        '''
        mrb登记报废
        :param pcscount: pcb报废数量
        :return:
        '''
        dr = self.incaidan('WIP工艺进度查询')
        self.barcode = dr.get_text('x,//*[@id="tr_6"]/td[5]/span')
        dr = self.incaidan('MRB登记(新)')
        handle = dr.open_new_window('id,searchBarCodeImg')
        dr.types('n,queryBarCode',self.barcode)
        dr.wait_selenium('x,//a[text()="确认"]').click()
        dr.switch_to_window(handle)
        if self.versions == 'new':
            dr.switch_to_frame('id,iframeEle')
        else:
            dr.switch_to_frame('n,fram_work')
        dr.select_by_visible_text('id,responsibilityProcess','钻孔')
        dr.click('s,input[value="请选择"]')
        dr.click('x,//li[@selectvalue="漏钻"]')
        dr.type('id,pcsAmount',pcscount)
        dr.click('s,input[value="保存草稿"]')
        dr.wait_selenium('s,input[value="确认报废"]').click()
        text = dr.switch_to_alert()
        if text.__contains__('报废成功！'):
            dr.accept_alert()
        else:raise NameError('没有成功报废')

    def mrbbuliao(self):
        '''
        填写补料申请单
        :return:
        '''
        dr = self.incaidan('MRB登记列表(新)')
        dr.types('n,selectBarCode',self.barcode)
        dr.click('id,sta_0')
        dr.wait_selenium('s,input[value="填写补料申请"]').click()
        dr.wait_selenium('s,input[value="保存并提交计划部"]').click()
    def plan(self):
        '''
        补料申请计划部
        :return:
        '''
        dr = self.incaidan('补料申请记录(计划部)')
        dr.click('x,//img[@alt="填写计划部意见"]')
        dr.type('id,burdenProducer','1')
        dr.type('id,burdenAuditor','1')
        dr.type('id,projectAdvice','1')
        dr.click('s,input[value="保存并提交市场部"]')
    def bazaar(self):
        '''
        补料申请市场部
        :return:
        '''
        dr = self.incaidan('补料申请记录(市场部)')
        dr.click('n,areaIdList')
        dr.click('x,//img[@alt="确认是否需要补料"]')
        dr.type('id,martAdvice','1')
        dr.click('s,input[value="确认补料"]')
    def deputy(self):
        '''
        补料申请副总
        :return:
        '''
        dr = self.incaidan('补料申请记录(副总)')
        dr.click('n,areaIdList')
        dr.click('x,//img[@alt="填写副总经理意见"]')
        dr.type('id,bossAdvice','1')
        dr.click('id,sbtn')
    def quality(self):
        '''
        补料申请品质部
        :return:
        '''
        dr = self.incaidan('补料申请记录(品质部)')
        dr.click('n,areaIdList')
        dr.click('s,input[value="编辑责任划分"]')
        dr.type('id,lossTo','1')
        dr.type('id,losstoMoney','1')
        dr.click('id,sbtn')
    def finance(self):
        '''
        补料申请财务
        :return:
        '''
        dr = self.incaidan('补料申请记录(财务部)')
        dr.click('n,areaIdList')
        dr.click('x,//img[@alt="确认责任划分"]')
        dr.wait_selenium('id,sbtn').click()
    def producebuliao(self):
        '''
        生成补料订单
        :return:
        '''
        dr = self.incaidan('待补料单列表')
        xiadan_text = self.barcode.split('B')[0]
        dr.types('id,noticeCode',xiadan_text)
        dr.wait_selenium('s,input[value="补料生成"]').click()

if __name__ == '__main__':
    data = {'user': 'jlsdev', 'pwd': 'jls123'}
    q = BULIAO(BoxDriver(BoxBrowser.Chrome))
    q.base_driver.implicitly_wait(2)
    q.login_zxh(data)
    q.djmrb('1')#mrb报废数量
    q.mrbbuliao()
    q.plan()
    q.bazaar()
    q.deputy()
    q.quality()
    q.finance()
    q.producebuliao()
