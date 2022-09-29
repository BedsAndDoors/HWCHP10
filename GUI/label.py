import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.label_one = tkinter.Label(self.main_window, text='Hello World')
        self.label_two = tkinter.Label(self.main_window, text='GUI Program')

        self.label_one.pack(side='top')
        self.label_two.pack(side='bottom')     

        tkinter.mainloop()

my_gui = myGUI()

print('I am done')