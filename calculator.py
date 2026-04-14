import tkinter
import customtkinter

def Calculate():
    try:
        price = float(price_var.get())
        discount = float(discount_var.get())

        #calculate discount price
        final_price = price - (price * discount / 100)

        result_label.configure(text=f"Final Price: {final_price:.2f}")
        
    except ValueError:
        result_label.configure(text="Invalid input! Please enter numbers.")

#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Framework
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Discount Calculator")

# Title
title = customtkinter.CTkLabel(app, text="Discount Calculator")
title.pack(padx=10, pady=10)

# Variables
price_var = tkinter.StringVar()
discount_var = tkinter.StringVar()

#Price Input
price_label = customtkinter.CTkLabel(app, text="Enter Price:")
price_label.pack(padx=10, pady=5)

price_entry = customtkinter.CTkEntry(app, textvariable=price_var)
price_entry.pack(padx=10, pady=5)

# Discount Input
discount_label = customtkinter.CTkLabel(app, text="Enter Discount (%):")
discount_label.pack(padx=10, pady=5)

discount_entry = customtkinter.CTkEntry(app, textvariable=discount_var)
discount_entry.pack(padx=10, pady=5)

# Calculate Button
calculate_button = customtkinter.CTkButton(app, text="Calculate", command=Calculate)
calculate_button.pack(padx=10, pady=10)

# Result Label
result_label = customtkinter.CTkLabel(app, text="")
result_label.pack(padx=10, pady=10)

#Run App
app.mainloop()