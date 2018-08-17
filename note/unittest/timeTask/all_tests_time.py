#coding=utf-8
import unittest
import HTMLTestRunner
import os ,time

listaa='/home/ada/lily/RCGT/note/unittest/test_case'

def creatsuitel():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(
        listaa,
        pattern ='start_*.py', 
        top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit

alltestnames = creatsuitel()
now = time.strftime('%Y-%m-%M-%H_%M_%S',time.localtime(time.time()))
filename = '/home/ada/lily/RCGT/note/unittest/report/'+now+'timeTaskResult.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况:')


#if __name__ == "__main__":
#    runner.run(alltestnames)

#########控制什么时间脚本执行######
k=1
while k <2:
    timing=time.strftime('%H_%M',time.localtime(time.time()))
    if timing == '16_44':
        print u"开始运行脚本:"
        runner.run(alltestnames)  #执行测试用例
        print u"运行完成退出"
        break
    else:
        time.sleep(5)
        print timing
