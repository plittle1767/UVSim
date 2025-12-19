from Tkinter.UVSim import Operations
from Tkinter.UVSim import OperationsError
import unittest


class TestOperations(unittest.TestCase):

    def setUp(self):
        self.operations = Operations()

    def test_load_operation(self):
        # Prepare test data
        test_address = 1
        test_word = "+1234"
        self.operations.registers[test_address] = test_word

        # Perform the load operation
        self.operations.load_store_op(20, test_address)

        # Check if the accumulator contains the expected word
        self.assertEqual(self.operations.accumulator, test_word)

    def test_store_operation(self):
        # Prepare test data
        test_address = 2
        test_word = "-5678"
        self.operations.registers[test_address] = test_word
        self.operations.accumulator = test_word

        # Perform the store operation
        self.operations.load_store_op(21, test_address)

        # Check if the memory at the specified address contains the expected word
        self.assertEqual(self.operations.registers[test_address], test_word)

    def test_invalid_address(self):
        # Attempt to load and store from an invalid address
        self.operations.registers = {0: "+4010", 1: "+2105", 2: "+2105", 3: "+2105", 4: "+4300", 5: "+0000"}
        # Test load
        with self.assertRaises(OperationsError) as context:
            self.operations.load_store_op(20, 7)
        self.assertTrue("Invalid memory address: 7" in str(context.exception))
        # Test store
        with self.assertRaises(OperationsError) as context:
            self.operations.load_store_op(21, 7)
        self.assertTrue("Invalid memory address: 7" in str(context.exception))

    def test_load_store_op(self):
        # Test the load operation
        test_address_load = 1
        test_word_load = "+9876"
        self.operations.registers[test_address_load] = test_word_load
        self.operations.load_store_op(20, test_address_load)
        self.assertEqual(self.operations.accumulator, test_word_load)

        # Test the store operation
        test_address_store = 3
        test_word_store = "-5432"
        self.operations.registers[test_address_store] = test_word_store
        self.operations.accumulator = test_word_store
        self.operations.load_store_op(21, test_address_store)
        self.assertEqual(self.operations.registers[test_address_store], test_word_store)


if __name__ == "__main__":
    unittest.main()
