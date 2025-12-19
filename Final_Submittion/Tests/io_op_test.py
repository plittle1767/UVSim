from Tkinter.UVSim import Operations
from Tkinter.UVSim import OperationsError
import unittest
import io
from unittest.mock import patch


class TestOperations(unittest.TestCase):
    def setUp(self):
        self.operations = Operations()
        self.operations.registers[0] = "+1111"
        self.operations.registers[1] = "-1234"
        self.operations.registers[2] = "+0000"
        self.operations.registers[3] = "+0000"
        self.operations.registers[4] = "+0000"
        self.operations.registers[5] = "+0000"
        self.operations.registers[6] = "+0000"

    @patch("builtins.input", return_value="2244")  # Use patch to simulate input
    def test_read(self, mock_input):
        self.operations.IO_op(10, 2)
        expected_output = "+2244"
        self.assertEqual(self.operations.registers[2], expected_output)

    @patch("builtins.input", return_value="-1440")
    def test_read2(self, mock_input):
        self.operations.IO_op(10, 3)
        expected_output = "-1440"
        self.assertEqual(self.operations.registers[3], expected_output)

    @patch("builtins.input", return_value="+4466")
    def test_read3(self, mock_input):
        self.operations.IO_op(10, 4)
        expected_output = "+4466"
        self.assertEqual(self.operations.registers[4], expected_output)

    # Test invalid length
    @patch("builtins.input",
           return_value="+12345")
    def test_bad_input2(self, mock_input):
        initial_value = self.operations.registers[5]
        success = self.operations.IO_op(10, 5)
        self.assertFalse(success)   # Assert that the input was not processed
        self.assertEqual(self.operations.registers[5], initial_value)   # Assert that the register value is unchanged

    # Test invalid char
    @patch("builtins.input",
           return_value="+00f0")
    def test_bad_input3(self, mock_input):
        initial_value = self.operations.registers[6]
        success = self.operations.IO_op(10, 6)
        self.assertFalse(success)  # Assert that the input was not processed
        self.assertEqual(self.operations.registers[6], initial_value)  # Assert that the register value is unchanged

    def test_write(self):
        # Use patch to check print statement
        with patch("builtins.input", return_value="+1111"), \
                patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:

            self.operations.IO_op(11, 0)
            printed_output = mock_stdout.getvalue().strip().splitlines()[1:]
            expected_output1 = "+1111"
            self.assertEqual([expected_output1], printed_output)

    def test_write2(self):
        # Use patch to check print statement
        with patch("builtins.input", return_value="-1234"), \
                patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:

            self.operations.IO_op(11, 1)
            printed_output = mock_stdout.getvalue().strip().splitlines()[1:]
            expected_output = "-1234"
            self.assertEqual([expected_output], printed_output)

    def test_write_invalid_address(self):
        # Use patch to check print statement
        # with patch("builtins.input", return_value="Error: Address {address} not found in registers."), \
        #         patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        #     self.operations.IO_op(11, 15)
        #     printed_output = mock_stdout.getvalue().strip().splitlines()[1:]
        #     expected_output = "Error: Address {address} not found in registers."
        #     self.assertEqual([expected_output], printed_output)
        with self.assertRaises(OperationsError) as context:
            self.operations.IO_op(11, 15)

        self.assertTrue("Error: Address 15 not found in registers." in str(context.exception))


if __name__ == "__main__":
    unittest.main()
