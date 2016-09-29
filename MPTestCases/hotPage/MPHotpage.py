#coding:utf-8
#Edit by liyuanhong 2016/4/12#
import unittest
import Params
from appium import webdriver
from time import sleep

class MPHotpage(unittest.TestCase):
	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		print "************************** MPHotpage test **************************"
		
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
		desired_caps['deviceName']='69T7N15B26001273'

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
		'''��ҳƽ���������
		1������л�����ҳ���еķ���
		'''
		print 'start switch_category_at_shouye_by_click test ...  '
		self.init_case()
		sleep(5)
		ele1 = self.driver.find_elements_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RadioButton') #����׵��ϵ���ҳ
		ele1[0].click()
		sleep(2)
		ele1[1].click()
		sleep(2)
		ele1[2].click()
		sleep(2)
		for i in range(0,12):
			ele1[3].click()
			sleep(2)
		ele1[4].click()
		sleep(2)
		ele1[5].click()
		sleep(2)

	def switch_Opencategory_at_shouye_by_click(self):
		'''��ҳƽ���������
		1������л�����ҳչ����Ƶ������
		'''
		print 'start switch_Opencategory_at_shouye_by_click test ...  '
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
		sleep(1)
		ele = self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
		for i in range(0,14):
			ele[i].click()
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
			sleep(1)
		self.driver.swipe(500, 900, 500, 300) #���ϻ���
		ele = self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
		ele[len(ele) - 1].click()
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
		sleep(1)
		ele[len(ele) - 2].click()
		sleep(1)


	def drag_to_change_category_order(self):
		'''��ҳƽ���������
		1���ı���ҳ�����˳��
		'''
		print 'start drag_to_change_category_order test ...  '
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #���չ��Ƶ������
		sleep(1)
		ele = self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
		for i in range(0,2):
			self.driver.drag_and_drop(ele[2],ele[4])
			sleep(1)
		sleep(2)

		
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
	#suite.addTest(MPHotpage('switch_category_at_shouye_by_click'))
	#suite.addTest(MPHotpage('switch_Opencategory_at_shouye_by_click'))
	suite.addTest(MPHotpage('drag_to_change_category_order'))
	runner = unittest.TextTestRunner()  
	runner.run(suite)