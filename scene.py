#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       scene.py
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
import sys
import time
from visual import *
from worker import Worker
#from server import Server
from webserver import WebServer
from scenedefs import SceneDefs


class Scene():
	
	def __init__(self):
		#Scene Vars
		self.scenedefs = SceneDefs(400,400,400)
		self.dims = self.scenedefs.getSceneDimensions()

		self.id = 0
		#Actor Vars
		#self.objList = []
		self.threadList = []

		#Walls
		self.xWall = box(pos=(0,self.dims[1]/2,self.dims[2]/2), size=(0.01,self.dims[0],self.dims[1]), axis=(1,0,0),color=color.blue, opacity=0.07)
		self.yWall = box(pos=(self.dims[0]/2,0,self.dims[2]/2), size=(0.01,self.dims[0],self.dims[2]), axis=(0,1,0),color=color.red, opacity=0.05)
		self.zWall = box(pos=(self.dims[0]/2,self.dims[1]/2,0), size=(0.01,self.dims[1],self.dims[2]), axis=(0,0,1),color=color.green, opacity=0.03)
		
		#self.lamp = local_light(pos=(self.dims[0],self.dims[1],self.dims[2]), color=color.yellow)
		
		self.xAxis = cylinder(pos=(0,0,0), radius=2, axis=(self.dims[0],0,0),color=color.white, opacity=0.3)
		self.yAxis = cylinder(pos=(0,0,0), radius=2, axis=(0,self.dims[0],0),color=color.white, opacity=0.3)
		self.zAxis = cylinder(pos=(0,0,0), radius=2, axis=(0,0,self.dims[0]),color=color.white, opacity=0.3)
		
		self.origin = label(text='0%', pos=(0,0,0),align='center', depth=-0.3, color=color.white,yoffset=-5,box=False,line=True,height=5,opacity=0.1)
		
		self.xAxisText = label(text='Mem', pos=self.xAxis.axis,align='center', depth=-0.3, color=color.blue, yoffset=5, xoffset=10,box=False,line=True,height=7)
		self.xAxis1 = label(text='100%', pos=(self.dims[0],0,0),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),yoffset=-5,box=False,line=True,height=5,opacity=0.1)
		self.xAxis2 = label(text='75%', pos=(self.dims[0]*.75,0,0),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),yoffset=-5,box=False,line=True,height=5,opacity=0.1)
		self.xAxis3 = label(text='50%', pos=(self.dims[0]*.5,0,0),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),yoffset=-5,box=False,line=True,height=5,opacity=0.1)
		self.xAxis4 = label(text='25%', pos=(self.dims[0]*.25,0,0),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),yoffset=-5,box=False,line=True,height=5,opacity=0.1)
		
		self.yAxisText = label(text='CPU', pos=self.yAxis.axis,align='center', depth=-0.3, color=color.red, xoffset=5, yoffset=10,box=False,line=True,height=7)
		self.yAxis1 = label(text='100%', pos=(0,self.dims[0],0),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),xoffset=-5,box=False,line=True,height=5,opacity=0.1)
		self.yAxis2 = label(text='75%', pos=(0,self.dims[0]*.75,0),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),xoffset=-5,box=False,line=True,height=5,opacity=0.1)
		self.yAxis3 = label(text='50%', pos=(0,self.dims[0]*.5,0),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),xoffset=-5,box=False,line=True,height=5,opacity=0.1)
		self.yAxis4 = label(text='25%', pos=(0,self.dims[0]*.25,0),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),xoffset=-5,box=False,line=True,height=5,opacity=0.1)
		
		self.zAxisText = label(text='Disk', pos=self.zAxis.axis,align='center', depth=-0.3, color=color.green, yoffset=5, xoffset=-10,box=False,line=True,height=7)
		self.yAxis1 = label(text='100%', pos=(0,0,self.dims[0]),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),yoffset=-5,box=False,line=True,height=5,opacity=0.1)
		self.yAxis2 = label(text='75%', pos=(0,0,self.dims[0]*.75),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),yoffset=-5,box=False,line=True,height=5,opacity=0.1)
		self.yAxis3 = label(text='50%', pos=(0,0,self.dims[0]*.5),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),yoffset=-5,box=False,line=True,height=5,opacity=0.1)
		self.yAxis4 = label(text='25%', pos=(0,0,self.dims[0]*.25),align='center', depth=-0.3, color=(0.5, 0.5, 0.5),yoffset=-5,box=False,line=True,height=5,opacity=0.1)
				
		#LightSource
		self.window = display.get_selected()
		
	def close(self):
		self.window.destroy()

	def addWorker(self,color,radius,script,interval,title):
		if(title=="auto"):
			title = str(self.id)
			self.id += 1
			
		newws = WebServer(color,radius,self,script,interval,title)
		newws.start()
		self.threadList.append(newws)
	
	def removeAllWorkers(self):
		for item in self.threadList:
			item.shutdown()
			#time.sleep(.5)
		self.threadList = []
	
	def incWorkerMeanX(self,title,x):
		for item in self.threadList:
			if(item.getTitle()==title and item.getWLType()=="norm"):
				item.getWLGen().setXMean(item.getWLGen().getXMean()+x)		
				break

	def incWorkerMeanY(self,title,y):
		for item in self.threadList:
			if(item.getTitle()==title and item.getWLType()=="norm"):
				item.getWLGen().setYMean(item.getWLGen().getYMean()+y)		
				break
	
	def incWorkerMeanZ(self,title,z):
		for item in self.threadList:
			if(item.getTitle()==title and item.getWLType()=="norm"):
				item.getWLGen().setZMean(item.getWLGen().getZMean()+z)		
				break

	def incAllWorkerMeanX(self,x):
		for item in self.threadList:
			if(item.getWLType()=="norm"):
				item.getWLGen().setXMean(item.getWLGen().getXMean()+x)		
			
	def incAllWorkerMeanY(self,y):
		for item in self.threadList:
			if(item.getWLType()=="norm"):
				item.getWLGen().setYMean(item.getWLGen().getYMean()+y)		

	def incAllWorkerMeanZ(self,z):
		for item in self.threadList:
			if(item.getWLType()=="norm"):
				item.getWLGen().setZMean(item.getWLGen().getZMean()+z)		



	def removeWorker(self,title):
		for item in self.threadList:
			if(item.getTitle()==title):
				item.shutdown()
				self.threadList.remove(item)
				break
		return
	
