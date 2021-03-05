# s = 'detailsIdStr=435181&deliverymodecode=1&pageName=cash&contractId=297358&deliveryMode=%E9%A1%BA%E4%B8%B0%E6%A0%87%E5%BF%AB&payment=%E9%A2%84%E4%BB%98&paymentDetail=%E9%A2%84%E4%BB%98100%25&freightPayType=%E4%B9%99%E6%96%B9%28%E7%8E%B0%E4%BB%98%29&area=%E6%B7%B1%E5%9C%B3&merchandiser=%E5%BC%A0%E7%8E%B2&merchandiserId=3162&detailsIds=435181&detailsId=435181&billNumber=300&bakNumber=0&hideAccountNumber=2&note=2SH81553A%EF%BC%8CZXH2004291001%EF%BC%8C&deliveryModeCode1=160224&isReload=1&isLedProduct=0&queryFilterAreaId=1&isLed0=0&currePage=1&areaId=1&customerCode=&produceCode=&contractCode=&queryDepotStatus=&depotStatus=&queryDeliveryDate=&deliveryEndDate=&writeEndTime=&settlement=&peculiarPlankMark=&customerShort=&abnormal=&produceCodeStr=&noticeCodeStr=&contractCodeStr=&customerPO='
# s1 = 'isReload=1&customerCode=&produceCode=&contractCode=&isLedProduct=0&queryDepotStatus=&depotStatus=&queryFilterAreaId=1&queryDeliveryDate=&deliveryEndDate=&writerBeginTime=2020-01-30&writeEndTime=&settlement=&peculiarPlankMark=&isLed=0&customerShort=&detailsIdStr=435181&pageName=cash&currePage=1&contractId=297358&deliveryMode=%E9%A1%BA%E4%B8%B0%E5%BF%AB%E9%80%92&abnormal=&produceCodeStr=&noticeCodeStr=&contractCodeStr=&payment=%E9%A2%84%E4%BB%98&paymentDetail=%E9%A2%84%E4%BB%98100%25&deliveryModeCode=1&freightPayType=%E4%B9%99%E6%96%B9%28%E7%8E%B0%E4%BB%98%29&areaId=1&area=%E6%B7%B1%E5%9C%B3&merchandiser=%E5%BC%A0%E7%8E%B2&merchandiserId=3162&detailsIds=435181&detailsId=435181&billNumber=300&bakNumber=0&hideAccountNumber=2&customerPO=&note=2SH81553A%EF%BC%8CZXH2004291001%EF%BC%8C&deliveryModeCode1=160224'
# sd = dict(l.split('=') for l in s.split('&'))
# sd1 = dict(l.split('=') for l in s1.split('&'))
# sa=[]
# for u in sd1:
#     if u not in sd:
#         print(u)
# print(1)


# from urllib.request import quote
# a = '嘉立盛测试账户'
# b = quote(a)
# print(b)
# b1 = quote(b)
# print(b1)
# b2 = quote(b)
# print(b2)

# print(b)

# 解码是另一个模块
# from urllib import parse
# aa = '%25E5%2598%2589%25E7%25AB%258B%25E7%259B%259B%25E6%25B5%258B%25E8%25AF%2595%25E8%25B4%25A6%25E6%2588%25B7'
# # aa = '%E5%98%89%E7%AB%8B%E7%9B%9B%E6%B5%8B%E8%AF%95%E8%B4%A6%E6%88%B7'
# bb = parse.unquote(aa)
# bb = parse.unquote(bb)
# bb = parse.unquote(bb)
#
# print(bb)




##################################################################################
# bb = ''
# b = dict(u.split('=') for u in bb.split('&'))
# print(b)


# import re
# cc =  ["6078,'0077M',1,'Arte PCB-2','3371','A','C级'"]
# cc = cc[0]
#
# cc = re.sub('[\']', '', cc)
# r = cc.split(',')
# ff = re.findall(r'[A-Za-z]', r[-1])[0]
# print(ff)
# rr = r[1] + "'123'"
# print(rr)
# for rr in r:
#     print(rr)
# # 查看两个字典共有的key
# print(a.keys() & b.keys())
# # 查看字典a 和字典b 的不共有的key
# print(a.keys()^b.keys())
# # 查看在字典a里面而不在字典b里面的key
# print(b.keys()-a.keys())
# # 查看字典a和字典b相同的键值对
# print(a.items() & b.items())


