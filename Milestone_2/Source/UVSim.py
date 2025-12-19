class OperationsError(Exception):
    pass


class Operations:

    def __init__(self):
        self.file = None
        self.address = 0
        self.registers = {}
        self.accumulator = "+0000"
        self.current_address = 0
        self.current_word = None

    def read_file(self, filename):
        linecount = 0
        self.address = 0
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if len(line) != 5:
                    raise OperationsError(f"Error on line {linecount}: Invalid word: {line}")
                elif line[0] not in "+-":
                    raise OperationsError(f"Error on line {linecount}: Invalid word: {line}")
                elif not line[1:].isdigit():
                    raise OperationsError(f"Error on line {linecount}: Invalid word: {line}")
                if linecount > 99:
                    raise OperationsError(f"Error on line {linecount}: Too many words in the file")
                self.registers[self.address] = line
                self.address += 1
                linecount += 1

    def get_register(self):
        return self.registers

    def get_accumulator(self):
        return self.accumulator

    def get_current_address(self):
        return self.current_address

    def get_current_word(self):
        return self.current_word

    def set_current_address(self, address):
        self.current_address = address

    def set_current_word(self, word):
        self.current_word = word

    def IO_op(self, op, address):
        print("I/O Operation")

        if address in self.registers:
            # Read Operation
            if op == 10:
                retries = 100  # Maximum number of retries for testing purposes
                while retries > 0:
                    user_input = input(
                        f"Enter a '+' or '-' followed by a four-digit value to read into location {address}: ")

                    # Validate input
                    if len(user_input) == 5 and user_input[1:].isdigit() and (
                            user_input[0] == "+" or user_input[0] == "-"):
                        self.registers[address] = user_input
                        print("Value stored")
                        return True  # Input processed successfully

                    print(
                        f"Bad input: Please enter a '+' or '-' followed by a four-digit value to read into location {address}.")
                    retries -= 1

                print("Exceeded maximum number of retries. Aborting input.")
                return False  # Input not processed

            # Write Operation
            elif op == 11:
                print(f"{self.registers[address]}")
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

        result_str = "{0:04d}".format(abs(result))
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
            if self.accumulator[1:] == "0000":
                self.current_address = address
                print("BranchZero executed")
            else:
                self.current_address += 1

    def execute(self):
        self.current_address = 0
        while self.current_address < len(self.registers):
            try:
                self.current_word = self.registers[self.current_address]
                op = int(self.current_word[1:3])
                address = int(self.current_word[3:])
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


if __name__ == "__main__":
    operations = Operations()
    print("Welcome to the UVSim Program!\n")
    file_name = input("Please enter the file path and the file name you would like to load: ")
    try:
        operations.read_file(file_name)
        operations.execute()
    except OperationsError as e:
        print(f"{e}")
