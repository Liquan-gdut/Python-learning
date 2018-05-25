import re
import collections

def wordCount(path):
    result= {}
    with open(path) as file_obj:
        data = file_obj.read()
        data = data.lower()
        data = re.sub("\"|,|\.|!|:","",data)
        for word in data.split():
            if word not in result:
                result[word] = 0
            result[word] +=1
        return result

def sort_by_count(d):
    d = collections.OrderedDict(sorted(d.items(),key=lambda t: -t[1]))
    return d
if __name__ == '__main__':
    file_name = "E:\pg2527.txt"
    dword = wordCount(file_name)
    dword = sort_by_count(dword)
    fp =open ('wordCount.txt','w')
    fp.write('单词名称   频数'+'\n')
    for key,value in dword.items():
        fp.write(key +':    '+ str(value)+'\n')