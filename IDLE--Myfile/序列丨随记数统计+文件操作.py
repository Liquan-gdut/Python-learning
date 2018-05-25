import random
from operator import itemgetter

sou_list=[]
for i in range(0,1000):
    sou_list.append(random.randint(0,100))
cout_dic={}
for key in sou_list:
    if key in cout_dic:
        continue
    else:
        cout_dic[key]=sou_list.count(key)
    #if key in cout_dic:
    #    cout_dic[key]=cout_dic[key]+1
    #else:
     #   cout_dic[key]=1
#sort_dic=sorted(cout_dic.items(),key=operator.itemgetter(0))
sort_dic=sorted(cout_dic.items(),key=itemgetter(0))
print("未排序：",cout_dic)
print("已排序：",dict(sort_dic))


#打开文件，可写，写入文件，关闭文件
sort_dic_str=((str(dict(sort_dic)).replace(",","\n")).replace("{"," ")).replace("}"," ")
with open("随机数统计结果.txt","w") as fp:
    fp.write(sort_dic_str)
