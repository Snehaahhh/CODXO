import requests
from tkinter import *
from tkinter import ttk, messagebox

# Function to fetch exchange rates with improved error handling
def get_exchange_rate(from_currency, to_currency):
    api_key = "e4fd0df5271b2fc89ea8b6bb"

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

    
    try:
        # Make the API request
        response = requests.get(url)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Check if the API call was successful
        if data['result'] == 'success':
            exchange_rate = data['conversion_rates'].get(to_currency)
            if exchange_rate is None:
                messagebox.showerror("Error", f"Currency '{to_currency}' not found.")
                return None
            return exchange_rate
        else:
            messagebox.showerror("Error", f"API Error: {data['error-type']}")
            return None
        
    except requests.exceptions.HTTPError as http_err:
        messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Error", f"Request failed: {str(e)}")
        return None
    except ValueError as e:
        messagebox.showerror("JSON Error", f"Invalid JSON response: {str(e)}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        return None

# Function to perform currency conversion
def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = amount_var.get()
    
    # Validate amount input
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return
    
    # Get exchange rate
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        result_var.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

# Main window setup
window = Tk()
window.title("Currency Converter")
window.geometry("400x300")
window.configure(bg="#ffffff")

# Title label
title_label = Label(window, text="Currency Converter", font=("Helvetica", 18, "bold"), bg="#ffffff")
title_label.pack(pady=10)

# Frame for input fields
frame = Frame(window, bg="#ffffff")
frame.pack(pady=10)

# Amount entry
amount_label = Label(frame, text="Amount:", font=("Helvetica", 12), bg="#ffffff")
amount_label.grid(row=0, column=0, padx=10, pady=5)
amount_var = StringVar()
amount_entry = Entry(frame, textvariable=amount_var, font=("Helvetica", 12))
amount_entry.grid(row=0, column=1, padx=10, pady=5)

# From currency dropdown
from_currency_label = Label(frame, text="From Currency:", font=("Helvetica", 12), bg="#ffffff")
from_currency_label.grid(row=1, column=0, padx=10, pady=5)
from_currency_var = StringVar()
from_currency_combobox = ttk.Combobox(frame, textvariable=from_currency_var, font=("Helvetica", 12), state="readonly")
from_currency_combobox['values'] = ("USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "CNY")
from_currency_combobox.grid(row=1, column=1, padx=10, pady=5)
from_currency_combobox.current(0)  # Set default value

# To currency dropdown
to_currency_label = Label(frame, text="To Currency:", font=("Helvetica", 12), bg="#ffffff")
to_currency_label.grid(row=2, column=0, padx=10, pady=5)
to_currency_var = StringVar()
to_currency_combobox = ttk.Combobox(frame, textvariable=to_currency_var, font=("Helvetica", 12), state="readonly")
to_currency_combobox['values'] = ("USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "CNY")
to_currency_combobox.grid(row=2, column=1, padx=10, pady=5)
to_currency_combobox.current(1)  # Set default value

# Convert button
convert_button = Button(window, text="Convert", font=("Helvetica", 14, "bold"), command=convert_currency, bg="#4CAF50", fg="#ffffff")
convert_button.pack(pady=20)

# Result label
result_var = StringVar()
result_label = Label(window, textvariable=result_var, font=("Helvetica", 14), bg="#ffffff")
result_label.pack(pady=10)

window.mainloop()
