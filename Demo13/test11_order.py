'''
功能要求：
要求用户输入总资产，例如： 2000
显示商品列表，让用户根据序号选择商品和数量
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功，并显示剩余金额。并询问是否继续购买，是则同上，否则退出。
屏幕显式：
-----------------------------
序号   商品      价格
   1.   电脑     1999
   2.   鼠标        30
   3.   手机       998
   4.   键盘        50
-----------------------------
请输入您的资产总额：
'''
print("序号   商品      价格\n"
      "1.   电脑      1999\n"
      "2.   鼠标        30\n"
      "3.   手机       998\n"
      "4.   键盘        50")
sum1 = int(input("请输入总资产："))
while True:
    no = int(input("请输入序号："))
    if no > 4:
        print("输入异常")
        break
    number = int(input("请输入数量:"))
    list_price = [1999, 30, 998, 50]
    price = list_price[no - 1]
    sum2 = number * price
    if sum2 <= sum1:
        sum2 = sum1 - sum2
        sum1 = sum2
        print(f"购买成功,剩余余额为：{sum2}")
        option = input("是否继续购买,请输入是或者否：")
        if option == '是':
            pass
        else:
            break
    else:
        print("账户余额不足！")
        break
