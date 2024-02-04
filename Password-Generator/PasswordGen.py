                                             ###  CODSOFT INTERNSHIP:-
                                                      ####  PASSWORD-GENERATOR!!!!.....


import tkinter as tk
from tkinter import ttk
import string
import random


class PasswordGeneratorApplication(tk.Tk):
    """
    A simple password generator application using Tkinter.

    Attributes:
        length (tk.IntVar): The length of password.
        result (str): The generated password.
        selectedDifficulty (tk.StringVar): The selected difficulty level.

    Methods:
        __init__(self, master=None):
            Initialize the password generator application.

        createWidgets(self):
            Create the GUI components for the password generator application.

        generate(self):
            Generate a password based on desired complexity and length.
    """

    def __init__(self, master=None):
        """
        Initialize the password generator application.

        Parameters:
            master (tk.Tk): The master Tkinter window.
        """
        tk.Tk.__init__(self, master)
        self.title("Password Generator")
        self.resizable(False, False)
        self.createWidgets()

    def createWidgets(self):
        """
        Create the GUI components for the password generator application.
        """

        self.length = tk.IntVar(value=0)
        self.result = "[To Be Generated]"
        self.selectedDifficulty = tk.StringVar(value="Select an option")

        title_label = tk.Label(self, text="Password Generator", font=("Helvetica", 24))
        title_label.pack(pady=10)

        self.result_label = tk.Label(
            self, text=str(self.result), font=("Helvetica", 20)
        )
        self.result_label.pack(pady=10)

        # Define the options for the dropdown menu
        options = ["Easy", "Medium", "Hard"]

        # Create a dropdown menu
        dropdown_menu = ttk.Combobox(
            self, textvariable=self.selectedDifficulty, values=options, state="readonly"
        )
        dropdown_menu.pack(pady=10)
        dropdown_menu.set("Select an option")  # Set the default value

        pw_len_label = tk.Label(
            self, text="Length of Password", font=("calibre", 10, "bold")
        )
        pw_len = tk.Entry(
            self, textvariable=self.length, font=("calibre", 10, "normal")
        )

        pw_len_label.pack(pady=10)
        pw_len.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(padx=20, pady=20)

        generate_button = tk.Button(
            button_frame, text="Generate Password", command=self.generate
        )
        generate_button.pack(padx=10, pady=10)

    def generate(self):
        """
        Generate a password based on desired complexity and length.
        """

        pw_length = self.length.get()
        difficulty = self.selectedDifficulty.get()

        if difficulty == "Easy" or difficulty == "Select an option":
            characters = string.ascii_lowercase
        elif difficulty == "Medium":
            characters = string.ascii_letters
        elif difficulty == "Hard":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            # Handle unexpected difficulty level
            characters = string.ascii_lowercase

        generated_password = "".join(
            random.choice(characters) for _ in range(pw_length)
        )
        self.result_label.config(text=generated_password)


if __name__ == "__main__":
    app = PasswordGeneratorApplication()
    app.mainloop()