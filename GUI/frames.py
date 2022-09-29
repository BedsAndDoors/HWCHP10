import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.label_one = tkinter.Label(self.topframe, text='John')
        self.label_two = tkinter.Label(self.topframe, text='Jim')
        self.label_three = tkinter.Label(self.topframe, text='Jerry')
 
        self.label_one.pack(side='left')
        self.label_two.pack(side='left')   
        self.label_three.pack(side='left')     
  
        self.label_four = tkinter.Label(self.bottomframe, text='Jill')
        self.label_five = tkinter.Label(self.bottomframe, text='Jen')
        self.label_six = tkinter.Label(self.bottomframe, text='Jessica')
 
        self.label_four.pack(side='left')
        self.label_five.pack(side='left')   
        self.label_six.pack(side='left')

        self.topframe.pack()
        self.bottomframe.pack()

        self.mybutton = tkinter.Button(self.main_window, text='Click Here', command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for Clicking!')

my_gui = myGUI()

print('I am done')