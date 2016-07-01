#coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import sys
import test 
class contact(object):
	"""docstring for contact"""
	def __init__(self):
		os.popen('adb shell am start -n com.kinstalk.remotecontact/.activity.PhoneListActivity')


	def deletContacts(self,id):
		element = test.Element()
		element.waitForElement('resource-id','com.kinstalk.remotecontact:id/item1',"Delete the first contact")
		print "Entered the Contact Page"
		element.waitForElement('class','android.widget.Button',"Click the Edit button")
		print "Entered the Actions Page"
		element.waitForElement('resource-id','com.kinstalk.remotecontact:id/btn_del_from_list',"click the Delete")
		print "Entered the Deleting page"
		os.popen('adb shell input tap 514 515')
		print 'Click OK for deleting'
	def addContacts(self):
		element = test.Element()
		os.popen('adb shell input tap 515 58')
		element.waitForElement("resource-id","com.kinstalk.remotecontact:id/tv_number_1","Click to add")
		print "Typing the number"
		element.waitForElement("resource-id",'com.kinstalk.remotecontact:id/tv_invite',"Next step")
		os.popen('adb shell input swipe 500 500 800 800')
		print "Done with the swipe"
		element.waitForElement("resource-id",'com.kinstalk.remotecontact:id/handwrite_ok',"Click ok")
		print "Click for OK"


	def checkForContacts(self):
		element = test.Element()
		judge = element.checkForElement('resource-id','com.kinstalk.remotecontact:id/item2')
		while(judge):
			self.deletContacts('com.kinstalk.remotecontact:id/item2')
			print "Delete Successful"
			judge = element.checkForElement('resource-id','com.kinstalk.remotecontact:id/item2')
		print "Only one contact exists"
		self.addContacts()
		see = element.checkForElement('resource-id','com.kinstalk.remotecontact:id/item2')
		if (see == True):
			print "Add contact Successful"
		assert see is True, "Fail to add contact"
		self.deletContacts('com.kinstalk.remotecontact:id/item1')
		print "Delete the new contact"
		see = element.checkForElement('resource-id','com.kinstalk.remotecontact:id/item2')
		if (see == True):
			print "Add contact Successful"
		assert see is not True, "Fail to delete contact"

		os.popen('adb shell input keyevent 3')



if __name__ == '__main__':
	c= contact()
	c.checkForContacts()
