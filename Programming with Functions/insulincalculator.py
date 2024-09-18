from tkinter import *
import datetime

#used to use certain formulas depending on the time of day
current_time = datetime.datetime.now()
current_hour = int(current_time.strftime('%H'))

class MyWindow:
    def __init__(self, win):

        #This adds labels for the user input
        self.carbLabel=Label(win, text='Carbs')
        self.glucoseLabel=Label(win, text='Glucose')
        self.insulinLabel=Label(win, text='Insulin')

        #this adds text entry boxes
        self.text1=Entry(bd=3)
        self.text2=Entry()
        self.text3=Entry()

        #calculate button
        self.button1 = Button(win, text='Calculate Insulin')

        #defines the placement of items on the window
        self.carbLabel.place(x=100, y=50)
        self.text1.place(x=200, y=50)
        self.glucoseLabel.place(x=100, y=100)
        self.text2.place(x=200, y=100)
        self.calculateButton=Button(win, text='Calculate', command=self.calculate)
        self.calculateButton.place(x=100, y=150)
        self.insulinLabel.place(x=100, y=200)
        self.text3.place(x=200, y=200)

    #calculations and user input
    def calculate(self):
        self.text3.delete(0, 'end')

        #this gets info from the user
        carbs=int(self.text1.get())
        glucose=int(self.text2.get())

        #calculates the insulin according to the ratio
        ratio = 0
        if current_hour <= 11:
            ratio = carbs / 6
        elif (current_hour > 11) and (current_hour <= 15):
            ratio = carbs / 8
        elif current_hour >= 16:
            ratio = carbs / 6

        #calculates the correction 
        correction = 0
        if current_hour <= 14:
            correction = (glucose - 130) / 32
        elif current_hour >= 14:
            correction = (glucose - 130) / 30

        #adds both correction and ratio together
        insulin = round(ratio + correction, 1)

        #prints the insulin calculation in the GUI
        self.text3.insert(END, str(insulin))

#creates the window, name, and dimensions
window=Tk()
mywin=MyWindow(window)
window.title('Insulin Calculator')
window.geometry("400x300+10+10")
window.mainloop()