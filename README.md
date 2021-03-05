自动化测试



框架结构:
automated-testing
base   基础封装
menu   JLC扫描菜单
Jlc_system  嘉立创ERP系统
|----case     测试用例
|----data     数据
|----main     主入口
|----page     页面设计
|----report   测试报告
|----runner    组织用例
|----screenshot 截图

文件存放路径
D:\\上传文件

样板下单-拼版前流程
1-前台下单至下发拼版，执行
automated-testing\Jlc_system\page\OrderSample_step1.py
2-拼版软件完成拼版（手工完成）
3-内编工艺扫描，执行
automated-testing\Jlc_system\page\process_scan_step2.py
4-扫描之外其他流程，执行
automated-testing\Jlc_system\page\OrderSample_step3.py

批量下单-拼版前流程
1-前台下单至下发拼版，执行
automated-testing\Jlc_system\page\OrderBatch_step1.py
2-拼版软件完成拼版（手工完成）
3-内编工艺扫描
automated-testing\Jlc_system\page\process_scan_step2.py
4-扫描之外其他流程
automated-testing\Jlc_system\page\OrderBatch_step3.py

PCB+钢网下单流程
automated-testing\Jlc_system\page\OrderSample_steel_step1.py
钢网下单之后的后续流程：
automated-testing\Jlc_system\page\OrderSteel_step2.py
小批量+钢网下单流程
automated-testing\Jlc_system\page\OrderBatch_steel_step1.py

PCB+SMT下单流程
automated-testing\Jlc_system\page\OrderSample_smt_step1.py