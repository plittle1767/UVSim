from OperationsError import OperationsError
from EventHanlder import EventHandler
import flet as ft


class Operations:
    registers = {}

    def __init__(self, page: ft.Page):
        self.file = None
        self.address = 0
        self.accumulator = "+000000"
        self.current_address = 0
        self.current_word = None
        self.stop_execution_bol = False
        self.output = "000000"
        self.event_handler = EventHandler(page,)
        self.got_input = False
        self.u_input = ""
        self.word_length = 0
        self.op_digits = 0
        self.address_digits = 0

    def check_file(self, filename):
        # Checks entire file to make sure it's not mixed 4-digits and 6-digits
        def check_list(lyst):
            # Helper function to check if all elements of the list are the same
            return len(set(lyst)) == 1

        length_list = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                length_list.append(len(line))
            if check_list(length_list):
                self.word_length = length_list[0]
                print(f"Format Approved. Type: {self.word_length}-digit")
                return
            else:
                raise OperationsError("The file you selected does not have proper format.")

    def read_file(self, filename):
        self.check_file(filename)
        linecount = 0
        self.address = 0
        self.registers.clear()
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if len(line) != 5 and len(line) != 7:   # Accepts both types
                    raise OperationsError(f"Error on line {linecount}: Invalid word: {line}")
                elif line[0] not in "+-":
                    raise OperationsError(f"Error on line {linecount}: Invalid word: {line}")
                elif not line[1:].isdigit():
                    raise OperationsError(f"Error on line {linecount}: Invalid word: {line}")
                if linecount > 249:  # Updated to fit both formats
                    raise OperationsError(f"Error on line {linecount}: Too many words in the file")
                self.registers[self.address] = line
                self.address += 1
                linecount += 1
        while self.address < 250:   # Updated to fit both formats
            self.registers[self.address] = None
            self.address += 1
            linecount += 1
        print("File read successfully")

    def set_got_input(self, got_input):
        self.got_input = got_input

    def set_u_input(self, u_input):
        self.u_input = u_input

    def get_output(self):
        return self.output

    def stop_execution(self):
        self.stop_execution_bol = True

    def IO_op(self, op, address):
        print("I/O Operation")

        if address in self.registers:
            # Read Operation
            if op == 10:
                retries = 10  # Maximum number of retries for testing purposes
                while retries > 0:
                    # user_input = input(f"Enter a four-digit value to read into location {address}: ")
                    user_input = self.event_handler.get_user_input()
                    # while not self.got_input:
                    #     pass
                    # self.got_input = False
                    # user_input = self.u_input

                    # Add plus sign to positive values
                    if user_input[0] != "-" and user_input[0] != "+":
                        user_input = "+" + user_input
                    # Validate input
                    if user_input[1:].isdigit() and (
                            user_input[0] == "+" or user_input[0] == "-"):
                        self.registers[address] = user_input
                        print("Value stored")
                        return  # Input processed successfully

                    print(f"Bad input: Please enter a four-digit value to read into location {address}.")
                    retries -= 1

                print("Exceeded maximum number of retries. Aborting input.")
                raise OperationsError(f"Exceeded maximum number of retries. Aborting input.") # Input not processed

            # Write Operation
            elif op == 11:
                self.output = self.registers[address]
                self.event_handler.display_output(self.output)
                print(f"print value {self.registers[address]}")
        else:
            raise OperationsError(f"Error: Address {address} not found in registers.")

    def load_store_op(self, op, address):
        print("Load/Store operation")

        # First check if address is in memory
        if address not in self.registers:
            raise OperationsError(f"Error: Invalid memory address: {address}")

        elif op == 20:  # Load
            self.accumulator = self.registers[address]
            print(f"Loaded from memory: {self.accumulator}")

        elif op == 21:  # Store
            self.registers[address] = self.accumulator
            print(f"Stored in memory: {self.accumulator} at address {address}")

    def arithmetic_op(self, op, address):
        print("Arithmetic operation")

        # Turn the accumulator into an int
        op_code = self.accumulator[1:]
        result = int(op_code)

        # First check if address is in memory
        if address not in self.registers:
            raise OperationsError(f"Error: Invalid memory address: {address}")

        # 30 - Add a word from a specific location in memory to the word in the accumulator (leave the result in the
        # accumulator).
        elif op == 30:
            result += int(self.registers[address])

        # 31 - Subtract a word from a specific location in memory from the word in the accumulator (leave the result in
        # the accumulator).
        elif op == 31:
            result -= int(self.registers[address])

        # 32 - Divide the word in the accumulator by a word from a specific location in memory (leave the result in the
        # accumulator).
        elif op == 32:
            result //= int(self.registers[address])

        # 33 - Multiply a word from a specific location in memory to the word in the accumulator (leave the result in
        # the accumulator).
        elif op == 33:
            result *= int(self.registers[address])

        result = max(-999999, min(999999, result))  # Updated to fit both formats
        result_str = "{0:06d}".format(abs(result))  # Updated to fit both formats
        self.accumulator = ('+' if result >= 0 else '-') + result_str

    def branch_op(self, op, address):
        # First check if address is in memory
        if address not in self.registers:
            raise OperationsError(f"Error: Invalid memory address: {address}")
        elif op == 40:
            self.current_address = address
            print("Branch executed")
        elif op == 41:
            if self.accumulator[0] == "-":
                self.current_address = address
                print("BranchNeg executed")
            else:
                self.current_address += 1
        elif op == 42:
            if self.accumulator[1:] == "000000":    # Updated to fit both formats
                self.current_address = address
                print("BranchZero executed")
            else:
                self.current_address += 1

    def execute(self):
        self.current_address = 0
        while self.current_address < len(self.registers):
            try:
                if self.stop_execution_bol:
                    print("Program execution stopped")
                    self.stop_execution_bol = False
                    break
                self.current_word = self.registers[self.current_address]

                # Differentiate between word_length type at execution
                if self.word_length == 5:
                    self.op_digits = int(self.current_word[1:3])
                    self.address_digits = int(self.current_word[3:])
                elif self.word_length == 7:
                    self.op_digits = int(self.current_word[2:4])
                    self.address_digits = int(self.current_word[4:])

                op = self.op_digits
                address = self.address_digits

                if op == 10 or op == 11:
                    self.IO_op(op, address)
                    self.current_address += 1
                elif op == 20 or op == 21:
                    self.load_store_op(op, address)
                    self.current_address += 1
                elif op == 30 or op == 31 or op == 32 or op == 33:
                    self.arithmetic_op(op, address)
                    self.current_address += 1
                elif op == 40 or op == 41 or op == 42:
                    self.branch_op(op, address)
                elif op == 43:  # Halt
                    print("Halt executed")
                    break
                else:
                    self.current_address += 1
            except OperationsError as e:
                raise OperationsError(f"{e}")
        print("Program execution complete")

# if __name__ == "__main__":
#     operations = Operations()
#     print("Welcome to the UVSim Program!\n")
#     file_name = input("Please enter the file path and the file name you would like to load: ")
#     try:
#         operations.read_file(file_name)
#         operations.execute()
#     except OperationsError as e:
#         print(f"{e}")
