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

	return suite