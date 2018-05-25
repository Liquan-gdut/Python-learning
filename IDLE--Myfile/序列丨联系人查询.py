#1：联系人查询，输入对应名字，输出值
#2：新建联系人，输入名字、电话号码，插入到字典中
#3：删除联系人，输入名字，pop
#4：退出，谢谢您的使用，break
#思路：外层循环：根据输入进入内层循环：4,3,2,1定义功能
print("""#1：联系人查询
#2：新建联系人
#3：删除联系人
#4：查看所有联系人
#5：退出""")
phoneTable={}
while 1:
    fun=input("请选择功能序号：")
    if fun=="5":
        print("Thanks for your using")
        break
    if fun=="4":
        for name,phone in phoneTable.items():
            print(name,phone)
    if fun=="1":
        while 1:
            name=input("(提示：按q返回上一层)请输入待查询联系人姓名:")
            if name=="q":
                break
            if name in phoneTable:
                print("联系方式：",phoneTable[name])
            else:
                print("联系人不存在")
    if fun=="2":
        while 1:
            name=input("(提示：按q返回上一层)请输入新联系人姓名:")
            if name=="q":
                break
            if name:
                num=input("(提示：按q返回上一层)请输入新联系方式:")
                phoneTable[name]=num
                print("新建成功")
    if fun=="3":
        while 1:
            name=input("(提示：按q返回上一层)请输入待删除联系人姓名:")
            if name=="q":
                break
            if name in phoneTable:
                phoneTable.pop(name)
                print("删除成功")
            else:
                print("联系人不存在")
    else:
        print("输入有误，请按要求输入！")
