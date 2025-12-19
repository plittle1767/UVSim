import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


class OperationsError(Exception):
    pass


class Operations:
    def __init__(self, root, console):
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_counter = 0
        self.input_buffer = 0
        self.output_buffer = ""
        self.halted = False
        self.root = root
        self.console = console
        self.stopped = False

    def load_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for i, line in enumerate(file):
                    line = line.strip()
                    if len(line) != 5:
                        raise OperationsError(f"Error on line {i + 1}: Invalid word: {line}")
                    if line[0] not in "+-":
                        raise OperationsError(f"Error on line {i + 1}: Invalid word: {line}")
                    if not line[1:].isdigit():
                        raise OperationsError(f"Error on line {i + 1}: Invalid word: {line}")
                    if i >= 100:
                        raise OperationsError(f"Error: Too many words in the file")
                    self.memory[i] = int(line)
        except FileNotFoundError:
            raise OperationsError("File not found.")

    def execute(self):
        while not self.halted and not self.stopped and 0 <= self.instruction_counter < 100:
            instruction = self.memory[self.instruction_counter]
            opcode, operand = divmod(instruction, 100)
            if opcode == 10:
                self.read_input(operand)
            elif opcode == 11:
                self.write_output(operand)
            elif opcode == 20:
                self.load_accumulator(operand)
            elif opcode == 21:
                self.store_accumulator(operand)
            elif opcode == 30:
                self.add(operand)
            elif opcode == 31:
                self.subtract(operand)
            elif opcode == 32:
                self.divide(operand)
            elif opcode == 33:
                self.multiply(operand)
            elif opcode == 40:
                self.branch(operand)
            elif opcode == 41:
                self.branch_neg(operand)
            elif opcode == 42:
                self.branch_zero(operand)
            elif opcode == 43:
                self.halt()
            else:
                raise OperationsError("Invalid opcode")
            self.instruction_counter += 1
        if self.stopped:
            self.console.insert(tk.END, "Program stopped by user.\n")
        elif self.halted:
            self.console.insert(tk.END, "Program execution completed.\n")
        self.root.update_idletasks()

    def stop(self):
        self.stopped = True

    def restart(self):
        self.stopped = False
        self.halted = False
        self.instruction_counter = 0
        self.accumulator = 0
        self.console.delete('1.0', tk.END)

    def read_input(self, address):
        def close_dlg():
            try:
                value = int(entry.get())
                self.memory[address] = value
                self.console.insert(tk.END, f"Input: {value}\n")
                dialog.destroy()
                self.root.update()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a number.")

        dialog = tk.Toplevel()
        dialog.title("Input Dialog")
        dialog.geometry("200x100")

        label = tk.Label(dialog, text=f"Enter a value for address {address}:")
        label.pack()

        entry = tk.Entry(dialog)
        entry.pack()

        button = tk.Button(dialog, text="OK", command=close_dlg)
        button.pack()

        dialog.transient(self.root)
        dialog.grab_set()
        self.root.wait_window(dialog)

    def write_output(self, address):
        output = self.memory[address]
        self.console.insert(tk.END, f"Output: {output}\n")

    def load_accumulator(self, address):
        self.accumulator = self.memory[address]

    def store_accumulator(self, address):
        self.memory[address] = self.accumulator

    def add(self, address):
        self.accumulator += self.memory[address]

    def subtract(self, address):
        self.accumulator -= self.memory[address]

    def divide(self, address):
        divisor = self.memory[address]
        if divisor == 0:
            raise OperationsError("Division by zero")
        self.accumulator //= divisor

    def multiply(self, address):
        self.accumulator *= self.memory[address]

    def branch(self, address):
        self.instruction_counter = address - 1

    def branch_neg(self, address):
        if self.accumulator < 0:
            self.instruction_counter = address - 1

    def branch_zero(self, address):
        if self.accumulator == 0:
            self.instruction_counter = address - 1

    def halt(self):
        self.halted = True


def select_file():
    filename = filedialog.askopenfilename()
    if filename:
        try:
            operations.load_file(filename)
            operations.execute()
            messagebox.showinfo("Execution Complete", "Program execution completed successfully.")
        except OperationsError as e:
            messagebox.showerror("Error", str(e))


def stop_program():
    operations.stop()


def restart_program():
    operations.restart()
    select_file()


root = tk.Tk()
root.title("UVSim GUI")

console = scrolledtext.ScrolledText(root, width=60, height=15)
console.pack()

operations = Operations(root, console)

load_button = tk.Button(root, text="Load Program", command=select_file)
load_button.pack()

stop_button = tk.Button(root, text="Stop Program", command=stop_program)
stop_button.pack()

restart_button = tk.Button(root, text="Restart Program", command=restart_program)
restart_button.pack()

root.mainloop()
