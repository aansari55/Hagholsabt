import tkinter as tk
import pyperclip
import locale
import timeit
import os
import sys

locale.setlocale(locale.LC_ALL, 'fa_IR.UTF-8')  # set locale to Persian/Farsi
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))) # Get the path to the directory containing the script

# Function for formating the UserInput "Number"
def format_number(number):
    persian_digits = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"]
    number_str = locale.format_string("%d", number, grouping=True)
    persian_number_str = ""
    for digit in number_str:
        if digit.isnumeric():
            persian_number_str += persian_digits[int(digit)]
        else:
            persian_number_str += digit
    return persian_number_str

# Function (Main) for calculating the commulative sum under some conditions
def check_number():
    number = int(number_entry.get().replace(',', ''))  # remove commas from input
    result_label.config(text="")
    result = 1600000
    if number > 2000000:
        result += (min(number, 10000000) - 2000000) * 0.4
        if number > 10000000:
            result += (min(number, 50000000) - 10000000) * 0.24
            if number > 50000000:
                result += (min(number, 100000000) - 50000000) * 0.08
                if number > 100000000:
                    result += (min(number, 200000000) - 100000000) * 0.04
                    if number > 200000000:
                        result += (min(number, 500000000) - 200000000) * 0.024
                        if number > 500000000:
                            result += (min(number, 1000000000) - 500000000) * 0.012
                            if number > 1000000000:
                                result += (number - 1000000000) * 0.006
    
    result_formatted = format_number(int(result))
    result_label.config(text=f"حق‌التحریر این سند برابر {result_formatted} ریال است")
    copy_button.config(state=tk.NORMAL)
    pyperclip.copy(result_formatted)

# Functio for Copy2Clipboar Button
def copy_to_clipboard():
    result = result_label.cget("text")
    result = result.split(" ")[-3].strip(".")
    pyperclip.copy(result.replace(',', ''))  # remove commas from result
    copy_button.config(text="کپی شده", state=tk.DISABLED)
    window.after(3000, lambda: copy_button.config(text="کپی کردن", state=tk.NORMAL))

#GUI stuff

# Create the window
window = tk.Tk()
window.geometry("700x250")
window.title("حق‌التحریر دفاتر - اسفند 1401")
window.resizable(False, False)

# Load the logo image
logo = tk.PhotoImage(file=os.path.join(base_path, "./sabt.png"))
# Create the logo label
logo_label = tk.Label(window, image=logo) 
logo_label.pack(side=tk.LEFT, padx=10, pady=10)

# Create the user interface
font = ("Tahoma", 14)

number_label = tk.Label(window, text="مبلغ سند را در کادر زیر وارد کنید (ریال)", font=font)
number_entry = tk.Entry(window, width=20, font=font)
check_button = tk.Button(window, text="محاسبه", font=font, command=check_number)
result_label = tk.Label(window, font=font)
copy_button = tk.Button(window, text="کپی کردن", font=font, state=tk.DISABLED, command=copy_to_clipboard)

number_label.pack(pady=10)
number_entry.pack(pady=10)
check_button.pack(pady=10)
result_label.pack()
copy_button.pack(pady=10)

# Run the program
window.mainloop()