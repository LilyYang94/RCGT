# coding = utf-8
from selenium import webdriver
browser = webdriver.Firefox()

first_url= 'http://www.baidu.com'
driver.get(first_url)

browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium") #find id and input
browser.find_element_by_id("su").click() #find id and click
browser.quit()
driver.maximize_window()    #将浏览器最大化显示

print "设置浏览器宽480、高800显示"
driver.set_window_size(480, 800)

driver.back() # 回退
driver.forward() # 前进

find_element_by_id()
find_element_by_name()
find_element_by_class_name()
find_element_by_tag_name()
find_element_by_link_text()
find_element_by_partial_link_text()
find_element_by_xpath()
find_element_by_css_selector()

<a href="http://news.baidu.com" name="tj_news">新 闻</a>
<a href="http://tieba.baidu.com" name="tj_tieba">贴 吧</a>
<a href="http://zhidao.baidu.com" name="tj_zhidao">一个很长的文字连接</a>
通过 link text 定位元素:
find_element_by_link_text("新 闻")
find_element_by_link_text("贴 吧")
find_element_by_link_text("一个很长的文字连接")
通 partial link text 也可以定位到上面几个元素:
find_element_by_partial_link_text("新")
find_element_by_partial_link_text("吧")
find_element_by_partial_link_text("一个很长的")

find_element_by_xpath(" /html/body/div[2]/form/span/input ")
'''
xath 缺陷 :1、性能差,定位元素的性能要比其它大多数方式差;2、不够健壮,XPath
会随着页面元素布局的改变而改变;3. 兼容性不好,在不同的浏览器下对 XPath 的实现是不一样的

'''

div[@class='eleclass'] 
div[contains(@class,'eleclass')] #contains 
//a[contains(.,'Issue 1164')]       a:contains(Issue 1164)

CSS 
*                      通用元素选择器,匹配任何元素
E                      标签选择器,匹配所有使用 E 标签的元素
.info                  class 选择器,匹配所有 class 属性中包含 info 的元素
#footer id 选择器,匹配所有 id 属性等于 footer 的元素
E,F                    多元素选择器,同时匹配所有 E 元素或 F 元素, E 和 F 之间用逗号分隔
E F                    后代元素选择器,匹配所有属于 E 元素后代的 F 元素, E 和 F 之间用空格分隔
E>F                    子元素选择器,匹配所有 E 元素的子元素 F
E+F                    毗邻元素选择器,匹配紧随 E 元素之后的同级元素 F (只匹配第一个)
E~F                    同级元素选择器,匹配所有在 E 元素之后的同级 F 元素
E[att='val']           属性 att 的值为 val 的 E 元素 (区分大小写)
E[att^='val']          属性 att 的值以 val 开头的 E 元素 (区分大小写)
E[att$='val']          属性 att 的值以 val 结尾的 E 元素 (区分大小写)       
E[att*='val']          属性 att 的值包含 val 的 E 元素 (区分大小写)
E[att1='v1'][att2*='v2'] 属性 att1 的值为 v1,att2 的值包含 v2 (区分大小写)
E:contains('xxxx')     内容中包含 xxxx 的 E 元素
E:not(s)               匹配不符合当前选择器的任何元素

div#eleid
div.eleclass
div[title=Move mouse here]
div#eleid >*
li:nth(5)
//li[6]                 li:nth(5)
//a[contains(.,'Issue 1164')]             a:contains(Issue 1164)
CSS 定位语法比 XPath 更为简洁,定位方式更多灵活多样;不过对 CSS 理
解起来要比 XPath 较难;但不管是从性能还是定位更复杂的元素上,CSS 优于 XPath,笔者更推荐使用 CSS
定位页面元素。

clear 清除元素的内容,如果可以的话
send_keys 在元素上模拟按键输入
click 单击元素
submit 提交表单

driver.find_element_by_id("user_name").clear()

