#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       scriptworkgen.py
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
import subprocess as sub
import time
from threading import Thread
import scenedefs

class ScriptWorkloadGenerator(Thread):
	
	def __init__(self, scene, script, interval):
		Thread.__init__(self)
		self.scene = scene
		self.dims = self.scene.scenedefs.getSceneDimensions();
		self.running = True
		self.interval = interval
		#self.p = sub.Popen(script,stdout=sub.PIPE,stderr=sub.PIPE)
		self.p = sub.Popen([script,str(interval)],stdout=sub.PIPE,stderr=sub.PIPE)
		self.output = self.p.stdout
		tmpList = self.output.readline().strip().split(",")
		tmpList = [int(float(tmpList[0])),int(float(tmpList[1])),int(float(tmpList[2]))]
		#tmpList = [tmpList[0]*(self.dims[0]/100),tmpList[1]*(self.dims[1]/100),tmpList[2]*(self.dims[2]/100)]
		self.loadValues = tmpList
		
	def getLoadValue(self):
		return self.loadValues
		
	def run(self):

		#snap = time.time()		
		#tmpList = []
		while(self.running):
			
			line = self.output.readline()
			tmpList = line.strip().split(",")
			#print tmpList
			tmpList = [int(float(tmpList[0])),int(float(tmpList[1])),int(float(tmpList[2]))]
			#tmpList = [tmpList[0],tmpList[1],tmpList[2]]
			#print tmpList
			
			#if(time.time()-snap >= self.interval):
			self.loadValues = tmpList
			#	snap = time.time()
			
		
	def stop(self):
		self.running = False
	
