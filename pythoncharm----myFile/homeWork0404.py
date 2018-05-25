print("welcome 3115002441")
import time
start = time.clock()
pt = [True] * 1200
res = []
for p in range(2,1200):
    if not pt[p]: continue
    res.append(p)
    for i in range(p*p,1200,p):
        pt[i] = False
file = open('3115002441+LiQuan.txt','a+')
flag = 1
for i in range(1,len(res)):
    if res[i] - res[i-1] == 2:
        list_prime = [res[i-1], res[i]]
        file.write(str(list_prime))
        if flag % 4 ==0:
            file.write('\n')
        flag += 1
print (res[i-1], res[i])
end = time.clock()
file.close()
print("time:%s" % (end - start))