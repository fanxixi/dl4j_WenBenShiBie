# Author:fanxixi
# -*- coding:utf-8 -*-
#用这个来添加标注
#file = open('neg2.txt','r',encoding = 'utf-8')
file = open('post1.txt','r',encoding = 'utf-8')
lines = file.readlines()
file.close()
#file = open('neg3.txt','w',encoding = 'utf-8')
file = open('post3.txt','w',encoding = 'utf-8')
for words in lines:
    file.write("正面 " + words)
file.close()