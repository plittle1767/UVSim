"""
The UVSim is a simple virtual machine, but powerful. The UVSim can only interpret a machine language called BasicML.

The UVSim contains CPU, register, and main memory. An accumulator – a register into which information is put before
the UVSim uses it in calculations or examines it in various ways. All the information in the UVSim is handled in
terms of words. A word is a signed four-digit decimal number, such as +1234, -5678. The UVSim is equipped with a
100-word memory, and these words are referenced by their location numbers 00, 01, ..., 99. The BasicML program must
be loaded into the main memory starting at location 00 before executing. Each instruction written in BasicML occupies
one word of the UVSim memory (instruction is signed four-digit decimal number). We shall assume that the sign of a
BasicML instruction is always plus, but the sign of a data word may be either plus or minus. Each location in the
UVSim memory may contain an instruction, a data value used by a program or an unused area of memory. The first two
digits of each BasicML instruction are the operation code specifying the operation to be performed.
"""


class Operations:
    def __init__(self):
        self.file = None
        self.address = 0
        self.registers = {}
        self.accumulator = "+0000"
        self.input_number = None

    def read_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                self.registers[self.address] = line
                self.address += 1

    def set_input(self, input_number):
        self.input_number = input_number

    def get_accumulator(self):
        return self.accumulator

    def get_register(self):
        return self.registers

    def IO_op(self, op, address):
        print("I/O Operation")

    def load_store_op(self, op, address):
        print("load/store operation")
        if op == 20:  # Load
            if address in self.registers:
                self.accumulator = self.registers[address]
                print(f"Loaded from memory: {self.accumulator}")
            else:
                print(f"Error: Attempted to load from an invalid memory address: {address}")
        elif op == 21:  # Store
            self.registers[address] = self.accumulator
            print(f"Stored in memory: {self.accumulator} at address {address}")
        else:
            print("Invalid load/store operation code")

    def arithmetic_op(self, op, address):
        print("Arithmetic operation")

        # Turn the accumulator into an int
        op_code = self.accumulator[1:]
        result = int(op_code)

        # 30 - Add a word from a specific location in memory to the word in the accumulator (leave the result in the
        # accumulator).
        if op == 30:
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
        else:
            print("Invalid arithmetic operation code.")

        result = max(-9999, min(9999, result))
        result_str = "{0:04d}".format(abs(result))
        self.accumulator = ('+' if result >= 0 else '-') + result_str

    def execute(self):
        current_address = 0
        while current_address < len(self.registers):
            current_word = self.registers[current_address]
            op = int(current_word[1:3])
            address = int(current_word[3:])
            if op == 10 or op == 11:
                self.IO_op(op, address)
            elif op == 20 or op == 21:
                self.load_store_op(op, address)
            elif op == 30 or op == 31 or op == 32 or op == 33:
                self.arithmetic_op(op, address)
            elif op == 40:  # Branch
                current_address = address
                print("Branch executed")
            elif op == 41:  # BranchNeg
                self.accumulator = "-1234"  # testing purposes
                if self.accumulator[0] == "-":
                    current_address = address
                    print("BranchNeg executed")
            elif op == 42:  # BranchZero
                self.accumulator = "+0000"  # testing purposes
                if self.accumulator[1:] == "0000":
                    current_address = address
                    print("BranchZero executed")
            elif op == 43:  # Halt
                print("Halt executed")
                break


if __name__ == "__main__":
    operations = Operations()
    operations.read_file('C:\\Users\\Britos\\Documents\\Mydevelopment\\FletProgram\\lala')
    operations.execute()
