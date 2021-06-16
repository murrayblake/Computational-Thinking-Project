#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:12:39 2021

@author: Blake Murray & Matt Deiss
"""

from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv


  
def getwingraph():
    dataframe = pd.read_csv('cbb20.csv', index_col = 2)
    fig, ax = plt.subplots()
    dataframe = dataframe.sort_values('W', ascending = False)
    ax.bar(dataframe.index, dataframe['W'])
    ax.set_xticklabels(dataframe.index, rotation = 60, horizontalalignment = 'right', fontsize = 12)
    ax.set_title('Number of Wins by Conference', fontsize = 20)
    ax.set_ylabel('# Wins', fontsize = 10)
    ax.set_xlabel('Conference', fontsize = 10)
    plt.savefig('ConferenceWinsBar.png')
    plt.show()
    
def findthemax():
    input_file = csv.DictReader(open('cbb20.csv'))
    max_win = None
    max_team = None
    for row in input_file:
        win = int(row['W'])
        if max_win == None or max_win < win:
            max_win = win
            max_team = row['TEAM']
        
    if max_win != None:
        op = (max_team,max_win)
        output_text = Label(text = op)
        output_text.place(x = 150, y = 300)
    else:
        print('The file does not contain teams')
        
def champions():
    with open('cbb.csv') as file:
        reader = csv.reader(file)
        champ = []
        for row in reader:
            if 'Champions' in row:
                champ.append(row[0]+'-'+row[23]+',')
                pc = champ 
                output_champ = Label(text=pc)
                output_champ.place(x=150, y=360)
                
def getshootinggraph():
    data = np.genfromtxt("cbb20.csv", delimiter=",", names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v"])
    plt.plot(data["a"], data["i"])
    plt.title('Effective Field Goal % Compared to Rank')
    plt.ylabel('Shooting Percentage')
    plt.xlabel('End of Season Rank')
    plt.savefig('ShootingLine.png')
    plt.show()        
    

    

    
        
        
    
    
    
   
    
   
    
   