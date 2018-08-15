# encoding: utf-8
import os,datetime,time
result_dir = './report'
lists = os.listdir(result_dir)
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"/"+fn) if not
os.path.isdir(result_dir+"/"+fn) else 0)

#print ("fn value is : " + fn)
print "********list*************"
print lists
print "###########END###############"
print ('最新的文件为: '+lists[-1])
file = os.path.join(result_dir,lists[-1])
print file

