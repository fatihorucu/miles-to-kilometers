from tkinter import *
window = Tk()
window.title("Miles to kilometers")
window.config(padx=20, pady=20)
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
entry.grid(column=2, row=0)


def miles_to_kilometer():
    converted_value = float(entry.get())*1.609
    global kilometer_label
    kilometer_label = Label(text="%.2f" % converted_value)
    kilometer_label.grid(column=2, row=2)


miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=1, row=2)
kilometer_label = Label(text="0")
kilometer_label.grid(column=2, row=2)
kilometer_text = Label(text="kilometers")
kilometer_text.grid(column=3, row=2)

button = Button(text="Calculate", command=miles_to_kilometer)
button.grid(column=2, row=3)











window.mainloop()