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

