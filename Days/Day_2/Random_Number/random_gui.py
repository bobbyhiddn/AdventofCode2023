import tkinter as tk
import threading
import time

class CounterApp:
    def __init__(self, root):
        self.minutes = 0
        self.seconds = 0
        self.root = root
        self.root.title("Random Number Generator")

        # Start counter thread
        threading.Thread(target=self.counter_thread, daemon=True).start()

        # Button
        self.button = tk.Button(root, text="Generate Number", command=self.button_pressed)
        self.button.pack()

        # Label for showing result
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.pack()

    def counter_thread(self):
        while True:
            self.seconds += 1
            if self.seconds == 50:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 95:
                    self.minutes = 0
            time.sleep(0.001)  # increment every millisecond

    def format_counter(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

    def perform_operation(self, counter_value, x):
        operation_digit = int(counter_value[3]) % 4
        number_to_operate = int(counter_value[4:])
        # Ensure number_to_operate is never 0 for operations
        if number_to_operate == 0:
            number_to_operate = 1

        result = 0

        if operation_digit == 0:  # integer division
            result = x // number_to_operate
        elif operation_digit == 1:  # multiply
            result = x * number_to_operate
        elif operation_digit == 2:  # add
            result = x + number_to_operate
        elif operation_digit == 3:  # subtract
            result = x - number_to_operate

        # Convert negative result to positive
        result = abs(result)

        return result

    def button_pressed(self):
        result = 0
        while result == 0:
            counter_value = self.format_counter()
            x = int(counter_value[0])  # first digit of minutes
            result = self.perform_operation(counter_value, x)

        self.result_label.config(text=f"Result: {result}")


# Create the main window
root = tk.Tk()
app = CounterApp(root)
root.mainloop()
