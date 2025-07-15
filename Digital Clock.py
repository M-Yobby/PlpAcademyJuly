from tkinter import*
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.config(bg="black")

label = Label(root, font=('Arial', 50, 'bold'), background= 'black', foreground='cyan')
label.pack(anchor='center')

def time():
    string =strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

time()
root.mainloop()