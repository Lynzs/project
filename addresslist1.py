import cProfile as p
import os
import re


class Item:
    def __init__(self, name, age, gender, call):
        self.name = name
        self.age = age
        self.gender = gender
        self.call = call


def menu():
    print("")
    print("1.insert an item ")
    print("2.delete an item")
    print("3.Modify an item")
    print("4.Display all item")
    print("5.Sort all items")
    print("6.Exit the program")
    print("What do you want to do?")

def step():
    while True:
        menu()
        sel = int(input())
        if sel == 1:
            insert()
        elif sel == 2:
            delete()
        elif sel == 3:
            modify()
        elif sel == 4:
            display()
        elif sel == 5:
            sort1()
        elif sel == 6:
            search()
        else:
            break

def insert():
    name = input("请输入姓名：")
    age = (input("请输入年龄："))
    gender = input("请输入性别：")
    while True:
        call = input("请输入手机号：")
        p=re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
        math=p.match(call)
        if math:
            item = Item(name, age, gender, call)
            global itemlist
            itemlist.append(item)
            break
        else:
            print("输入手机号错误，请输入正确的手机号：")



def output(item):
    print("%s is %s岁， gender is %s，call is %s" % (item.name, item.age, item.gender, item.call))




def display():
    global itemlist
    l = len(itemlist)
    # print(name,age,gender)
    for i in range(0, l):
        output(itemlist[i])
    print("")


def delete():
    valuable = input("请输入删除条件：")
    global itemlist
    l = len(itemlist)
    for i in range(0, l):
        if (itemlist[i].name == valuable) or (itemlist[i].call == valuable):
            itemlist.pop(i)
            print("已删除！")
            break


def updata (item, count):
    if count == 0:
        item.name = input("请输入你想要修改的姓名：")
    elif count == 1:
        item.name = input("请输入新的姓名：")
        item.age = input("请输入新的年龄：")
    elif count == 2:
        item.name = input("请输入新的姓名：")
        item.gender = input("请输入新的性别：")
    elif count == 3:
        item.call = input("请输入新的手机号：")
    elif count == 4:
        item.name = input("请输入新的姓名：")
        item.age = input("请输入新的年龄：")
        item.gender = input("请输入新的性别：")
        item.call = input("请输入新的手机号：")


def modify():
    global itemlist
    l = len(itemlist)
    while True:
        count = int(input("请输入你要操作的编号：0：修改姓名 1：修改姓名、年龄 2：修改姓名、性别 3：修改手机号 4：修改姓名、年龄、性别、手机号"))
        if count > 4:
            print("请输入正确的操作序号！")
            continue


        if count != 3:
            name = input("请输入姓名：")
            for i in range(0, l):
                if itemlist[i].name == name:
                    updata(itemlist[i], count)
                    print("update done!")
                    break
        else:
            call = input("请输入手机号：")
            for i in range(0, l):
                if itemlist[i].call == call:
                    updata(itemlist[i], count)
                    print("update done!")
                    break


def sort1():
    global itemlist
    n = input("请输入排序方式：")
    if n == "name":
        itemlist.sort(key=lambda item:item.name, reverse=True)
    if n == "age":
        itemlist.sort(key=lambda item: item.age, reverse=True)
    print("sort done!")

def search():
    var = input("请输入查询条件：")
    global itemlist
    for i in range(len(itemlist)):
        Boolt = is_num_by_except(var)
        if Boolt:
            if len(var) >= 3:
                recount = isSubstring(var, itemlist[i].call)
            else:
                recount = isSubstring(var, itemlist[i].age)

        elif (var == "男") or (var == "女"):
            recount = isSubstring(var, itemlist[i].gender)
        else:
            recount = isSubstring(var, itemlist[i].name)
        if recount:
            output(itemlist[i])
        elif not recount:
            continue
        else:
            print("没有匹配的条件，请重新输入查询条件")
            break


def isSubstring(str1, str2):
    return str1 in str2

def is_num_by_except(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


itemlist = []
step()
print("goodbye!")
