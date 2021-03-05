from zhongxinhua.page.GUGE2 import Zxh
from base.box_driver import BoxBrowser,BoxDriver
from zhongxinhua.api.apisac import api_sac


# shangchaunpath = 'D:\\上传文件'
# 前台
# b = Zxh(BoxDriver(BoxBrowser.Chrome))
# b.biaomian = '有铅'
# b.login_zxh(data={'user': 'jlsdev', 'pwd': 'jls123'})
# shuju = b.xiadantzd()  # 下单通知单
# b.gcs_sh(xiadan_text=shuju[0])  # 工程师审核
# b.zgsh(xiadan_text=shuju[0])  # 主管审核
# b.gcgl('','','','')  # 工程制作
# b.jicai(xiadan_text=shuju[0])  # 基材
# b.lingliaochuku(xiadan_text=shuju[0])  # 领料出库
# saomiao = b.wip(xiadan_text=shuju[0])  # 开启wip，获取条码
saomiao=['H67219Z1','H67219Z2','H67219Z3']
api_sac().aaa(saomiao)
# b.gysaomiao(saomiao,'深圳')  # 扫描工艺
# b.gongyipeizhi(name='22',bianma='22',cangfang='江苏二厂',cengshu='2',biaomian='喷锡',leixing='玻纤板',
#                xianlu='全部',cesi='飞针测试',erzuan='无')