#!/usr/bin/python
#coding=utf-8
import time
f=open('123.txt','a')
now = time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime(time.time()))
f.write('file run time:'+now+'\n')
f.close()