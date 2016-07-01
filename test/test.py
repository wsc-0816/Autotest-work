#coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import sys
class Element(object):
    """
    通过元素定位,需要Android 4.0以上
    """
    def __init__(self):
        """
        初始化，获取系统临时文件存储目录，定义匹配数字模式
        """
        os.popen('adb shell service call window 1 i32 4939')
        self.tempFile = tempfile.gettempdir() 
        self.pattern = re.compile(r"\d+")

    def __uidump(self):
        """
        获取当前Activity控件树
        /data/local/tmp/uidump.xml
        """
        os.popen("adb shell uiautomator dump /data/local/tmp/uidump.xml")
        os.popen("adb pull /data/local/tmp/uidump.xml  "+ self.tempFile[:-1] + "uidump.xml")
    def __element(self, attrib, name):
        """
        同属性单个元素，返回单个坐标元组
        """
        self.__uidump()
        tree = ET.ElementTree(file=self.tempFile[:-1] + "uidump.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])

                return Xpoint, Ypoint


    def __elements(self, attrib, name):
        """
        同属性多个元素，返回坐标元组列表
        """
        list = []
        self.__uidump()
        tree = ET.ElementTree(file=self.tempFile[:-1] + "uidump.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
                if (Xpoint, Ypoint) not in list:
                    list.append((Xpoint, Ypoint))
        return list

    def findElementByName(self, name):
        """
        通过元素名称定位
        usage: findElementByName(u"相机")
        """
        return self.__element("text", name)

    def findElementsByName(self, name):
        return self.__elements("text", name)

    def findElementByClass(self, className):
        """
        通过元素类名定位
        usage: findElementByClass("android.widget.TextView")
        """
        return self.__element("class", className)

    def findElementsByClass(self, className):
        return self.__elements("class", className)

    def findElementById(self, id):
        """
        通过元素的resource-id定位
        usage: findElementsById("com.android.deskclock:id/imageview")
        """
        return self.__element("resource-id",id)

    def findElementsById(self, id):
        return self.__elements("resource-id",id)
    def waitForElement(self,attrib,id,st):
        evevt = Event()
        temp = self.__element(attrib,id)
        if temp is not None:
            evevt.touch(temp[0], temp[1])
            time.sleep(2)
        assert temp is not None, 'Nothing found for the current step: %s' %st 
    def checkForElement(self,attrib,id):
        temp = self.__element(attrib,id)
        if(temp == None):
            return False
        else:
            return True
    def waitForElements(self,attrib,id,st):
        evevt = Event()
        temp = self.__elements(attrib,id)
        if temp is not None:
            for i in range(len(temp)):
                evevt.touch(temp[i][0], temp[i][1])
        assert temp is not None, "Nothing found for current step: %s" %st
    def Network(self):
        process = os.popen('adb shell getprop gsm.network.type') # return file
        output = process.readlines()
        process.close()
        if output[0][:-2] == "Unknown":
            return False
        else:
            return True








class Event(object):
    def __init__(self):
        os.popen("adb wait-for-device ")

    def touch(self, dx, dy):
        """
        触摸事件
        usage: touch(500, 500)
        """
        os.popen("adb shell input tap " + str(dx) + " " + str(dy))
        time.sleep(0.5)

def test():
    element = Element()
    element.waitForElement("resource-id","com.kinstalk.cookielauncher:id/center_child")

    '''evevt = Event()

    e1 = element.findElementById(u"com.kinstalk.cookielauncher:id/center_child")
    evevt.touch(e1[0], e1[1])
    time.sleep(2)

    e2 = element.findElementByName(u"手机充值")
    evevt.touch(e2[0], e2[1])'''

