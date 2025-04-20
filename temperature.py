from tkinter import *


screen = Tk()
screen.config(background="white")
screen.geometry("400x600")
screen.title("Temperature Converter")




def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_label = Label(screen, text="Celsius", font=("Arial", 20, 'bold'), bg="white", fg="black")
celsius_label.pack(pady=20)

celsius_entry = Entry(screen, font=("Arial", 20, 'bold'), bg="white", fg="black")
celsius_entry.pack(pady=20)

# farenheit_entry = Entry(screen, font=("Arial", 20, 'bold'), bg="white", fg="black")
# farenheit_entry.pack(pady=20)

result_label = Label(screen, text="", font=("Arial", 20, 'bold'), bg="white", fg="black")
result_label.pack(pady=20)



def convert_temperature():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = celsius_to_fahrenheit(celsius)
        result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        result_label.config(text="Invalid input!")

def farenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

fahrenheit_label = Label(screen, text="Fahrenheit", font=("Arial", 20, 'bold'), bg="white", fg="black")
fahrenheit_label.pack(pady=20)





# def convert_temperature2():
#     try:
#         fahrenheit = float(farenheit_entry.get())
#         celsius = farenheit_to_celsius(fahrenheit)
#         result_label2.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
#     except ValueError:
#         result_label2.config(text="Invalid input!")


# def clear_entries():
#     celsius_entry.delete(0, END)
#     farenheit_entry.delete(0, END)
#     result_label.config(text="")
#     result_label2.config(text="")
# convert_button2 = Button(screen, text="Convert", fg="black", bg="white", font=("Arial", 20, 'bold'), command=convert_temperature2)
# convert_button2.pack(pady=20)


convert_button = Button(screen, text="Convert", fg="black", bg="white", font=("Arial", 20, 'bold'), command=convert_temperature)
convert_button.pack(pady=20)

    





screen.mainloop()