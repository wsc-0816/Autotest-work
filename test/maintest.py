#coding=utf-8

import tempfile
import os
import re
import time
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

class sample(object):
	def runtest(self):
		c = contact.contact()
		c.checkForContacts()
		w = wifi.wifi()
		w.wifiTest()
		n = note.Note()
		n.testNotes()
		a= app.app()
		a.apptest()
		p = photo.photo()
		p.phototest()
		v = video.video()
		v.videotest()
		m = media.Media()
		m.MediaCheck()


if __name__ == '__main__':
	t = sample()
	t.runtest()

