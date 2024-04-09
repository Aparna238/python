import tkinter as tk
import logging
from tkinter import messagebox

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='task.log'
                    )

class InvalidInput(Exception):
    def __init__(self,message):
        self.message = message

def validate_input(input):
    words = input.split()
    if len(words) < 3:
        raise InvalidInput("Please enter atleast 3 words")

def process_input():
    try:
        user_input = entry.get()    
        validate_input(user_input)

        logging.info(f"Correct input recieved: {user_input}")
        capitalize_next = True
        processed_output = ''

        for char in user_input:
            if char != ' ': 
                if capitalize_next:
                    processed_output += char.upper()
                else:
                    processed_output += char.lower()
                capitalize_next = not capitalize_next
            else:
                processed_output += char
                
        output_label.config(text=processed_output)
        logging.info(f"Output displayed: {processed_output}")

    except InvalidInput as e:
        logging.error("Wrong input received: Less than 3 words ")
        messagebox.showerror("Error", e.message)

    
window = tk.Tk()

window.title("String processing")

window.geometry("400x200")

instruction_label = tk.Label(window, text="Input string ")
instruction_label.pack()

entry = tk.Entry(window)
entry.pack()

submit_button = tk.Button(window, text="Process Input", command=process_input)
submit_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

logging.debug("Program started")
window.mainloop()
logging.debug("Program ended")
