import tkinter as tk
import logging
from tkinter import messagebox
import argparse

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

def process_input(user_input):
    try:  
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
                
        print("Modified string: ",processed_output)
        logging.info(f"Output displayed: {processed_output}")

    except InvalidInput as e:
        logging.error("Wrong input received: Less than 3 words ")
        print("Error!! Wrong input - less than 3 words")

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i')
    args = parser.parse_args()

    if args.input and args.output:
        logging.debug("Input via command line")
        process_input(args.input)
