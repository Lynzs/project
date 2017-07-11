# -*- coding utf-8 -*-
def bank(b,balance):
    while b != None:
        if b == keys[0]:
            print("您当前账户余额为：", balance)
            break
        elif b == keys[1]:
            saveMoney = int(input("请放入钞票："))
            balance = balance + saveMoney
            print("您当前账户余额为：", balance)
            break
        elif b == keys[2]:
            while b==keys[2]:
                drawMoney = int(input("请输入取出金额："))
                if (balance-drawMoney)<0:
                    print("您输入的取出金额大于您的余额，请重新输入：")
                    continue
                else:
                    balance = balance - drawMoney
                    print("您当前账户余额为：", balance)
                    break
            break
        elif b == keys[3]:
            while b == keys[3]:
                payment = int(input("请输入缴费金额："))
                if (balance-payment)<0:
                    print("您输入的缴费金额大于您的余额，请重新输入：")
                    continue
                else:
                    balance = balance - payment
                    print("您当前账户余额为：", balance)
                    break
            break
        elif b == keys[4]:
            break
        else:
            print("没有该项操作！")
            break
    return balance


errorcount=0
userName = "zhangsan"
passWord = "123456"
balance=1000
username = input("请输入用户名：")
password = input("请输入密码：")
keys=['查询余额','存款','取款','缴费','退出']
while True:
    if (userName == username) and (passWord == password):
        if errorcount>=3:
            print("今天已输入错误超过3次，请明天再试")
            username = input("请输入用户名：")
            password = input("请输入密码：")
        else:
            button1 = input("请输入下一步操作：查询余额/取款/存款/缴费/退出：")
            balance = bank(button1,balance)
            if button1 == keys[4]:
                break

    else:
        errorcount += 1
        if errorcount>=3:
            print("今天已输入错误超过3次，请明天再试")
        else:
            print("输入用户/密码错诶，请从重新输入：")
        username=input("请输入用户名：")
        password=input("请输入密码：")
print("欢迎下次光临！")

