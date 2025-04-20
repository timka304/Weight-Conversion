from tkinter import *

screen = Tk()
screen.config(background="white")
screen.geometry("400x600")
screen.title("Weight Converter")

# Dropdown to show choices of the SI Unit user wants to pick for weight conversion

si_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
si_units_var = StringVar(screen)
si_units_var.set(si_units[0])  # Set default value


si_units_label = Label(screen, text="Select SI Unit", font=("Arial", 20, 'bold'), bg="white", fg="black")
si_units_label.pack(pady=20)

si_units_dropdown = OptionMenu(screen, si_units_var, *si_units)
si_units_dropdown.config(font=("Arial", 20, 'bold'), bg="white", fg="black")

si_units_dropdown.pack(pady=20)

# Entry field for the user to enter the weight value
weight_entry = Entry(screen, font=("Arial", 20, 'bold'), bg="white", fg="black")
weight_entry.pack(pady=20)


# Label to show the result of the conversion
result_label = Label(screen, text="", font=("Arial", 20, 'bold'), bg="white", fg="black")
result_label.pack(pady=20)

# Function to convert weight based on the selected SI unit
def convert_weight():
    try:
        weight = float(weight_entry.get())
        unit = si_units_var.get()

        if unit == "Kilograms":
            grams = weight * 1000
            pounds = weight * 2.20462
            ounces = weight * 35.274
            result_label.config(text=f"{weight} kg = {grams:.2f} g, {pounds:.2f} lb, {ounces:.2f} oz")
        elif unit == "Grams":
            kilograms = weight / 1000
            pounds = weight * 0.00220462
            ounces = weight * 0.035274
            result_label.config(text=f"{weight} g = {kilograms:.2f} kg, {pounds:.2f} lb, {ounces:.2f} oz")
        elif unit == "Pounds":
            kilograms = weight / 2.20462
            grams = weight / 0.00220462
            ounces = weight * 16
            result_label.config(text=f"{weight} lb = {kilograms:.2f} kg, {grams:.2f} g, {ounces:.2f} oz")
        elif unit == "Ounces":
            kilograms = weight / 35.274
            grams = weight / 0.035274
            pounds = weight / 16
            result_label.config(text=f"{weight} oz = {kilograms:.2f} kg, {grams:.2f} g, {pounds:.2f} lb")
    except ValueError:
        result_label.config(text="Invalid input!")

# Button to trigger the conversion
convert_button = Button(screen, text="Convert", fg="black", bg="white", font=("Arial", 20, 'bold'), command=convert_weight)
convert_button.pack(pady=20)

# Label to show the conversion result
result_label = Label(screen, text="", font=("Arial", 20, 'bold'), bg="white", fg="black")
result_label.pack(pady=20)


# Function to clear the entries and result label
def clear_entries():
    weight_entry.delete(0, END)
    result_label.config(text="")



screen.mainloop()