﻿# Python基础知识小结
 
 ### 一、Python概览
#### 1、python程序架构
	模块导入...
	类定义....
	全局函数定义......
	主程序：
      	顶层代码（尽量少，尽量将其封装在类、函数当中）
      	属性/方法调用
#### 2、为什么说python是动态强类型语言？
强类型：虽然不用显示声明数据类型，当python解释器会根据“赋值类型”自动确定数据类型，且在当前只有一个数据类型；
动态：c++等语言，一旦一开始确定其类型，后续的赋值必须按照该类型；python的数据类型可根据赋值类型，一直变化。
#### 3、基本数据类型：string  number  list   tuple   dictionary  sets    
#### 4、常用操作符与内置函数
(1)操作符：“is”、“in”、注意python中没有“++，——”操作符<br>
(2)内置函数：type()、isinstance()、str()、len()、max()、min()、sum()、map()、reduce()；随机函数：random.randint(x，y)、random.choice(x，序列)、random.shuffle()；<br>
 ### 二、序列
#### 1、概述
（1）定义：序列就是一块用来存放多个值的连续内存空间。<br>
（2）列表：包含若干元素的连续、有序、可变的内存空间；元组：包含若干元素的连续、有序、不可变的内存空间（ps：相比于列表，不够灵活但更加安全、访问速度更快）；字典：包含若干元素的连续、无序、可变的内存空间，元素为“键-值”对，键不可重复；<br>
（3）通用操作：查找：index（value）、删除：del（）<br>
#### 2、列表
（1）定义：略<br>
（2）操作：创建：直接创建“[]”，或使用“list（）”，增：a_list.append(x)、a_list.insert(index，value)，扩展：a_list.extend(b_list)，
                     排序：a_list.sort()、删除：a_list.remove()、a_list.pop()，切片：a_list[star,end,步长]，可倒序<br>
#### 3、元组
（1）定义：略<br>
（2）操作：创建：直接创建“()”，或使用“tuple（）”，不可增/改；<br>
#### 4、字典
（1）定义：略<br>
（2）操作：创建：直接创建“{}”，或使用“dict（）”，查找：a_dict[键值]、a_dict.get(键)、a_dict.keys()、a_dict.values()、a_dict.items()，打包创建：dict（zip(keys，values)），keys、values为两个独立列表，zip()将他们一一对应起来；继承扩展：dict.update(b_dict)<br>

 ### 三、字符串
#### 1、本质：不可变序列。
#### 2、常用操作
查找：index（x）、find（“xx”，指定开始位置）；切片：str.split("分隔符")；拼接：str.join(a_list)，将某个字符插入到某列表中，结果返回拼接的字符串；大小写转换：lower（）、upper（）；首字母大写：title()；替换：str.replace（“待替换目标字符”，“字符”）；开头结尾判断：starwith（）、endwith（）；加密：marktrans（）、tanslate（）<br>
 ### 四、函数
#### 1、语法：
    def name（参数）：
          函数体
#### 2、局部与全局变量
局部可以访问全局变量，但无法在局部修改全局变量，返回结果不影响全局变量<br>
#### 3、可变长度参数
（1）*p：自动将传入的多个参数，转换成“元组”<br>
（2）**p：传入参数要以“x=2”格式传入，自动将传入的多个参数，转换成“字典”<br>

 ### 五、面向对象（类）
1、类的定义：属性：私有的通过构造函数，公有直接在类中定义；方法：一般都是公有的，外部可直接访问，私有的则需要通过公有接口进行访问，函数名为“__name()”。<br>

	class name（基类）：         
		公有属性
		构造函数定义私有属性
		方法定义          //注：所有的方法定义都需要传入“self”作为第一个对象参数
#### 2、继承
（1）机制：传入基类 + super(本子类，self)<br>
（2）语法<br>
#### 
    class student（people）：
       def __init__(.....): 
          super(本子类，self).__init__(.....)      //注：super表示调用“父类”的意思，当需要用到父类的代码块时，可通过super调用；
 ### 六、文件操作
#### 1、常用操作
（1）文件打开、读取内容、写入内容、保存关闭文件<br>
####
          fp = open("filename"，“r/w”)
          fp_text = fp.read()
          ........
          fp.write("待写入内容")
          fp.close()
 ### 七、基于UDP的网络编程
#### 1、目的：采用面向无连接的UDP协议，实现客户端与服务器的通信，达到数据传输的目的。
#### 2、过程：<br>
客户端操作结果：<br>
![image](https://github.com/Liquan-gdut/Python-learning/blob/master/clientResult.png)

服务端操作结果：<br>
![image](https://github.com/Liquan-gdut/Python-learning/blob/master/serverResult.png)


 ### python整体小结：
    ①了解python的大致程序架构；
	
    ②理解三种常用序列的本质定义、常用操作，日常算法题基本需要利用到以上常用操作
	
    ③字符串的常用操作、正则表达式
	
    ④基于UDP、TCP的网络编程

 ### 
    ①为什么学Python？
    答：注重解决问题而不拘泥语法，语言简洁可读性好，学习曲线较为平缓，学习过程较为顺畅；课程大纲要求，身边同学都在学，
	有这个学习氛围，也可与老师直接交流；
	
    ②Python案例
    答：词频统计，通讯录，登录验证。
