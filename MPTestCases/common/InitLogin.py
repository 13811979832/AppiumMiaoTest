#coding:utf-8
#Edit by liyuanhong 2016/10/20#

from time import sleep

def init_login(self):
	#����δ��½�����
	sleep(5)
	self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my_lay').click() #����׵��ϵ���
	sleep(2)
	try:
		self.driver.find_element_by_id('com.yixia.videoeditor:id/no_login_views').click() #����ҵ�ҳ�涥���ĸ�����Ϣ��������½�Ի���
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/login_phone_button').click() #����ֻ��ŵ�½
		sleep(2)
		#5�������ֻ���
		e3 = self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview')
		e3.click()  #����ֻ�������򵯳�����
		sleep(0.5)
		e3.send_keys('13699193860')
		sleep(2)
		#5����������
		e3 = self.driver.find_element_by_id('com.yixia.videoeditor:id/password_textview')
		e3.click()  #�����������򵯳�����
		sleep(0.5)
		e3.send_keys('123456')
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click() #�����½
		sleep(2)
		try:
			self.driver.find_element_by_id('com.yixia.videoeditor:id/skip').click() #�ֻ��Ű�ҳ��������
			sleep(2)
		except:
			pass
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #�����ҳ�ص���ҳ
		sleep(2)
	except:
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #��½״̬��ص�����ҳ��
		sleep(2)
		
		
		
		
		