# """
# from datetime import datetime
# from datetime import timedelta
# import time
#
# def date_add(date_str, days_count=1):
#     date_list = time.strptime(date_str, "%Y-%m-%d")
#     y, m, d = date_list[:3]
#     delta = timedelta(days=days_count)
#     date_result = datetime(y, m, d) + delta
#     date_result = date_result.strftime("%Y-%m-%d")
#     return date_result
#
# def num_to_char(num):
#     '''月份数字转中文'''
#     num=str(num)
#     listnum = list(num)
#     if listnum[0] == '0':
#         if str(len(listnum)) == '2':
#             num = listnum[1]
#     num_dict={"0":u"零","1":u"一","2":u"二","3":u"三","4":u"四","5":u"五","6":u"六","7":u"七","8":u"八","9":u"九","10":u"十","11":u"十一","12":u"十二",}
#     new_str=num_dict[num]+'月'
#     return new_str
#
# a = '2020-11-30 00:00'
# d = date_add(a.split('00:00')[0].strip()).split('-')
# f = d[-1]+num_to_char(str(d[1]))+d[0]
# print(1)
#
# """
# import re
# def extractValueViaRegularExpressions(pattern, text):
#     """
#     :param pattern: 正则表达式
#     :param text:    需要匹配的原字符串
#     :return:        返回匹配的值
#     """
#     matchObj = re.search(pattern, text, re.M|re.I)
#     rs = None
#     if matchObj:
#         print("正则表达式提取结果 : ", matchObj.group(0))
#         rs = matchObj.group(1)
#     else:
#         print("提取失败，没有匹配到结果")
#
#     return rs
# b = r"contractId=(.+?)';"
# a = "<script language='javascript'>  if(confirm('保存成功,是否打印合同?')){  location='/contract/contractAction!getContractDetailsToPrint.action?contractId=297652';  }else{ location='/contract/contractAction!getAllAccessOrders.action';} </script> "
# c = extractValueViaRegularExpressions(b,a)

# from lxml import etree
# import lxml
# a = 2
# print(type(2))
#
# if type(2) == lxml.etree._ElementUnicodeResult:
#     print(555)

#
# a = [{'a':'1','b':'2'},{'c':'3','d':'4'}]
# def parsetDictToWebFormFormat(ins):
#
#     if isinstance(ins, list):
#         try:
#             sstr = str()
#             for item in ins:
#                 for key, value in item.items():
#                     temp = '%s=%s' % (key, value)
#                     if sstr == '':
#                         sstr = temp
#                     else:
#                         sstr = '%s&%s' % (sstr, temp)
#             print(sstr.encode('utf-8'))
#             return sstr.encode('utf-8')
#
#         except Exception as msg:
#             raise msg
#     else:
#         print('入参必须是列表类型，当前入参类型是: %s' % type(ins))
# b= parsetDictToWebFormFormat(a)



