# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Blake Murray & Matt Deiss
"""

from tkinter import *
import sys 
import os 
import tkinter
from PIL import Image
from PIL import ImageTk
import Utilities
import csv

class AllTkinterWidgets:
    def __init__(self, master):
        frame = Frame(master, width = 500, height = 400)
        frame.pack(expand=0)
        
        # Menu Creation 
        self.mbar = Frame(frame, relief = 'raised', width = 500, bd = 2)
        self.mbar.pack(expand = 0, fill = X, side = TOP)
        
        # Create Drop Down Measurement Menu
        self.mbutton = Menubutton(self.mbar, text = 'Measurements')
        self.mbutton.pack(side = TOP)
        self.mmenu = Menu(self.mbutton, tearoff = 0)
        self.mbutton['menu'] = self.mmenu
        
        # Populate Measurement Drop Down Menu
        self.mmenu.add('command', label = 'Graph', command = self.graph)
        self.mmenu.add('command', label = 'Max', command = self.maxwin)
        self.mmenu.add('command', label = 'Winner', command = self.getchampions)
        self.mmenu.add('command', label = 'Shooting', command = self.graph2)
        
        # Entry Box Frame 
        self.t = StringVar()
        self.ef = Frame(frame, bd=2, relief='groove')
        self.lb2 = Label(self.ef, text='File:')
        self.lb2.pack(side= LEFT)
        self.entry = Entry(self.ef, textvariable = self.t, bg='white')
        self.bt = Button(self.ef,text = 'Load..', command = self.load) 
        self.entry.pack(side = LEFT, padx = 5)
        self.bt.pack(side = LEFT, padx = 5)
        self.ef.pack(expand = 0,fill = X,pady = 5,side = BOTTOM)
        
        # Listbox Creation
        self.lf = Frame(frame, bd=2, relief='groove')
        self.lb = Label(self.lf, text='Past Events:')
        self.bt1 = Button(self.lf, text = 'Clear', command = self.clear)
        self.listbox = Listbox(self.lf, height=10)
        self.sbl = Scrollbar(self.listbox, orient=VERTICAL)
        self.listbox.configure(yscrollcommand=self.sbl.set)
        self.lb.pack(side=LEFT, padx=5)
        self.bt1.pack(side = BOTTOM)
        self.sbl.pack(side=RIGHT, fill=Y)
        self.listbox.pack(padx=5, fill = X)
        self.lf.pack(expand=0, fill=X, pady=5, before = self.ef, side = BOTTOM)
        self.pf=Frame(frame)
        self.label=Label(self.pf)
        self.pf.pack()
        
        
        # Display Box
        self.db = Frame(frame, bd=2, relief=SUNKEN)
        self.text = Text(self.db, height=10, width =65, wrap = WORD)
        self.text.pack(side=LEFT,padx=5, expand =0)
        self.sb = Scrollbar(self.db, orient=VERTICAL)
        self.sb.pack(side=RIGHT, fill=Y)
        self.db.pack(expand=0, fill=BOTH, pady=10, padx=5, side = BOTTOM, before = self.lf)
        
       
        
        
        
        
        #Function defs
    def clear(self):
          self.label.config(image="")
          self.listbox.delete(0,'end')
    
    
    def graph(self):
        Utilities.getwingraph()
        self.label.config(image = "")
        self.fd = Image.open('ConferenceWinsBar.png')
        self.test = ImageTk.PhotoImage(self.fd)
        self.label = tkinter.Label(root, image=self.test)
        self.label.image = self.test
        self.label.place (x=290, y=300)
        self.listbox.insert(END, "Win data returned")
        
    def maxwin(self):
        Utilities.findthemax()
        self.listbox.insert(END, 'Showing team with the most wins')
        
    def load(self):
          try:
             fd = open(self.t.get())
          except:
             self.listbox.insert(END, 'Error loading file ' + self.t.get())
          lines = fd.read()
          fd.close()
          self.text.insert(END, lines)
          self.listbox.insert(END, 'Loaded file ' + self.t.get())
          
    def getchampions(self):
        Utilities.champions()
        self.listbox.insert(END, 'Showing the Champions from previous seasons')
        
        
    def graph2(self):
        Utilities.getshootinggraph()
        self.label.config(image = "")
        self.fd = Image.open('ShootingLine.png')
        self.test = ImageTk.PhotoImage(self.fd)
        self.label = tkinter.Label(root, image=self.test)
        self.label.image = self.test
        self.label.place (x=290, y=300)
        self.listbox.insert(END, "Shooting data returned")    
        
 
                         
root = Tk()
all = AllTkinterWidgets(root)
root.title('Final Project')
root.pack_propagate(0)
root.mainloop()