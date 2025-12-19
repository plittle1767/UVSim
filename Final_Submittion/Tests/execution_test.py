import unittest
from unittest.mock import patch
import random

from Tkinter.UVSim import Operations
from Tkinter.UVSim import OperationsError


def random_words_generator(numb_words):
    """
    Generate a register of random words
    numb_words: int - number of words to generate
    """
    address = random.randint(0, 99)
    address = f"{address:02d}"
    wordslist = []
    for i in range(numb_words):
        word = f"+{random.randint(1, 4)}"
        if word == "1" or "2":
            word += f"{random.randint(0, 1)}"
        else:
            word += f"{random.randint(0, 3)}"
        word += address
        wordslist.append(word)
    return wordslist


class ExecutionTests(unittest.TestCase):
    def setUp(self):
        self.operations = Operations()

    @patch('builtins.input', side_effect=["+7777", "+7777"])
    def test_execution_run(self, mock_input):
        """
        Test the program runs without errors
        """
        try:
            self.operations.execute()
        except OperationsError as e:
            self.fail(f"An error occurred: {e}")

    def test_bad_words(self):
        """
        Test the programs fail when the file contains bad words
        this test will create multiple files with bad words and run it
        """
        bad_words = ["+20458", "2054+", "+204", "-20458", "-204"]
        for word in bad_words:
            file = open("TestExecution.txt", "w")
            file.write(word)
            file.close()
            with self.assertRaises(OperationsError) as context:
                self.operations.read_file("TestExecution.txt")
            self.assertTrue(f"Error on line 0: Invalid word: {word}" in str(context.exception))

    def test_101_words(self):
        """
        Test the program doesn't run when the file contain with 101 or more words
        """
        words_to_add = random_words_generator(101)
        file = open("TestExecution.txt", "w")
        file.write("\n".join(words_to_add))
        file.close()
        with self.assertRaises(OperationsError) as context:
            self.operations.read_file("TestExecution.txt")
        self.assertTrue(f"Error on line 101: Too many words in the file")

    def test_100_words(self):
        """
        Test the program will run with 100 words or less
        """
        self.operations.registers.clear()
        words_to_add = random_words_generator(100)
        file = open("TestExecution.txt", "w")
        file.write("\n".join(words_to_add))
        file.close()
        self.operations.read_file("TestExecution.txt")
        i = 0
        for words in words_to_add:
            self.assertEqual(self.operations.registers[i], words)
            i += 1


if __name__ == '__main__':
    unittest.main()
