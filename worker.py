#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       worker.py
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
import time
from visual import *
from threading import Thread
import sys

class Worker(Thread):

	def __init__(self, objcolor, objradius, scene, loadGen, title):
	
		Thread.__init__(self)
		self.scene = scene
		self.title = title
		self.dims = self.scene.scenedefs.getSceneDimensions();
		self.running = False
		self.objRef = sphere(pos=vector(self.dims[0]/2,self.dims[1]/2,self.dims[2]/2), radius=objradius, color=objcolor)
		self.cylXRef = cylinder(pos=self.objRef.pos, radius=.5, axis=(-self.objRef.pos[0],0,0),color=(0.5, 0.5, 0.5), opacity=0.04)
		self.cylYRef = cylinder(pos=self.objRef.pos, radius=.5, axis=(0,-self.objRef.pos[1],0),color=(0.5, 0.5, 0.5), opacity=0.04)
		self.cylZRef = cylinder(pos=self.objRef.pos, radius=.5, axis=(0,0,-self.objRef.pos[2]),color=(0.5, 0.5, 0.5), opacity=0.04)
		self.ringXRef = ring(pos=(0,self.objRef.pos[1],self.objRef.pos[2]),axis=self.objRef.pos, radius=objradius+1,thickness=(.4+(objradius/100)), color=objcolor,opacity=0.25)
		self.ringYRef = ring(pos=(self.objRef.pos[0],0,self.objRef.pos[2]),axis=self.objRef.pos, radius=objradius+1,thickness=(.4+(objradius/100)), color=objcolor,opacity=0.25)
		self.ringZRef = ring(pos=(self.objRef.pos[0],self.objRef.pos[1],0),axis=self.objRef.pos, radius=objradius+1,thickness=(.4+(objradius/100)), color=objcolor,opacity=0.25)
		self.titleLabel = label(space=objradius*2,pos=self.objRef.pos, text=title,xoffset=15,yoffset=10,box=False,line=True,height=8,color=(0.5,0.5,0.5))
		
		self.dt = 0.025
		self.loadGen = loadGen
		self.interval = 0.05
		self.loadGen.start()

	def run(self):
		self.running = True
		
		self.objRef.velocity = vector(0,0,0)
		while(self.running):
			load = self.loadGen.getLoadValue()
			velocity = vector(load[0]*(self.dims[0]/100),load[1]*(self.dims[1]/100),load[2]*(self.dims[2]/100))-self.objRef.pos
			pos = self.objRef.pos + self.objRef.velocity*self.dt
			
			if pos.x > self.dims[0]:
				pos.x = self.dims[0]
			if pos.x < 0:
				pos.x = 0

			if pos.y > self.dims[1]:
				pos.y = self.dims[1]
			if pos.y < 0:
				pos.y = 0
				
			if pos.z > self.dims[2]:
				pos.z = self.dims[2]
			if pos.z < 0:
				pos.z = 0
			
			#Set ball location and velocity
			self.objRef.velocity = velocity
			self.objRef.pos = pos
			
			self.cylXRef.pos = self.objRef.pos
			self.cylXRef.axis = vector(-self.objRef.pos[0],0,0)
			self.ringXRef.pos = vector(0,self.objRef.pos[1],self.objRef.pos[2])
			self.ringXRef.axis = vector(-self.objRef.pos[0],0,0)
			
			self.cylYRef.pos = self.objRef.pos
			self.cylYRef.axis = vector(0,-self.objRef.pos[1],0)
			self.ringYRef.pos = vector(self.objRef.pos[0],0,self.objRef.pos[2])
			self.ringYRef.axis = vector(0,-self.objRef.pos[1],0)
			
			self.cylZRef.pos = self.objRef.pos
			self.cylZRef.axis = vector(0,0,-self.objRef.pos[2])
			self.ringZRef.pos = vector(self.objRef.pos[0],self.objRef.pos[1],0)
			self.ringZRef.axis = vector(0,0,-self.objRef.pos[2])
			
			self.titleLabel.pos = self.objRef.pos
			time.sleep(self.interval)
			

		self.loadGen.stop()
		self.objRef.visible = False
		self.cylXRef.visible = False
		self.cylYRef.visible = False
		self.cylZRef.visible = False
		self.ringXRef.visible = False
		self.ringYRef.visible = False
		self.ringZRef.visible = False
		self.titleLabel.visible = False
		del self.objRef
		del self.cylXRef
		del self.cylYRef
		del self.cylZRef
		del self.ringXRef
		del self.ringYRef
		del self.ringZRef
		del self.titleLabel
		del self.loadGen
		#print "Stopped "+str(self.title)
		

	def shutdown(self):
		self.running = False


