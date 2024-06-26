from tkinter import *

class Converter:
    def __init__(self):

        # Set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial","16","bold")
                                  )
        self.temp_heading.grid(row=0)

        instruction = "Please enter a temperature below and ""then press one of the buttons to ""convert it from centigrade to fahrenheit."      
        self.temp_instruction = Label(self.temp_frame,
                                       text=instruction, 
                                       wrap=250, width=40,
                                       justify="left")
        self.temp_instruction.grid(row=1)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
