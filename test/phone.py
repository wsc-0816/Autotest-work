#coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import sys
import test 

class phone(object):
	def __init__(self):
		os.popen('adb shell am start -n com.kinstalk.notepad/.activity.MainActivity')
		os.popen('adb shell input keyevent 3')
		os.popen('adb shell input keyevent 3')
		self.element = test.Element()
		a = self.element.Network()
		assert a is  True,"Network in not valid"
	def phoneTest(self):
		print "Entered contacts"
		self.element.waitForElement("resource-id",'com.kinstalk.cookielauncher:id/center_child',"Prepare to call")
		print "Prepare to type th phone number"
		#os.popen('adb shell input text 10086')
		print "Entered phone number"
		self.element.waitForElement("text",'1')
		self.element.waitForElement("text",'0')
		self.element.waitForElement("text",'0')
		self.element.waitForElement("text",'8')
		self.element.waitForElement("text",'6')
		print "Click to call "
		self.element.waitForElement("resource-id",'com.android.dialer:id/dialpad_floating_action_button_container',"Call")
		time.sleep(7)
		temp = self.element.findElementByName('00:00')
		if temp is  None:
			temp = self.element.findElementByName(u"无法连接到移动网络。")
			assert temp is  None,"Fail to call"
			self.element.waitForElement("resource-id",'com.android.dialer:id/floating_end_call_action_button_container',"Click to end")
		os.popen('adb shell input keyevent 3')




if __name__ == '__main__':
	m = phone()
	m.phoneTest()