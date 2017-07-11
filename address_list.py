import cProfile as p
import os
class Item:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

def menu():
    print("")
    print("1.insert an item ")
    print("2.delete an item")
    print("3.Modify an item")
    print("4.Display all item")
    print("5.Sort all items")
    print("6.Exit the programe")
    print("What do you want to do?")

def begin():
    global itemlist
    if os.path.exists('memberlist.data')==True:
        listfile=file('memberlist.data','r')
        if len(listfile.read())!=0:
            listfile.seek(0)
            itemlist=p.load(listfile)
        listfile.close()

def end():
    global itemlist
    listfile=file('memberlist.data','w+')
    p.dump(itemlist,listfile)
    listfile.close()
    

def insert():
    name=input("请输入姓名：")
    age=int(input("请输入年龄："))
    gender=input("请输入性别：")
    item=Item(name,age,gender)
    global itemlist
    itemlist.append(item)

def output():
    print("%s is %d gender is %s" %(item.name,item.age,item.gender))

def display():
    global itemlist
    l=len(itemlist)
    print("name,age,gender")
    for i in range(0,l):
        output(itemlist[i])
    print("")

def delete():
    name=input("请输入你想要删除的姓名：")
    global itemlist
    l=len(itemlist)
    for i in range(0,l):
        if itemlist[i].name==name:
            itemlist.pop(i)
            break

def updata():
    item.name=input("请输入姓名：")
    item.age=input("请输入年龄：")
    item.gender=input("请输入性别：")

def modify():
    name=input("请输入你想要修改的姓名：")
    global itemlist
    l=len(itemlist)
    for i in range(0,l):
        if itemlist[i].name==name:
            updata(itemlist[i])
            print("updata done!")

def sort():
    global itemlist
    itemlist.sort(None,key=lambda item:item.name)
    print("sort done!")


itemlist=[]
begin()
while True:
    menu()
    sel=int(input())
    if sel==1:
        insert()
    elif sel==2:
        delete()
    elif sel==3:
        modify()
    elif sel==4:
        display()
    else:
        break
end()
print("goodbye!")