#coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import sys
import test

class video(object):
	def __init__(self):
		os.popen('adb shell am start -n com.android.camera2/com.android.camera.CameraLauncher')
		self.element = test.Element()
	def videotest(self):
		print "Enter Camera"
		self.element.waitForElement('resource-id','com.android.camera2:id/video_record_button',"Click to record")
		print "Taking a video"
		time.sleep(3)
		os.popen('adb shell input tap 898 123')
		time.sleep(1)
		self.element.waitForElement('resource-id','com.android.camera2:id/shake_image_view',"Click to see the whole record")
		print "Enter the images"
		os.popen('adb shell input tap 510 380')
		time.sleep(8)
		os.popen('adb shell input tap 898 123')
		print "DELETING THE PHOTO"
		self.element.waitForElement('resource-id','com.android.gallery3d:id/confirm_btn',"Confirm to delete")
		print "Confirm to delete"
		temp = self.element.checkForElement('resource-id','com.android.gallery3d:id/no_image_video')
		assert temp is not False,"Fail to exit"
		os.popen('adb shell input keyevent 3')

if __name__ == '__main__':
	p = video()
	p.videotest()
