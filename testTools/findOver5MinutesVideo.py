#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('gbk')

import urllib
import json
from time import sleep


#����ҳƵ������5���ӵ���Ƶ
def testFenlei():
	categorys = [124,128]
	theMax = 0
	for cat in categorys:
		print "-------------------------------------------------------------"
		for var in range(1,4):
			#��ҳ����
			params = urllib.urlencode({'cateid': cat, 'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20})
			dat = urllib.urlopen("http://api.miaopai.com/m/cate2_channel.json?%s" % params)
			jdat = json.loads(dat.read())
			it = jdat['per']
			for i in range(0,it - 1):
				judge = jdat['result'][i].has_key('color')
				if judge:
					pass
				else:
					theTime = jdat['result'][i]['channel']['ext']['length']
					#print theTime
					if theTime > theMax:
						theMax = theTime
					if theTime >= 300:
						print "channel : " + jdat['name']
						print "ʱ�� : " + str(theTime) + " ��"
						print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
						print "time : " + jdat['result'][i]['channel']['ext']['finishTimeNice']
						print "t : " + jdat['result'][i]['channel']['ext']['t']
						print "ft : " + jdat['result'][i]['channel']['ext']['ft']
						print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
						print "***********************************************"
						print ""
			sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#�����ų���5���ӵ���Ƶ
def testHot():
	theMax = 0
	for var in range(1,10):
		#��ҳ����
		params = urllib.urlencode({'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/v6_hot_channel.json?%s" % params)
		jdat = json.loads(dat.read())
		it = jdat['per']
		for i in range(0,it - 1):
			judge = jdat['result'][i].has_key('color')
			if judge:
				pass
			else:
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "channel : " + "����"
					print "ʱ�� : " + str(theTime) + " ��"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					print "time : " + jdat['result'][i]['channel']['ext']['finishTimeNice']
					print "t : " + jdat['result'][i]['channel']['ext']['t']
					print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


testFenlei()
#testHot()




#http://api.miaopai.com/m/v6_hot_channel.json?token=OIynN5UcxhH082kWvIw7YWP4CTHYSeKI&refresh=3&version=6.6.0.1&page=2&per=20   #���Žӿ�
#http://api.miaopai.com/m/cate2_channel.json?cateid=128&token=OIynN5UcxhH082kWvIw7YWP4CTHYSeKI&version=6.6.0.1&page=1&per=20   #Ƶ���ӿ