python 是个容易出现编码问题的语言,有时候当我们在 send_keys()方法中输入中文时,然后脚本在
运行时就报编码错误,这个时候我们可以在脚本开头声明编码为 utf-8,然后在中文字符的前面加个小 u 就
解决了(表示转成 python Unicode 编码)
:
#coding=utf-8
send_keys(u"中文内容")

#返回百度输入的宽高
size=driver.find_element_by_id("kw").size

#返回百度页面底部备案信息
text=driver.find_element_by_id("cp").text

#返回元素的属性值,可以是 id、name、type 或元素拥有的其它任意属性
attribute=driver.find_element_by_id("kw").get_attribute('type')

#返回元素的结果是否可见,返回结果为 True 或 False
result=driver.find_element_by_id("kw").is_displayed()

ActionChains 类鼠标操作的常用方法:
 context_click() 右击
 double_click() 双击
 drag_and_drop() 拖动
 move_to_element() 鼠标悬停在一个元素上
 click_and_hold() 按下鼠标左键在一个元素上



#引入 ActionChains 类ActionChains 用于生成用户的行为;所有的行为都存储在 actionchains 对象。通过 perform()执行
#存储的行为。
from selenium.webdriver.common.action_chains import ActionChains
...
#定位到要双击的元素
double =driver.find_element_by_xpath("xxx")
#对定位到的元素执行鼠标双击操作
# perform 执行所有 ActionChains 中存储的行为。perfrome()同样也是 ActionChains 类提供的的方法,通常与
ActionChains()配合使用。
ActionChains(driver).double_click(double).perform()

drag_and_drop(source, target)
在源元素上按下鼠标左键,然后移动到目标元素上释放。


键盘事件
send_keys(Keys.BACK_SPACE) 删除键(BackSpace)
send_keys(Keys.SPACE)
send_keys(Keys.TAB)
空格键(Space)
制表键(Tab)
send_keys(Keys.ESCAPE)
回退键(Esc)
send_keys(Keys.ENTER) 回车键(Enter)
send_keys(Keys.CONTROL,'a') 全选(Ctrl+A)
send_keys(Keys.CONTROL,'c') 复制(Ctrl+C)
send_keys(Keys.CONTROL,'x') 剪切(Ctrl+X)
send_keys(Keys.CONTROL,'v') 粘贴(Ctrl+V)

#coding=utf-8
from selenium import webdriver
#引入 Keys 类包
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
#删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)
#输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(3)
#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)
#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)
#输入框重新输入内容,搜索
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(3)
#通过回车键盘来代替点击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()

#获得前面 title,打印
title = driver.title
#获得前面 URL,打印
now_url = driver.current_url
sleep():设置固定休眠时间。 python 的 time 包提供了休眠方法 sleep() ,
导入 time 包后就可以使用 sleep()
进行脚本的执行过程进行休眠。
implicitly_wait():是 webdirver 提供的一个超时等待。隐的等待一个元素被发现,或一个命令完成。
如果超出了设置时间的则抛出异常。
WebDriverWait():同样也是 webdirver 提供的方法。在设置时间内,默认每隔一段时间检测一次当前
页面元素是否存在,如果超过设置时间检测不到则抛出异常。

定位一组对象
find_elements 用于获取一组元素。

open html page

from selenium import webdriver
import os
driver = webdriver.Firefox()
file_path =
'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')
#然后从中过滤出 tpye 为 checkbox 的元素,单击勾选
for input in inputs:
if input.get_attribute('type') == 'checkbox':
input.click()
driver.quit()

os 模块为 python 语言标准库中的 os 模块包含普遍的操作系统功能。主要用于操作本地目录文件。
path.abspath()方法用于获取当前路径下的文件


