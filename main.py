#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
#
#       main.py
#       
#       Copyright 2011 Christopher Benninger <chris@amok>
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
#       
#       

import sys
from optparse import OptionParser
from scene import Scene
from visual import color,display


def main():
	
	scene = Scene()
	running = True
	showHelp()
	while True:
		sys.stdout.write("#>")
		s = sys.stdin.readline()
		items = s.split()
		
		if(len(items)<1):
			print "Invalid format:"
			showHelp()
			continue
		
		#if(items[0]=="exit"):
		#	myscene = display.get_selected()
		#	myscene.visible=False
		#	myscene.withdraw()
		
		elif(items[0]=="help"):	
			showHelp()
			print ""
			
		elif(items[0]=="add"):
			
			if(len(items)<7):
				print "Invalid format:"
				showHelp()
				continue
			
			newcolor = color.red
			if(items[1]=="red"):
				newcolor = color.red
			elif(items[1]=="green"):
				newcolor = color.green
			elif(items[1]=="yellow"):
				newcolor = color.yellow
			elif(items[1]=="blue"):
				newcolor = color.blue
				
			newrad = int(items[2])
			newcount = int(items[3])
			newscript = str(items[4])
			newinterval = int(items[5])
			newtitle = str(items[6])
		
			#newtail = str(items[6])
			#tail = False
			#if(newtail=="tail"):
			#	tail = True
			
			for i in range(0,newcount):
				scene.addWorker(newcolor,newrad,newscript,newinterval,newtitle)
		
		elif(items[0]=="remove"):
			title=str(items[1])
			
			if(title=="*"):
				scene.removeAllWorkers()
			else:
				scene.removeWorker(title)
			print ""
		
		elif(items[0]=="incr" or items[0]=="decr"):
		
			if(len(items)<4):
				print "Invalid format:"
				showHelp()
				continue
				
			if(items[2]=="x"):
				if(items[1]=="*"):
					if(items[0]=="incr"):
						scene.incAllWorkerMeanX(int(items[3]))
					elif(items[0]=="decr"):	
						scene.incAllWorkerMeanX(-int(items[3]))
				else:
					if(items[0]=="incr"):
						scene.incWorkerMeanX(str(items[1]),int(items[3]))
					elif(items[0]=="decr"):	
						scene.incWorkerMeanX(str(items[1]),-int(items[3]))
				
			elif(items[2]=="y"):
				if(items[1]=="*"):
					if(items[0]=="incr"):
						scene.incAllWorkerMeanY(int(items[3]))
					elif(items[0]=="decr"):	
						scene.incAllWorkerMeanY(-int(items[3]))
				else:
					if(items[0]=="incr"):
						scene.incWorkerMeanY(str(items[1]),int(items[3]))
					elif(items[0]=="decr"):	
						scene.incWorkerMeanY(str(items[1]),-int(items[3]))
				
			elif(items[2]=="z"):	
				if(items[1]=="*"):
					if(items[0]=="incr"):
						scene.incAllWorkerMeanZ(int(items[3]))
					elif(items[0]=="decr"):	
						scene.incAllWorkerMeanZ(-int(items[3]))
				else:
					if(items[0]=="incr"):
						scene.incWorkerMeanZ(str(items[1]),int(items[3]))
					elif(items[0]=="decr"):	
						scene.incWorkerMeanZ(str(items[1]),-int(items[3]))
			
					
				
					
			
		print ""

def showHelp():
	print ""
	print "Py Server Visualizer"
	print "Usage:"
	print "add <color> <radius> <count> <script|norm> <interval> <id|auto>"
	print "remove <id|*>"
	print "<incr|decr> <id|*> <x|y|z> <value>"
	print "help"
	print ""
	
	
	
	
main()
