import math
import tkinter as tk
from number_entry import IntEntry

def main():
    try:
        # Create the root Tk object.
        app = tk.Tk()

        # Create a HeartWindow object which will call
        # the __init__ function in the CircleWindow class.
        CircleWindow(app)

        # Start the tkinter loop that processes user events
        # such as key presses and mouse button clicks.
        app.mainloop()

    except RuntimeError as run_err:
        print(type(run_err).__name__, run_err, sep=": ")

class CircleWindow(tk.Frame):
    """The main window of this application."""

    def __init__(self, parent):
        """Initialize a Frame object."""

        # Call __init__ in the parent class.
        super().__init__(parent)

        # Create a label that displays "Radius:"
        lblRadius = tk.Label(self, text="Radius:")

        # Create a text field where the user will enter their radius.
        txtRadius = IntEntry(self, 1, 1000, width=5)

        # Create a label that displays "Area:"
        lblRates = tk.Label(self, text="Area:")

        # Create labels that will display the output.
        lblArea = tk.Label(self, width=4)

        # Create the Clear button.
        btnClear = tk.Button(self, text="Clear")

        # Layout all the labels, text fields, and buttons in a grid.
        lblRadius.grid(  row=0, column=0, padx=3, pady=2)
        txtRadius.grid(  row=0, column=1, padx=3, pady=2)
        lblRates.grid(row=0, column=2, padx=(30,3), pady=2)
        lblArea.grid( row=0, column=3, padx=3, pady=2)
        btnClear.grid(row=1, column=0, padx=3, pady=2, columnspan=5, sticky="W")

        self.master.title("Heart Rate")
        self.grid(padx=3, pady=3)


        # This function is called each time the user releases a key.
        def calc(event):
            """Compute and display the user's slowest
            and fastest beneficial heart rates.
            """
            try:
                # Get the user's radius.
                radius = txtRadius.get()

                # Compute the user's area.
                area = round(math.pi * (radius ** 2), 2)

                # Display the area for the user to see
                lblArea.config(text=str(area))

            except ValueError:
                # When the user deletes all the digits in the age
                # text field, clear the slowest and fastest labels.
                lblArea.config(text="")

        # This function is called each time
        # the user presses the "Clear" button.
        def clear():
            """Clear all the inputs and outputs."""
            txtRadius.delete(0, tk.END)
            lblArea.config(text="")
            txtRadius.focus()


        # Bind the calc function to the age text field so
        # that the calc function will be called when the
        # user changes the text in the text field.
        txtRadius.bind("<KeyRelease>", calc)

        # Bind the clear function to the clear button so
        # that the clear function will be called when the
        # user clicks the clear button.
        btnClear.config(command=clear)

        # Give the keyboard focus to the age text field.
        txtRadius.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
