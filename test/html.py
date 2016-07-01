

# coding = UFT-8
import os, sys
import time
import unittest
import HTMLTestRunner
import xml.etree.cElementTree as ET
import sys
import test 
import media
import wifi
import contact
import photo 
import note 
import video
import app
import phone

class basicTest1(unittest.TestCase):

	def contact(self):
		c = contact.contact()
		c.checkForContacts()
	
	def wifi(self):
		w = wifi.wifi()
		w.wifiTest()

	def note(self):
		n = note.Note()
		n.testNotes()

	def app(self):	
		a= app.app()
		a.apptest()
		
	def photo(self):	
		p = photo.photo()
		p.phototest()
		
	def video(self):	
		v = video.video()
		v.videotest()
		
	def  media(self):	
		m = media.Media()
		m.MediaCheck()
		
	def phone(self):
		p = phone.phone()
		p.phoneTest()
class basicTest2(unittest.TestCase):

	def contact(self):
		c = contact.contact()
		c.checkForContacts()

if __name__ == '__main__':
  
    print 'START'
    testunit=unittest.TestSuite()
    os.popen("adb root")
    os.popen("adb shell service call window 2 i32 4939")
    for i in range(3):
	    
	    testunit.addTest(basicTest1('contact'))
	    testunit.addTest(basicTest1('wifi'))
	    '''testunit.addTest(basicTest('note'))
	    testunit.addTest(basicTest('app'))
	    testunit.addTest(basicTest('photo'))
	    testunit.addTest(basicTest('video'))
	    testunit.addTest(basicTest('media'))
	    testunit.addTest(basicTest('phone'))'''
	    testunit.addTest(basicTest2('contact'))




    filename = '/Users/admin/Desktop/test.html'
    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Sample test', description='test basic function')
    runner.run(testunit)

    






