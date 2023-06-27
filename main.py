from tkinter import *
import pyperclip

FONT_NAME = "Courier"
FONT_SIZE = 55

# ---------------------------- Calculate ------------------------------- #
def calculate_func(e):
    input_number = website_entry.get()
    numbers = input_number.split("/")
    if numbers[1] == "-":
        numbers[1] = "0"
    
    result = float(numbers[0]) / 20 + float(numbers[1]) / 240
    result_r = round(result, 5)
    result_label.config(text=result_r)
    pyperclip.copy(result_r)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Shilling to normal number")
window.bind("<Return>", calculate_func)

canvas = Canvas(height=200, width=200)

canvas.create_image(100, 100)
canvas.grid(row=0, column=1)

entry_label = Label(text="Enter number in a format x/x:", font=(FONT_NAME, FONT_SIZE))
entry_label.grid(row=1, column=0)

text_label = Label(text="result:", font=(FONT_NAME, FONT_SIZE))
text_label.grid(row=2, column=0)

website_entry = Entry(width=21, font=(FONT_NAME, FONT_SIZE))
website_entry.grid(row=1, column=1)
website_entry.focus()

calculate_button = Button(text="calculate", width=14, font=(FONT_NAME, 30), command=calculate_func)
calculate_button.grid(row=1, column=2)

result_label = Label(text="X/X", font=(FONT_NAME, FONT_SIZE))
result_label.grid(row=2, column=1, columnspan=1)

window.mainloop()


