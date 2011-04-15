#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       wsworkgen.py
#       
#       Copyright 2011 Christopher Benninger <chrisbenninger@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#
from scipy import stats
import time
import numpy
import random
from threading import Thread

class WSWorkloadGenerator(Thread):

	def __init__(self, scene, interval):
		Thread.__init__(self)
		self.Xmean = random.randint(20, 80)
		self.Xdev = random.randint(1, 5)
		self.Ymean = random.randint(20, 80)
		self.Ydev = random.randint(1, 5)
		self.Zmean = random.randint(20, 80)
		self.Zdev = random.randint(1, 5)
		
		
		#self.mean = mean
		#self.dev = deviation
		self.running = True
		self.interval = interval
		self.loadValues = [0,0,0]
		self.loadValues[0] = numpy.random.normal(self.Xmean, self.Xdev, (1,1,1))[0]
		self.loadValues[1] = numpy.random.normal(self.Ymean, self.Ydev, (1,1,1))[0]
		self.loadValues[2] = numpy.random.normal(self.Zmean, self.Zdev, (1,1,1))[0]
		#self.loadValues = numpy.random.normal(loc=50, scale=100, size=3)
		#(loc=0.0, scale=1.0, size=None)
		
	def getLoadValue(self):
		return self.loadValues

	def run(self):
		time.sleep(random.randint(0, self.interval))
		while(self.running):
			#print self.Xmean
			self.loadValues[0] = numpy.random.normal(self.Xmean, self.Xdev, (1,1,1))[0]
			self.loadValues[1] = numpy.random.normal(self.Ymean, self.Ydev, (1,1,1))[0]
			self.loadValues[2] = numpy.random.normal(self.Zmean, self.Zdev, (1,1,1))[0]
			time.sleep(self.interval)
	
	def getXMean(self):
		return self.Xmean
	
	def setXMean(self,x):
		self.Xmean = x
	
	def getYMean(self):
		return self.Ymean
	
	def setYMean(self,y):
		self.Ymean = y

	def getZMean(self):
		return self.Zmean
	
	def setZMean(self,z):
		self.Zmean = z

	
	def stop(self):
		self.running = False
