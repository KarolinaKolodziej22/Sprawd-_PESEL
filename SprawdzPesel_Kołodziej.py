#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:38:03 2022

@author: kkolo
"""
# zadanie 1 gui

import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("Check your Pesel")
window.geometry('200x180')
#window.resizable(0,0)

#responsywnosc
n_rows=2
n_columns=1
for i in range(n_rows):
    window.grid_rowconfigure(i,  weight=1)
for i in range(n_columns):
    window.grid_columnconfigure(i,  weight=1)
    
#zmienna
pesel=StringVar()

#definicja funkcji 
def sprawdz():
    tekst=str(tekst_entry.get())
    if(tekst.isdigit()):
        i=int(tekst[9])
        if (i%2 == 0):
            messagebox.showinfo("Message", "Podany numer PESEL należy do kobiety")
            pesel.set('')
        elif (i%2 !=0):
            messagebox.showinfo("Message", "Podany numer PESEL należy do mężczyzny")
            pesel.set('')
    else:
        messagebox.showinfo("Message", "Wprowadz liczbe!")
        pesel.set('')
        
#dodanie labelu do okna wpisywania
tekst= Label(window, text="Wprowadź swój pesel")
tekst.grid(row=0, column=0)

#dodanie pola wpisu
tekst_entry = Entry(window, textvariable=pesel)
tekst_entry.grid(row=1, column=0)

btn_check= Button(window, text="Check", bg='blue', fg='white', command=sprawdz).grid(row=2, column=0)

window.mainloop()