####################################改变字符串######################################################
# aa = 'isReload=1&customerName=&customerCode=0046U&keyWord=&currePage=1&customerGradeLevelName=A%E7%BA%A7&isLEDOrderReload=1&orderFeeRangLimit=200&customerShort=%E5%8D%8E%E9%B9%8F%E7%94%B5%E5%8A%9B&merchId=45&isCombination=0&ledOrderInfoVO.ledProductId=601&ledOrderInfoVO.ledCategory=0&productLowestPrice=23.0&productLowestNumber=1000&standardPrice=23.0&productModel=%E5%AE%A4%E5%86%85%E5%85%A8%E5%BD%A93.910&productColor=&productSpecification=&productNameMo=&innerCode=&productId=601&productName=%E5%AE%A4%E5%86%85%E5%85%A8%E5%BD%A93.910%282PH76868A%29&internalCode=2PH76868A&productUnitPrice=23.0&productBoardSize=25*25&pLowestPrice=23.0&pLowestNumber=1000&ledOrderInfoVO.merchId=45&customerId=4271&customerCodeStr=0046U&ledOrderInfoVO.customerId=4271&ledOrderInfoVO.customerCode=0046U&ledOrderInfoVO.customerShort=%E5%8D%8E%E9%B9%8F%E7%94%B5%E5%8A%9B&ledOrderInfoVO.ledStatus=2&ledOrderInfoVO.orderCode=&ledOrderInfoVO.produceCode=&ledOrderInfoVO.materielCode=&ledOrderInfoVO.orderProducts=%E5%AE%A4%E5%86%85%E5%85%A8%E5%BD%A93.910%282PH76868A%29&ledOrderInfoVO.model=2PH76868A&ledOrderInfoVO.discount=1&ledOrderInfoVO.standardUnitPrice=23.0&ledOrderInfoVO.boardSize=25*25&ledOrderInfoVO.unitPrice=23.0&ledOrderInfoVO.orderNumber=332&total=7636.00&ledOrderInfoVO.weight=&totalWeight=&ledOrderInfoVO.orderDate=2020-07-04&ledOrderInfoVO.deliveryTime=2020-07-04&ledOrderInfoVO.addressId=5420&ledOrderInfoVO.note=&ledOrderInfoVO.sendNotice='
# a = dict(u.split('=') for u in aa.split('&'))
# print(a)
# ############################################
# a = ['领料', '钻孔(锣有铜槽）', '外层线路', '图形转移（2铜）', 'AOI扫描/蚀刻检查/中测', '二钻', '防焊', '字符', '表面处理', '成型', 'E-T测试FQC', '包装']
# b = ['30', '14', '16', '17', '25', '134', '18', '19', '20', '21', '22', '23']
# c = zip(a,b)
# d = []
# for row in c:
#     yy = []
#     for rr in row:
#         yy.append(rr)
#     d.append(yy)
# print(d)

# a = [['领料', '30'], ['钻孔(锣有铜槽）', '14'], ['外层线路', '16'], ['图形转移（2铜）', '17'], ['AOI扫描/蚀刻检查/中测', '25'], ['二钻', '134'], ['防焊', '18'], ['字符', '19'], ['表面处理', '20'], ['成型', '21'], ['E-T测试FQC', '22'], ['包装', '23']]
# b = [['yh01', '137', 'jls123', '内层压合'], ['01', '14', 'jls123', '钻孔(锣有铜槽）'], ['jx03', '15', 'jls123', '导电胶'], ['04', '16', 'jls123', '外层线路'], ['jszxh1002', '17', 'jls123', '图形转移（2铜）'], ['st07', '25', 'jls123', 'AOI扫描/蚀刻检查/中测'], ['jxzk02', '134', 'jls123', '二钻'], ['st10', '18', 'jls123', '防焊'], ['jx10', '19', 'jls123', '字符'], ['jx11', '20', 'jls123', '表面处理'], ['jxzk02', '134', 'jls123', '二钻'], ['jxsccx', '21', 'jls123', '成型'], ['jx13', '22', 'jls123', 'E-T测试FQC'], ['15', '23', 'jls123', '包装']]
# def group_scan_list(list,lists):
#     '''
#     数据处理，分配组合扫描条码用的数据
#     :param list:
#     :param lists:
#     :return:
#     '''
#     for row in list:
#         if row[0] == '领料':
#             continue
#         for rows in lists:
#             if row[0] in rows:
#                 break
#         break
#     rows.insert(1,row[-1])
#     return rows
# ll = group_scan_list(a,b)
# print(ll)

# import re
# a = 'https://test.zxhwork.com/web/webCompanyDynamicAction!selectCompanyDynamicData.action%3FdynamicType=wishText'
# c=re.search('.*(?=%)',a)
# b=re.search('.*(?=%)',a).group()
# print(1)

# def function(arg,*args,**kwargs):
#     print(arg,args,kwargs)
#
# function(6,7,8,9,a=1, b=2, c=3)

#6 (7, 8, 9) {'a': 1, 'b': 2, 'c': 3}

# from base.box_driver import BoxDriver,BoxBrowser
# a = BoxDriver(BoxBrowser.Chrome)
# a.navigate('https://www.baidu.com/')


# import random                           #导入random模块
# num = random.sample(range(200),10)
#
# print(sorted(num))
# print(1)