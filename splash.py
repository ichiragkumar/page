from tkinter import *
import tkinter.font as font


test= Tk()
test.geometry("9500x9500+5+5")
test['bg']='deep sky blue'
labelFont = font.Font(family='Helvitica', size=30)
test_label= Label(test, text= "Electric Shop Management" , fg='blue', font=labelFont)
test_label.pack(pady= 50)
test_label= Label(test, text= "Devloper : PURNIMA SHARMA" , font=labelFont )
test_label.pack(pady= 50)
# test_label= Label(test, text= "Guided by : Amod Kumar singh" , font=labelFont )
# test_label.pack(pady= 50)
test_label.configure(font=("Courier", 25, "italic"))
def main_window():
    test.destroy()
    import num.py
test.after(4000, main_window)
mainloop()