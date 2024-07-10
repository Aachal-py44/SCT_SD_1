import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value

    if from_scale == "C":
        if to_scale == "F":
            return celsius_to_fahrenheit(value)
        elif to_scale == "K":
            return celsius_to_kelvin(value)

    elif from_scale == "F":
        if to_scale == "C":
            return fahrenheit_to_celsius(value)
        elif to_scale == "K":
            return fahrenheit_to_kelvin(value)

    elif from_scale == "K":
        if to_scale == "C":
            return kelvin_to_celsius(value)
        elif to_scale == "F":
            return kelvin_to_fahrenheit(value)

    raise ValueError("Invalid temperature scale. Please use 'C', 'F', or 'K'.")

def on_convert():
    try:
        value = float(entry_value.get())
        from_scale = combo_from_scale.get()
        to_scale = combo_to_scale.get()
        result = convert_temperature(value, from_scale, to_scale)
        label_result.config(text=f"Result: {result:.2f} {to_scale}")
    except ValueError as e:
        label_result.config(text=f"Error: {str(e)}")

# Set up the main application window
root = tk.Tk()
root.title("Temperature Converter")

# Value entry
label_value = tk.Label(root, text="Enter temperature:")
label_value.grid(row=0, column=0, padx=10, pady=10)

entry_value = tk.Entry(root)
entry_value.grid(row=0, column=1, padx=10, pady=10)

# From scale
label_from_scale = tk.Label(root, text="From scale:")
label_from_scale.grid(row=1, column=0, padx=10, pady=10)

combo_from_scale = ttk.Combobox(root, values=["C", "F", "K"])
combo_from_scale.grid(row=1, column=1, padx=10, pady=10)
combo_from_scale.current(0)

# To scale
label_to_scale = tk.Label(root, text="To scale:")
label_to_scale.grid(row=2, column=0, padx=10, pady=10)

combo_to_scale = ttk.Combobox(root, values=["C", "F", "K"])
combo_to_scale.grid(row=2, column=1, padx=10, pady=10)
combo_to_scale.current(1)

# Convert button
button_convert = tk.Button(root, text="Convert", command=on_convert)
button_convert.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()