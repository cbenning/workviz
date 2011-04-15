#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       webserver.py
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
from worker import Worker
from wsworkgen import WSWorkloadGenerator
from scriptworkgen import ScriptWorkloadGenerator

class WebServer(Worker):

	def __init__(self, objcolor, objradius, scene, script, interval, title):
		
		self.title = title
		self.wltype = script
		
		if(script=="norm"):
			self.loadGen = WSWorkloadGenerator(scene, interval)
		else:
			self.loadGen = ScriptWorkloadGenerator(scene,script, interval)
			
		Worker.__init__(self, objcolor, objradius, scene, self.loadGen,title)

	def getWLType(self):
		return self.wltype

	def getWLGen(self):
		return self.loadGen

	def getTitle(self):
		return self.title
