from unittest import TestCase

from CS_2450.UVSim import Operations


class TestArithmetics(TestCase):
    def setUp(self):
        self.operations = Operations()
        self.operations.registers = {0: "+1208", 1: "+1000", 2: "+0002", 3: "+0000", 4: "+9000", 5: "+30000", 6: "+0001"}

    def test_add_1(self):
        self.operations.arithmetic_op(30, 0)
        self.assertEqual("+1208", self.operations.accumulator, "Add operation failed")

    def test_add_2(self):
        self.operations.arithmetic_op(30, 3)
        self.assertEqual("+0000", self.operations.accumulator, "Add operation failed")

    def test_truncation(self):
        self.operations.arithmetic_op(30, 5)
        self.assertEqual("+9999", self.operations.accumulator, "Add operation failed")

    def test_subtract_1(self):
        self.operations.arithmetic_op(30, 0)
        self.operations.arithmetic_op(31, 1)
        self.assertEqual("+0208", self.operations.accumulator, "Subtract operation failed")

    def test_subtract_2(self):
        self.operations.arithmetic_op(30, 3)
        self.operations.arithmetic_op(31, 6)
        self.assertEqual("-0001", self.operations.accumulator, "Subtract operation failed")

    def test_divide_1(self):
        self.operations.arithmetic_op(30, 0)
        self.operations.arithmetic_op(32, 2)
        self.assertEqual("+0604", self.operations.accumulator, "Divide operation failed")

    def test_divide_2(self):
        self.operations.arithmetic_op(30, 4)
        self.operations.arithmetic_op(32, 2)
        self.assertEqual("+4500", self.operations.accumulator, "Divide operation failed")

    def test_multiply_1(self):
        self.operations.arithmetic_op(30, 0)
        self.operations.arithmetic_op(33, 2)
        self.assertEqual("+2416", self.operations.accumulator, "Multiply operation failed")

    def test_multiply_2(self):
        self.operations.arithmetic_op(30, 4)
        self.operations.arithmetic_op(33, 3)
        self.assertEqual("+0000", self.operations.accumulator, "Multiply operation failed")

    def test_invalid(self):
        self.operations = Operations()
        self.operations.registers = {0: "+1200", 1: "+1010", 2: "+2002", 3: "+0300", 4: "+9500", 5: "+0401"}

        self.operations.arithmetic_op(90, 4)
        self.assertEqual("+0000", self.operations.accumulator, "Multiply operation failed")

