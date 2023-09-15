import tkinter as tk

def calculate_vat():
    try:
        amount = float(entry_amount.get())
        custom_vat = entry_custom_vat.get()
        if not custom_vat:
            raise ValueError("Custom VAT rate is empty")
        vat_rate = float(custom_vat)
        vat_amount = amount * (vat_rate / 100)
        total_amount = amount + vat_amount
        label_vat_amount.config(text=f"VAT Amount: ${vat_amount:.2f}")
        label_total_amount.config(text=f"Total Amount: ${total_amount:.2f}")
    except ValueError as e:
        label_vat_amount.config(text=f"Error: {e}")
        label_total_amount.config(text="")
    except Exception as e:
        label_vat_amount.config(text=f"An error occurred: {e}")
        label_total_amount.config(text="")

window = tk.Tk()
window.title("VAT Calculator")
window.configure()

label_amount = tk.Label(window, text="Enter Amount ($):")
label_amount.pack()

entry_amount = tk.Entry(window)
entry_amount.pack()

label_custom_vat = tk.Label(window, text="Enter VAT rate (%):")
label_custom_vat.pack()

entry_custom_vat = tk.Entry(window)
entry_custom_vat.pack()

calculate_button = tk.Button(window, text="Calculate VAT", command=calculate_vat, bg='#FF0000')
calculate_button.pack()

label_vat_amount = tk.Label(window, text="")
label_vat_amount.pack()

label_total_amount = tk.Label(window, text="")
label_total_amount.pack()

window.mainloop()
