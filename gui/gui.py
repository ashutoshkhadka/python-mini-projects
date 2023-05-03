from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.config(padx=50, pady=50)


def btn_clicked():
    miles = int(miles_input.get())
    km = round(miles * 1.61, 2)
    km_output_label.config(text=km)


miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_eq_to_label = Label(text="is equal to")
is_eq_to_label.grid(column=0, row=1)

km_label = Label(text="kms")
km_label.grid(column=2, row=1)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

km_output_label = Label()
km_output_label.grid(row=1, column=1)

calc_btn = Button(text="calculate", command=btn_clicked)
calc_btn.grid(column=1, row=2)

window.mainloop()
