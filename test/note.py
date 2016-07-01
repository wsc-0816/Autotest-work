#coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import sys
import test 

class Note(object):
	def __init__(self):
		os.popen('adb shell am start -n com.kinstalk.notepad/.activity.MainActivity')
		element = test.Element()


	def addNotes(self):
		element = test.Element()
		element.waitForElement('resource-id','com.kinstalk.notepad:id/show_top_btn',"Click to write")
		print "Start to write"
		os.popen('adb shell input swipe 500 500 800 800')
		time.sleep(1)
		os.popen('adb shell input swipe 500 500 800 800')
		element.waitForElement('resource-id','com.kinstalk.notepad:id/handwrite_ok',"Click ok")
		print "Click ok"

	def deleteNote(self):
		element = test.Element()
		element.waitForElement('resource-id','com.kinstalk.notepad:id/show_bottom_delete',"Click to delete")
		print "Prepare to delete"
		element.waitForElement('resource-id','com.kinstalk.notepad:id/confirm_sure',"Click to confirm")
		print 'click ok'
	def testNotes(self):
		element = test.Element()
		temp = element.checkForElement('text',u"暂无便签")
		assert temp is True,"Double check the notes"
		self.addNotes()
		temp = element.checkForElement('text',"1/1")
		assert temp is True,"Fail to add new note"
		self.deleteNote()
		temp = element.checkForElement('text',u"暂无便签")
		assert temp is True,"Fail to delete note"
		os.popen('adb shell input keyevent 3')


if __name__ == '__main__':
	n = Note()
	n.testNotes()



