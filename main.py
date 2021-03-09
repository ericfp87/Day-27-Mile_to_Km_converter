from tkinter import *

def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_2 = round(km, 2)
    km_result.config(text=f"{km_2}")

window = Tk()
window.title("Conversor de Milhas para Km")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)

#Label

miles_label =Label(text="Milhas", font=("Arial", 20, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 20, "bold"))
km_label.grid(column=2, row=1)

is_equal_to = Label(text="é igual a", font=("Arial", 15, "bold"))
is_equal_to.grid(column=0, row=1)

km_result = Label(text="0", font=("Arial", 16))
km_result.grid(column=1, row=1)


#Button

calculation_button = Button(text="Calcular", command=button_clicked)
calculation_button.grid(column=1, row=2)

#Entry

miles_input = Entry(width=7, font=("Arial", 16, "bold"))
miles_input.grid(column=1, row=0)

# km_input = Entry(width=7)
# km_input.grid(column=1, row=1)


window.mainloop()