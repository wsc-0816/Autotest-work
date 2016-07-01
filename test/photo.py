#coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import sys
import test

class photo(object):
	def __init__(self):
		os.popen('adb shell am start -n com.android.camera2/com.android.camera.CameraLauncher')
		self.element = test.Element()
	def phototest(self):
		print "Enter Camera"
		self.element.waitForElement('resource-id','com.android.camera2:id/photo_capture_button',"Click to take a photo")
		print "Taking a photo"
		time.sleep(5)
		self.element.waitForElement('resource-id','com.android.camera2:id/shake_image_view','Click to see the whole photo')
		print "Enter the images"
		os.popen('adb shell input tap 510 380')
		time.sleep(1)
		os.popen('adb shell input tap 898 123')
		print "DELETING THE PHOTO"
		self.element.waitForElement('resource-id','com.android.gallery3d:id/confirm_btn',"Confirm to delete")
		print "Confirm to delete"
		temp = self.element.checkForElement('resource-id','com.android.gallery3d:id/no_image_video')
		assert temp is True,"Fail to exit"
		print "Delete Successful"
		os.popen('adb shell input keyevent 3')

if __name__ == '__main__':
	p = photo()
	p.phototest()


