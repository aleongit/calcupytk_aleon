#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Aleix Leon

#imports ______________________________________________
from tkinter import *
import tkinter.font as font
import tkinter.ttk as ttk

#constants ______________________________________________

#classes objecte ______________________________________________
#finestra calculadora (classe)
class Calculadora():
    def __init__(self):

        #objecte tk
        self.arrel = Tk()

        #cadena expressió i StringVar() pels inputs
        self.expression = ""
        self.input_text = StringVar()

        #posicionar
        w = 500 # width for the Tk root
        h = 570 # height for the Tk root

        # get screen width and height
        ws = self.arrel.winfo_screenwidth() # width of the screen
        hs = self.arrel.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        self.arrel.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #finestra mida fixa
        self.arrel.resizable(0, 0)

        #títol
        self.arrel.title("Calculadora by aleon")
        
        #font
        #self.font1 = font.Font(weight='bold')
        #https://www.geeksforgeeks.org/how-to-set-font-for-text-in-tkinter/

        # Creating our text widget.
        #sample_text=tkinter.Text( root, height = 10)
        #sample_text.pack()
        
        # Create an object of type Font from tkinter.
        self.font1 = font.Font( family = "Consolas", 
                                        size = 20, 
                                        weight = "bold")
        
        #frame pantalla
        self.frame_pantalla = Frame(self.arrel, bg = "white", bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 0)
        #self.frame_pantalla.pack(side = TOP)
        self.frame_pantalla.pack(expand=1)
        
        #input pantalla (entry)
        self.input_pantalla = Entry(self.frame_pantalla, width=16, font = ('Consolas', 38, 'bold'), textvariable = self.input_text, bg = "white", bd = 0, justify = RIGHT, state='disabled', disabledbackground="white", disabledforeground="black")
        self.input_pantalla.grid(row = 0, column = 0) #posició en grid
        self.input_pantalla.pack(ipady = 15) #altura

        #frame butons
        self.btns_frame = Frame(self.arrel, bg = "white")
        self.btns_frame.pack()

        #1a filera butons
        self.clear = Button(self.btns_frame, text = "Clean!", font = self.font1, fg = "black", width = 22, height = 2, bd = 0, bg = "#f5f5f6", cursor = "hand2", command = lambda: self.btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
        self.divide = Button(self.btns_frame, text = "/", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#f5f5f6", cursor = "hand2", command = lambda: self.btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
        
        #2a filera butons
        self.seven = Button(self.btns_frame, text = "7", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
        self.eight = Button(self.btns_frame, text = "8", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
        self.nine = Button(self.btns_frame, text = "9", font = self.font1,fg = "black", width = 7, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
        self.multiply = Button(self.btns_frame, text = "*", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#f5f5f6", cursor = "hand2", command = lambda: self.btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

        #3a filera butons
        self.four = Button(self.btns_frame, text = "4", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
        self.five = Button(self.btns_frame, text = "5", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
        self.six = Button(self.btns_frame, text = "6", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
        self.minus = Button(self.btns_frame, text = "-", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#f5f5f6", cursor = "hand2", command = lambda: self.btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

        #4a filera butons
        self.one = Button(self.btns_frame, text = "1", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
        self.two = Button(self.btns_frame, text = "2", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
        self.three = Button(self.btns_frame, text = "3", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
        self.plus = Button(self.btns_frame, text = "+", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#f5f5f6", cursor = "hand2", command = lambda: self.btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

        #5a filera butons
        self.zero = Button(self.btns_frame, text = "0", font = self.font1, fg = "black", width = 14, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
        self.point = Button(self.btns_frame, text = ".", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#f5f5f6", cursor = "hand2", command = lambda: self.btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
        self.equals = Button(self.btns_frame, text = "=", font = self.font1, fg = "black", width = 7, height = 2, bd = 0, bg = "#f5f5f6", cursor = "hand2", command = lambda: self.btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

        #ampliem frame
        self.btns_frame.pack(expand=1)

        #loop finestra activa
        self.arrel.mainloop()
    
    def btn_click(self,item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")

    def btn_equal(self,):
        try:
            result = str(round( eval(self.expression),2) ) 
        except Exception as error:
            result= "* FATAL ERROR *"
        self.input_text.set(result)


#test ______________________________________________________________
#main __________________________________________
#programa  ______________________________________________________________
if __name__ == "__main__":
    app = Calculadora()