设置等待时间
sleep():设置固定休眠时间。 python 的 time 包提供了休眠方法 sleep() ,
导入 time 包后就可以使用 sleep()
进行脚本的执行过程进行休眠。
implicitly_wait():是 webdirver 提供的一个超时等待。隐的等待一个元素被发现,或一个命令完成。
如果超出了设置时间的则抛出异常。
WebDriverWait():同样也是 webdirver 提供的方法。在设置时间内,默认每隔一段时间检测一次当前
页面元素是否存在,如果超过设置时间检测不到则抛出异常。

定位一组对象
open html page
from selenium import webdriver
import os
driver = webdriver.Firefox()
file_path =
'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)

CSS 
driveriver = webdriver.Firefox()
file_path =
'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
# 选择所有的 type 为 checkbox 的元素并单击勾选
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
checkbox.click()
# 打印当前页面上 type 为 checkbox 的个数
print len(driver.find_elements_by_css_selector('input[type=checkbox]'))
# 把页面上最后1个 checkbox 的勾给去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
driver.quit()

层级定位
#在父亲元件下找到 link 为 Action 的子元素
menu =
driver.find_elem定位 frame 中的对象
在 web 应用中经常会出现 frame 嵌套的应用,假设页面上有 A、B 两个 frame,其中 B 在 A 内,那么
定位 B 中的内容则需要先到 A,然后再到 B。

