# def calc(x,y):
#     print('---------------------')
#     try:
#         res = x / y
#     except TypeError as e:
#         return '传入对象类型与要求不符'
#     except Exception as e:
#         print('其他异常')
#         return e
#     else:
#         print('无异常，一切正常')
#         return res
#     finally:
#         print('无论是否有异常，都要走到这里')
#
# # print(calc(1,2))#这个没有出异常，走else和finally语句
# # print(calc(1,'x'))#这个出现传入参数类型不正确的异常，会返回传入对象类型与要求不符合，和执行finally的代码
# print(calc(1,0))#

for i in range(1):
    print(i)