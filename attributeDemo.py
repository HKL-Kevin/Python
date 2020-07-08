# -*- coding:utf-8 -*- #
"这是一个关于类属性和成员属性的例子"

class homeMember:
    home = "广东"   #类变量

    def __init__(self,name,age):
        self.name = name    #实列变量
        self.age = age

    def introduce(self):
        print("My name is %s,my age is %d and my home is in %s" % (self.name,self.age,self.home))

mem1 = homeMember("a",24)
mem2 = homeMember("b",22)

mem1.introduce()
mem2.introduce()