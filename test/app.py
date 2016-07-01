#coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import sys
import test

class app(object):
	def __init__(self):
		os.popen('adb shell am start -n com.android.settings/.Settings')
		os.popen('adb shell am start -n com.kinstalk.cookielauncher/.CookieLauncher')
		self.element = test.Element()
	def apptest(self):
		print "Enter CookieLauncher"
		evevt = test.Event()
		li =self.element.findElementsByClass("android.widget.FrameLayout")
		for i in range(len(li)):
			evevt.touch(li[i][0],li[i][1])
			print "Enter App"
			temp = self.element.checkForElement('resource-id','com.kinstalk.cookielauncher:id/center_child')
			if (temp == False):
				print "Entered Successful"
				os.popen('adb shell input keyevent 3')
			assert temp is False, "Fail to enter The failed coordinates are %s,%s" %(li[i][0],li[i][1])

if __name__ == '__main__':
	c= app()
	c.apptest()	

