#coding:utf-8
#Edit by liyuanhong 2016/4/12#
import unittest
import Params
from appium import webdriver
from time import sleep

class MPHotpage(unittest.TestCase):
	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		
	def init_case(self):
		#����������Ƿ���ڵ����
		try:
			sleep(1)
			el = self.driver.find_element_by_id('com.yixia.videoeditor:id/adver_imageview')   #��ȡ��������Ƿ����
			self.driver.find_element_by_id('com.yixia.videoeditor:id/textview')    #�����������ϵ�'�������'��ť
			sleep(2)
		except Exception,ex:
			pass
			
	def setUp(self):
		desired_caps={}
		desired_caps['device']='android'
		desired_caps['platformName']='Android'
		desired_caps['browserName']=''
		desired_caps['version']='4.4.2'
		desired_caps['deviceName']='HUAWEI H60-L01'

		#desired_caps['app'] = PATH('D:\\AndroidAutomation\\AndroidAutoTest\\app\\zhongchou.apk')
		#�����Ե�App�ڵ����ϵ�λ��
		desired_caps['appPackage']='com.yixia.videoeditor'
		desired_caps['appActivity']='.ui.login.SplashActivity'
		self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

	def tearDown(self):
		self.driver.quit();
		print 'end ... '
	
	def click_shouye_rebang_faxian_wo(self):
		'''��ť�ĵ������
		1���ֱ�Ե׵��ϵ���ҳ���Ȱ񡢷��֣��ҽ����˵��
		'''
		print 'start click_shouye_rebang_faxian_wo test ...  '
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #����׵��ϵ���ҳ
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_friend').click() #����׵��ϵ��Ȱ�
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_message_tip').click() #����׵��ϵķ���
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #����׵�����
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #����׵��ϵ���ҳ
		sleep(2)
		
	def switch_category_at_shouye_by_click(self):
		'''��ť�ĵ������
		1���л�����ҳ���еķ���
		'''
		print 'start switch_category_at_shouye_by_click test ...  '
		self.init_case()
		sleep(5)
		ele1 = self.driver.find_elements_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RadioButton') #����׵��ϵ���ҳ
		print ele1
		print len(ele1)
		ele1[3].click();
		sleep(5)
		
		
		
	def switch_category_at_shouye_by_slide(self):
		'''�л�����ҳ��
		1�������л�����ҳ���еķ���
		'''
		print 'start switch_category_at_shouye_by_slide test ...  '
		self.init_case()
		sleep(5)
		for i in range(0,20):
			self.driver.swipe(700, 1000, 50, 1000) #���һ���
			sleep(2)
		for i in range(0,20):
			self.driver.swipe(50, 1000, 700, 1000) #���󻬶�
			sleep(2)
	
		
		
		
def suite(self):
	suite = unittest.TestSuite()  
	#suite.addTest(MPHotpage('click_shouye_rebang_faxian_wo'))
	#suite.addTest(MPHotpage('switch_category_at_shouye_by_slide'))
	suite.addTest(MPHotpage('switch_category_at_shouye_by_click'))
	runner = unittest.TextTestRunner()  
	runner.run(suite)