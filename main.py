from tkinter import *


def miles_to_km():
    miles = int(input.get())
    km = miles * 1.609
    result_text.config(text = km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=220, height=125)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="Miles")
my_label.grid(column=3, row=0)
my_label.config(padx=5, pady=5)
my_label2 = Label(text='is equal to')
my_label2.grid(column=0, row=1)
my_label3 = Label(text='Km')
my_label3.grid(column=3, row=1)
result_text = Label(text='0')
result_text.grid(column=1, row=1)
result_text.config(padx=5, pady=5)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=3)

input = Entry( width=7)
input.grid(column=1, row=0)









window.mainloop()