find_element_by_id('dropdown1').find_element_by_link_text('Another
action')


定位 frame 中的对象
在 web 应用中经常会出现 frame 嵌套的应用,假设页面上有 A、B 两个 frame,其中 B 在 A 内,那么
定位 B 中的内容则需要先到 A,然后再到 B。

下面的代码中 frame.html 里有个 id 为 f1 的 frame,而 f1 中又嵌入了 id 为 f2 的 frame
driver.switch_to_frame("f1")
driver.switch_to_frame("f2")
switch_to_frame 的参数问题。官方说 name 是可以的,但是经过实验发现 id 也可以。所以只要 frame
中 id 和 name,那么处理起来是比较容易的。如果 frame 没有这两个属性的话,你可以直接手动添加。


浏览器多窗口处理
#获得当前窗口
nowhandle=driver.current_window_handle
#打开注册新窗口
driver.find_element_by_name("tj_reg").click()
#获得所有窗口
allhandles=driver.window_handles
#循环判断窗口是否为当前窗口
for handle in allhandles:
if handle != nowhandle:
driver.switch_to_window(handle)
print 'now register window!'
#切换到邮箱注册标签
driver.find_element_by_id("mailRegTab").click()
time.sleep(5)
driver.close()
#回到原先的窗口
driver.switch_to_window(nowhandle)
driver.find_element_by_id("kw").send_keys(u"注册成功!")
time.sleep(3)
driver.quit()

current_window_handle
获得当前窗口句柄
window_handles
返回的所有窗口的句柄到当前会话
switch_to_window()
用于处理多窗口操作的方法,与我们前面学过的 switch_to_frame() 是类似,switch_to_window()用于
处理多窗口之前切换,switch_to_frame() 用于处理多框架的切换。
close()
如果你足够细心会发现我们在关闭“注册页”时用的是 close()方法,而非 quit();close()用于关闭当前
窗口,quit()用于退出驱动程序并关闭所有相关窗口。




alert/confirm/prompt 处理
webdriver 中处理 JavaScript 所生成的 alert、confirm 以及 prompt 是很简单的。具体思路是使用
switch_to.alert()方法定位到 alert/confirm/prompt。然后使用 text/accept/dismiss/send_keys 按需进行操做。
 text 返回 alert/confirm/prompt 中的文字信息。
 accept 点击确认按钮。
 dismiss 点击取消按钮,如果有的话。
 send_keys 输入值,这个 alert\confirm 没有对话框就不能用了,不然会报错。

#获取网页上的警告信息
alert=driver.switch_to_alert()
#接收警告信息
alert.accept()

#得到文本信息并打印
alert = driver.switch_to_alert()
print
alert.text()

#取消对话框(如果有的话)
alert = driver.switch_to_alert()
alert.dismiss()

#输入值(如果有的话)
alert = driver.switch_to_alert()
alert.send_keys(“xxx”)




下拉框处理
#先定位到下拉框
m=driver.find_element_by_id("ShippingMethod")
#再点击下拉框下的选项
m.find_element_by_xpath("//option[@value='10.69']").click()




分页处理
对于 web 页面上的分页功能,我们一般做做以下操作:
 获取总页数
 翻页操作(上一页,下一页)




 上传文件
 #定位上传按钮,添加本地文件
driver.find_element_by_name("file").send_keys('D:\\selenium_use_case\upload
_file.txt')
send_keys()方法除可以输入内容外,也可以跟一个本地的文件路径。从而达
到上传文件的目的。



调用 JavaScript
webdriver 提供了 execute_script() 接口用来调用 js 代码。
#######通过 JS 隐藏选中的元素##########第一种方法:
#隐藏文字信息
driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(5)
#隐藏按钮:
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()',button)




控制浏览器滚动条
可以借助 JavaScript
是来完成操作。
一般用到操作滚动条的会两个场景:
 注册时的法律条文的阅读,判断用户是否阅读完成的标准是:滚动条是否拉到最下方。
 要操作的页面元素不在视觉范围,无法进行操作,需要拖动滚动条
#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)





cookie 处理
webdriver 可以读取、添加和删除 cookie 信息。
webdriver 操作 cookie 的方法有:
 get_cookies()
 get_cookie(name)
获得所有 cookie 信息
返回特定 name 有 cookie 信息

 add_cookie(cookie_dict)
 delete_cookie(name)
 delete_all_cookies()
添加 cookie,必须有 name 和 value 值
删除特定(部分)的 cookie 信息
删除所有 cookie 信息

#向 cookie 的 name 和 value 添加会话信息。
driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
#遍历 cookies 中的 name 和 value 信息打印,当然还有上面添加的信息
for cookie in driver.get_cookies():
print "%s -> %s" % (cookie['name'], cookie['value'])
##### 下面可以通过两种方式删除 cookie #####
# 删除一个特定的 cookie
driver.delete_cookie("CookieName")
# 删除所有 cookie
driver.delete_all_cookies()
time.sleep(2)
driver.close()



获取对象的属性
# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')
#然后循环遍历出 data-node 为594434493的元素,单击勾选
for input in inputs:
if input.get_attribute('data-node') == '594434493':
input.click()





验证码问题
记录 cookie
通过向浏览器中添加 cookie 可以绕过登录的验证码,这是比较有意思的一种解决方案。我们可以在
用户登录之前,通过 add_cookie()方法将用户名密码写入浏览器 cookie ,再次访问系统登录链接将自
动登录。例如下
#访问 xxxx 网站
driver.get("http://www.xxxx.cn/")
#将用户名密码写入浏览器 cookie
driver.add_cookie({'name':'Login_UserNumber', 'value':'username'})
driver.add_cookie({'name':'Login_Passwd', 'value':'password'})
#再次访问 xxxx 网站,将会自动登录
driver.get("http://www.xxxx.cn/")
使用 cookie 进行登录最大的难点是如何获得用户名密码的 name ,如果找到不到 name 的名字,就没
办法向 value 中输用户名、密码信息。
笔者的建议是可以通过 get_cookies()方法来获取登录的所有的 cookie 信息,从而进行找到用户名、
密码的 name 对象的名字;当然,最简单的方法还是询问前端开发人员。




模块化与类库
通用的部分可以寫進模塊（類似於一個函數）
把重复的部分
写成一个公共的模块,需要的时候进行调用,这样就大大提高了我们编写脚本的效率。

login.py
#登录模块
def login():
driver.find_element_by_id("tbUserName").send_keys("username")
driver.find_element_by_id("tbPassword").send_keys("456123")
driver.find_element_by_id("btnLogin").click()

quit.py
#退出模块
def
quit_():

测试用例:
#coding=utf-8
from selenium import webdriver
import login,quit_
#调用登录、退出模块
driver = webdriver.Firefox()
driver.get("http://wwww.xxx.com")
#调用登录模块
login.login()
#其它个性化操作
......
#调用退出模块
quit.quit_()

数据驱动
参数化,输入数据的不同从而引起输出结果的变化

#coding=utf-8
from selenium import webdriver
import time
values=['selenium','webdriver',u'虫师']
# 执行循环
for serch in values:
driver = webdriver.Firefox()
driver.get("http://www.xxxx.com")
driver.find_element_by_id("kw").send_keys(serch)
time.sleep(3)




Python Class
在类的方法中必须有个额外的第
一个参数(self),但在调用类的方法时却不必为这个参数赋值。self 参数所指的是对象本身,所以习惯
性地命名为 self。

数据驱动(参数化)
try :
	print a
except NameError,msg:
	print msg




Try...finally...





Raise 抛出异常

异常名称 描述
BaseException 所有异常的基类
SystemExit 解释器请求退出
KeyboardInterrupt 用户中断执行(通常是输入^C)
Exception 常规错误的基类
StopIteration 迭代器没有更多的值
GeneratorExit 生成器(generator)发生异常来通知退出
StandardError 所有的内建标准异常的基类
ArithmeticError 所有数值计算错误的基类
FloatingPointError 浮点计算错误
OverflowError 数值运算超出最大限制
ZeroDivisionError 除(或取模)零 (所有数据类型)
AssertionError 断言语句失败
AttributeError 对象没有这个属性
EOFError 没有内建输入,到达EOF 标记
EnvironmentError 操作系统错误的基类
IOError 输入/输出操作失败
OSError 操作系统错误
WindowsError 系统调用失败
ImportError 导入模块/对象失败
LookupError 无效数据查询的基类
IndexError 序列中没有此索引(index)
KeyError 映射中没有这个键
MemoryError 内存溢出错误(对于Python 解释器不是致命的)
NameError 未声明/初始化对象 (没有属性)
UnboundLocalError 访问未初始化的本地变量
ReferenceError 弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError 一般的运行时错误
NotImplementedError 尚未实现的方法
SyntaxError Python 语法错误
IndentationError 缩进错误
TabError Tab 和空格混用
SystemError 一般的解释器系统错误
TypeError 对类型无效的操作
ValueError 传入无效的参数
UnicodeError Unicode 相关的错误
UnicodeDecodeError Unicode 解码时的错误
UnicodeEncodeError Unicode 编码时错误
UnicodeTranslateError Unicode 转换时错误
Warning 警告的基类
DeprecationWarning 关于被弃用的特征的警告
FutureWarning 关于构造将来语义会有改变的警告
OverflowWarning 旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning 关于特性将会被废弃的警告
RuntimeWarning 可疑的运行时行为(runtime behavior)的警告
SyntaxWarning 可疑的语法的警告
UserWarning 用户代码生成的警告






weddriver 错误截图
get_screenshot_as_file()函数将截取当前页面的截图保存到指定的位置
#捕捉百度输入框异常
try:
browser.find_element_by_id("kwsss").send_keys("selenium")
browser.find_element_by_id("su").click()
except:
browser.get_screenshot_as_file("/home/fnngj/python/error_png.png")






引入 unittest 单元测试框架

selenium IDE 界面介绍
1---文件(File):创建、打开和保存测试案例和测试案例集。
编辑(Edit):复制、粘贴、删除、撤销和选择测试案例中的所有命令。
Options (设置): 用于设置 seleniunm IDE。
2---用来填写被测网站的地址。
3---速度控制:控制案例的运行速度。
4---运行所有:运行一个测试案例集中的所有案例。
5---运行:运行当前选定的测试案例。
6---暂停/恢复:暂停和恢复测试案例执行。
7---|单步:可以运行一个案例中的一行命令。
8---录制:点击之后,开始记录你对浏览器的操作。
9---案例集列表。
10---测试脚本;table 标签:用表格形式展现命令及参数。source 标签:用原始方式展现,默
认是 HTML 语言格式,也可以用其他语言展示。
11---查看脚本运行通过/失败的个数。
12---当选中前命令对应参数。
13---日志/参考/UI 元素/Rollup
日志:当你运行测试时,错误和信息将会自定显示。
参考:当在表格中输入和编辑 selenese 命令时,面板中会显示对应的参考文档。
UI 元素/Rollup:参考帮助菜单中的,UI-Element Documentation。








unittest 框架

#coding= utf-8
# 将要被测试的类
class Widget:
    def __init__(self, size = (40, 40)):
		self._size = size
    
    def getSize(self):
		return self._size

	def resize(self, width, height):
    	if width < 0 or height < 0:
			raise ValueError, "illegal size"
    	self._size = (width, height)

	def dispose(self):
   		 pass


#coding= utf-8
from widget import Widget
import unittest

# 执行测试的类
class WidgetTestCase(unittest.TestCase):
	def setUp(self):
		self.widget = Widget()

# 测试 getSize()方法的测试用例
	def testSize(self):
		self.assertEqual(self.widget.getSize(), (40, 40))

# 测试 resize()方法的测试用例
	def testResize(self):
		self.widget.resize(100, 100)
		self.assertEqual(self.widget.getSize(), (100, 100))

	def tearDown(self):
		self.widget.dispose()
		self.widget = None

def suite():
	suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize")) #只运行"testSize"开头的方法
    suite.addTest(WidgetTestCase("testResize")) #只运行"testResize"开头的方法
    unittest.makeSuite(WidgetTestCase, "test") #运行所有以"test"开头的方法
    unittest.main() #运行所有以"test"开头的方法
	return suite

在 python 中导入模块一般使用的是 import
__name__,__name__作为模块的内置属性,简单点说呢,就是.py 文件的调用方式。最后是__main__,刚
才我也提过,.py 文件有两种使用方式:作为模块被调用和直接使用。如果它等于"__main__"就表示是直接
执行。
我们在实际的自动化测试用例开发过程中,首先要保证开发的单个用例文件(.py)是运行通过的,如
何跑单个文件上的用例,那么就可以在 if __name__ == “__main__”:后面编写执行用的语句,如上面介绍
的 TextTestRunner()方法来构造测试集,或直接使用 unittest.main()来运行所有用例。
那么一旦这个用例文件(.py)稳定之后,就需要将这个用例文件添加到用例集中,这个用例文件就被
做为一个模块被调用;这个时候 if __name__ == “__main__”:后面的内容将不会被执行。

driver.switch_to_alert().accept()


"""Time """
time.time() 获取当前时间戳
time.localtime() 当前时间的 struct_time 形式
time.ctime() 当前时间的字符串形式
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())




python 中的 package 必须包含一个__init__.py 的文件。





用例的读取

discover 解决用例的读取(用例文件则自动添加到测试套件中)
all_tests.py



自动化测试高级应用

自动发邮件功能
python 的 smtplib 模块提供了一种很方便的途径发送电子邮件。它对 smtp 协议进行了简单的封装。


python 多进程/线程基础
thread.start_new_thread(loop0, ())
start_new_thread()要求一定要有前两个参数。所以,就算我们想要运行的函数不要参数,我们也
要传一个空的元组。




threading 模块
我们应该避免使用 thread 模块,原因是它不支持守护线程。当主线程退出时,所有的子线程不论它
们是否还在工作,都会被强行退出。有时我们并不期望这种行为,这时就引入了守护线程的概念。 threading
模块则支持守护线程。


multiprocessing 模块
target 表示调用对象, args 表示调用对象的位置参数元组。 kwargs 表示调用对象的字典。 Name 为别名。
Group 实质上不使用。
p = Process(target=f, args=('bob',))

