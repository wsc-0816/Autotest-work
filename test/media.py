#coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import sys
import test
class Media(object):
	def __init__(self):
		os.popen('adb shell am start -n  com.kinstalk.netvideo/.MainActivity')
		self.element = test.Element()
		a = self.element.Network()
		assert a is  True,"Network in not valid"


	def MediaCheck(self):
		os.popen('adb shell input tap 510 380')
		print "Start playing"
		time.sleep(10)
		os.popen('adb shell input tap 798 173')
		temp = self.element.checkForElement('resource-id','com.kinstalk.netvideo:id/pause_button')
		assert temp is True, "Fail to play"
		time.sleep(5)
		os.popen('adb shell input tap 510 380')
		self.element.waitForElement('resource-id','com.kinstalk.netvideo:id/close_button',"Click to close")
		print 'Click to exit'
		temp = self.element.checkForElement('resource-id','com.kinstalk.netvideo:id/all_category')
		assert temp is False,"Fail to back category"
		print 'Exit Successful'
		os.popen('adb shell input keyevent 3')

if __name__ == '__main__':
	m = Media()
	m.MediaCheck()









		
