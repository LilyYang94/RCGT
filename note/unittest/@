#coding=utf-8
import unittest
import os,time,datetime
import smtplib
import HTMLTestRunner
import sys
from test_case import *
import allcase_list
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

def sentmail(file_new):
    #发送邮箱
    sender = 'yangyali94@163.com'
    #接收邮箱
    receiver = '522216217@qq.com'
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close

    #发送邮件主题
    subject = 'python autotesting result'
    #发送邮箱服务器
    smtpserver = 'smtp.163.com'
    #发送邮箱用户/密码
    username = 'yangyali94@163.com'
    password = 'Lily1234'
    #中文需参数‘utf-8’,单字节字符不需要
   # msg = MIMEText('Hello!','plain','utf-8')
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #print "****************msg***********"
    #print msg
    #print "*********************END*************"
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = 'Lily<yangyali94@163.com>'
    msg['To'] = '522216217@qq.com'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print 'email has send out !'

    
#查找测试报告,调用发邮件功能
def sendreport():
    result_dir = './report'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"/"+fn) if not
    os.path.isdir(result_dir+"/"+fn) else 0)
    
    print ('最新的文件为: '+lists[-2])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-2])
    print file_new

    #调用发邮件模块
    sentmail(file_new)


#把 test_case 目录添加到 path 下,这里用的相对路径
sys.path.append("\test_case")

listaa = "./test_case/"
def creatsuitel():
    testunit = unittest.TestSuite()
    #discover 方法定义
    discover = unittest.defaultTestLoader.discover(listaa,pattern ='start_*.py', top_level_dir=None)
    #print "****************************"
    #print discover
    #print "#############################"
    #discover 方法筛选出来的用例,循环添加到测试套件中
    for test_suite in discover:
#	print "*******test_suite****************"
#	print test_suite
#	print "****************END*************"
	for test_case in test_suite:
#	    print "*************testCase**********"
#	    print test_case
#	    print "####################END###############"
	    testunit.addTests(test_case)
    print testunit
    return testunit

alltestnames = creatsuitel()

#调用数组文件
#获取数组方法
#alltestnames = allcase_list.caselist()

#创建测试套件
#testunit=unittest.TestSuite()

#将测试用例加入到测试容器(套件)中
#for test in alltestnames:
#    testunit.addTest(unittest.makeSuite(test))
#testunit.addTest(unittest.makeSuite(baidu.Baidu))
#testunit.addTest(unittest.makeSuite(youdao.Youdao))

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)

#取前面时间
now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))

#定义个报告存放路径,支持相对路径。
filename = './report/' + now + '_result2.html'

fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行情况:')

#执行测试用例
#runner.run(testunit)
if __name__ == "__main__":
    runner.run(alltestnames)
    sendreport()
