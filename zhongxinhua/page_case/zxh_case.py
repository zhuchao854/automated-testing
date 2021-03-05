from zhongxinhua.page.GUGE2 import Zxh
from zhongxinhua.page.GUGEdaike_bo import Zxh_houtai
from zhongxinhua.page.GUGEdaike_led import Zxh_houtai_LED
from zhongxinhua.page.GUGEdaike_lv import Zxh_houtai_LJB
from zhongxinhua.page2.buliao import BULIAO
from zhongxinhua.api.apisac import api_sac

class zxh_test(Zxh_houtai,Zxh_houtai_LED,Zxh_houtai_LJB,Zxh,BULIAO):
    original_name=''
    def backstage_bo(self,dict):
        # 登陆后台
        self.login_zxh(dict)
        # 代客下单
        # for ii in range(1):
        self.daikexiadan(dict, self.shangchaunpath)
        # 审核订单
        self.shenghe(dict['客编'])
        # 合同的生成,上传附件,代客确认
        hetong_text = self.hetonglc()
        # 填写款到通知单
        self.kuandaofahuo(hetong_text)
        # 下单通知单
        self.xiadantzd(hetong_text)
        # 工程师,主管审核
        production_number = self.gcs_zg_sh()
        # 工程制作
        self.gcgl(dict, self.shangchaunpath, self.zuankong_path)
        # 生成基材领料单
        self.jicai()
        # 领料出库
        self.lingliaochuku(self.wuliaonumber)
        # 开启wip，获取条码
        saomiao, factory = self.wip()
        # 扫描工艺
        # self.gysaomiao(saomiao, factory='深圳')
        api_sac().aaa(saomiao)
        # 登录后台
        self.login_zxh(dict)
        # 审核包装
        self.shbaozhaung()
        #开单发货
        self.kaidaofahuo(diqu='深圳')
        # 审核送货单
        self.shsonghuodan(hetong_text)
        # 备货
        self.beihuo(hetong_text, '10')
        # 确认发货
        self.qrfahuo(hetong_text)
        return production_number
    def backstage_led(self,data,dict):
        # 登陆后台
        self.login_zxh(data)
        # 代客下单
        self.daikexiadan_led(dict)
        # 总经理审核订单
        self.general_manager_review_order()
        # 合同的生成,上传附件,代客确认
        hetong_text = self.hetonglc()
        # 填写款到通知单
        self.kuandaofahuo(hetong_text)
        # 调整led库存
        self.led_inventory(dict)
        # 开单发货
        self.kaidaofahuo_led(hetong_text)
        # 审核送货单
        self.shsonghuodan(hetong_text)
        # 备货
        self.beihuo(hetong_text, '10')
        # 确认发货
        self.qrfahuo(hetong_text)
    def backstage_lv(self,data,dict):
        # 登陆后台
        self.login_zxh(data)
        # 代客下单
        # for ii in range(1):
        self.daikexiadan_lv(dict, self.shangchaunpath)
        # 审核订单
        self.shenghe(dict['客编'])
        # 合同的生成,上传附件,代客确认
        hetong_text = self.hetonglc()
        # 填写款到通知单
        self.kuandaofahuo(hetong_text)
        # 下单通知单
        self.xiadantzd(hetong_text)
        # 工程师,主管审核
        production_number = self.gcs_zg_sh()
        # 工程制作
        self.gcgl(dict, self.shangchaunpath, self.zuankong_path)
        # 生成基材领料单
        self.jicai()
        # 领料出库
        self.lingliaochuku(self.wuliaonumber)
        # 开启wip，获取条码
        saomiao, factory = self.wip()
        # 扫描工艺
        # self.gysaomiao(saomiao, factory='深圳')
        api_sac().aaa(saomiao)
        # 登录后台
        self.login_zxh(data)
        # 审核包装
        self.shbaozhaung()
        # #开单发货
        self.kaidaofahuo(diqu='深圳')
        # 审核送货单
        self.shsonghuodan(hetong_text)
        # 备货
        self.beihuo(hetong_text, '10')
        # 确认发货
        self.qrfahuo(hetong_text)
        return production_number
    def online_kf(self,kehu_user,kehu_pwd,data,dict):
        # 登陆前台
        self.kehu_login(kehu_user, kehu_pwd)
        # 提交订单
        handle = self.kehu_xiadan(dict, self.xiadan_path)
        # 后台,打开新标签
        self.base_driver.add_window('window.open();')
        # 登陆后台
        self.base_driver.implicitly_wait(1)
        houtai_handle = self.login_zxh(data, handle)
        # 审核订单
        self.shenghe(kehu_user)
        # 付款
        self.kehu_fukuan()
        # 切到后台
        self.base_driver.switch_to_window(houtai_handle)
        # 获取订单合同号
        hetong_text = self.hetongcx()
        # 下单通知单
        self.xiadantzd(hetong_text, handle)
        # 工程师,主管审核
        production_number = self.gcs_zg_sh()
        # 工程制作
        self.gcgl(dict, self.shangchaunpath, self.zuankong_path)
        # 生成基材领料单
        self.jicai()
        # 领料出库
        self.lingliaochuku(self.wuliaonumber)
        # 开启wip，获取条码#开启wip，获取条码
        saomiao, factory = self.wip()
        # 扫描工艺
        # self.gysaomiao(saomiao, '深圳', handle)
        api_sac().aaa(saomiao)
        # 登录后台
        self.login_zxh(data, handle)
        # #审核包装
        self.shbaozhaung()
        # 开单发货
        self.kaidaofahuo(diqu='深圳')
        # #备货
        self.beihuo(hetong_text, '10')
        # 确认发货
        self.qrfahuo(hetong_text)
    def backstage_copy(self,data,case_config):
        # 登陆后台
        self.login_zxh(data)
        # 复制订单
        self.fandan(production_number=case_config[0], leixing=case_config[-1])
        # # 合同的生成,上传附件,代客确认
        hetong_text = self.hetonglc()
        # # 填写款到通知单
        self.kuandaofahuo(hetong_text)
        # # 下单通知单
        self.xiadantzd(hetong_text)
        # 工程师,主管审核
        production_number = self.gcs_zg_sh()
        # 工程制作
        self.gcgl(dict, self.shangchaunpath, self.zuankong_path)
        # 生成基材领料单
        self.jicai()
        # 领料出库
        self.lingliaochuku(self.wuliaonumber)
        # 开启wip，获取条码
        saomiao, factory = self.wip()
        # 扫描工艺
        # self.gysaomiao(saomiao, factory='深圳')
        api_sac().aaa(saomiao)
        # # 登录后台
        self.login_zxh(data)
        # 审核包装
        self.shbaozhaung()
        # #开单发货
        self.kaidaofahuo(diqu='深圳')
        # 审核送货单
        self.shsonghuodan(hetong_text)
        # 备货
        self.beihuo(hetong_text, '10')
        # 确认发货
        self.qrfahuo(hetong_text)
    def buliao(self,data):
        self.base_driver.implicitly_wait(2)
        self.login_zxh(data)
        self.djmrb('1')  # mrb报废数量
        self.mrbbuliao()
        self.plan()
        self.bazaar()
        self.deputy()
        self.quality()
        self.finance()
        self.producebuliao()