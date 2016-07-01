#coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import sys
import test


class wifi(object):

	def __init__(self):
		self.wifiName = u'szjy-guest-21'
		self.wifiPassword = '20150906'
		os.popen('adb shell input keyevent 3')
		os.popen('adb shell am start -n com.android.settings/.Settings')
		self.element = test.Element()
		temp = self.element.findElementById('com.android.settings:id/wifi_switch')
		page = 0 
		while  temp is None:
			temp = self.element.findElementById('com.android.settings:id/common_settings')
			if temp is not None:
				page = 2
				break
			temp =  self.element.findElementById('com.android.settings:id/qlove_change_password')
			if temp is not None:
				page = 1
				break
			temp =  self.element.findElementById('com.android.settings:id/bt_search_stereo')
			if temp is not None:
				page = -1
				break
			temp  = self.element.findElementById('com.android.settings:id/restore_settings')
			if temp is not None:
				page = -2
				break
			temp  = self.element.findElementById('com.android.settings:id/device_info_settings')
			if temp is not None:
				page = -3
				break
		if page > 0 :
			for i in range(page):
				self.element.waitForElement('resource-id','com.android.settings:id/right_arrow',"Fine the wifi page")
		elif page < 0 :
			page = abs(page)
			for i in range(page):
				self.element.waitForElement('resource-id','com.android.settings:id/left_arrow',"Fine the wifi page")
				print "Entered page of WIFI"
		'''self.element.waitForElement('resource-id','com.android.settings:id/wlan_settings')
		temp  = self.element.findElementByName(u'无')
		if temp is None :
			self.element.waitForElement('text',self.wifiName)
			self.element.waitForElement('resource-id','com.android.settings:id/wifi_button_forget')
'''
	def wifiTest(self):
		
		print "Prepare to close the WIFI"
		self.element.waitForElement('resource-id','com.android.settings:id/wifi_switch',"Close wifi")
		print "Closed wifi"
		self.element.waitForElement('resource-id','com.android.settings:id/wifi_switch',"reopen the wifi")
		print "reopen the wifi"
		time.sleep(2)
		temp  = self.element.findElementByName(u'已连接 szjy-guest-21')
		if temp is not None:
			print "Connect successful"
		assert temp is not None ,"Fail to reconnect"

if __name__ == '__main__':
	p = wifi()
	p.wifiTest()













			
			