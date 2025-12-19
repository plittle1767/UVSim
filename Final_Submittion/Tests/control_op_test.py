import unittest
from Tkinter.UVSim import Operations
from Tkinter.UVSim import OperationsError


class ControlOperationTests(unittest.TestCase):
    def setUp(self):
        self.operations = Operations()
        self.operationsError = OperationsError()
        self.operations.registers.clear()

    def test_branch_exec(self):
        """
        Test the program jump to a specific address
        without executing any other store operation after the branch
        """
        self.operations.registers = {0: "+4004", 1: "+2105", 2: "+2105", 3: "+2105", 4: "+4300", 5: "+0000"}
        self.operations.accumulator = "-1111"
        self.operations.execute()
        self.assertEqual(self.operations.registers[5], "+0000")

    def test_branch_to_unknown_addr(self):
        """
        Test the branch operation to an unknown address
        the program should raise an error
        """
        self.operations.registers = {0: "+4010", 1: "+2105", 2: "+2105", 3: "+2105", 4: "+4300", 5: "+0000"}
        with self.assertRaises(OperationsError) as context:
            # self.operations.branch_op(40, 10)
            self.operations.execute()
        self.assertTrue("Invalid memory address: 10" in str(context.exception))

    def test_branchNeg_exec(self):
        """
        Test the program jump to a specific address when the accumulator is negative
        without executing any other store operation after the branch
        """
        self.operations.registers = {0: "+4104", 1: "+2105", 2: "+2105", 3: "+2105", 4: "+4300", 5: "+0000"}
        self.operations.accumulator = "-1111"
        self.operations.execute()
        self.assertEqual(self.operations.registers[5], "+0000")

    def test_branchNeg_positive_accumulator(self):
        """
        Test the branch negative operation with a positive accumulator
        the program should run normally without executing the branch
        """
        self.operations.accumulator = "+1111"
        self.operations.registers = {0: "+4104", 1: "+4104", 2: "+4104", 3: "+2105", 4: "+4300", 5: "+0000"}
        self.operations.execute()
        self.assertEqual(self.operations.registers[5], self.operations.accumulator)

    def test_branchNeg_to_unknown_addr(self):
        """
        Test the branch negative operation to an unknown address
        the program should raise an error
        """
        self.operations.accumulator = "-1111"
        self.operations.registers = {0: "+4110", 1: "+2105", 2: "+2105", 3: "+2105", 4: "+4300", 5: "+0000"}
        with self.assertRaises(OperationsError) as context:
            self.operations.branch_op(41, 10)

        self.assertTrue("Invalid memory address: 10" in str(context.exception))

    def test_branchZero_exec(self):
        """
        Test the program jump to a specific address if the accumulator is "0000"
        without executing any other store operation after the branch
        """
        self.operations.registers = {0: "+4204", 1: "+2105", 2: "+2105", 3: "+2105", 4: "+4300", 5: "-0000"}
        self.operations.accumulator = "+0000"
        self.operations.execute()
        self.assertEqual(self.operations.registers[5], "-0000")

    def test_branchZero_non_zero_accumulator(self):
        """
        Test the branch zero operation with a non-zero accumulator
        the program should run normally without executing the branch
        """
        self.operations.accumulator = "+1111"
        self.operations.registers = {0: "+4204", 1: "+4204", 2: "+4204", 3: "+2105", 4: "+4300", 5: "+0000"}
        self.operations.execute()
        self.assertEqual(self.operations.registers[5], self.operations.accumulator)

    def test_branchZero_to_unknown_addr(self):
        """
        Test the branch zero operation to an unknown address
        the program should raise an error
        """
        self.operations.accumulator = "+0000"
        self.operations.registers = {0: "+4210", 1: "+2105", 2: "+2105", 3: "+2105", 4: "+4300", 5: "+0000"}
        with self.assertRaises(OperationsError) as context:
            self.operations.branch_op(42, 10)

        self.assertTrue("Invalid memory address: 10" in str(context.exception))

    def test_halt_program(self):
        """
        Test the program ends when Halt word is executed
        """
        self.operations.registers = {0: "+4300", 1: "+2102", 2: "+0000"}
        self.operations.execute()
        self.assertEqual(self.operations.registers[2], "+0000")


if __name__ == '__main__':
    unittest.main()
