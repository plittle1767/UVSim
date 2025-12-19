# UVSim

## Description
UVSim is a simple virtual machine designed to help computer science students to learn about machine language and 
computer architecture. This software simulator allows students to execute machine language programs written in 
BasicML on the UVSim. The UVSim works with words, which are signed four-digit decimal numbers (e.g., +1234, -5678). 
It has a 100-word memory, and these words are referenced by location numbers 00, 01, ..., 99.

## Prerequisites
- Download the latest version of Python from https://www.python.org/downloads/ with your corresponding OS and run the installer.
- Download any files you would like to use with the UVSim program.

## Installation
1. Download the UVSim project file. This can be done by clicking "<>code", "Download ZIP", and then unzip the file.

## How to Run
1. Make sure all the required modules (Standard Python Library) are accessible in the Python environment where you intend to run this program.
2. Execute the Python file using a Python interpreter. You can do this by running python main.py in your terminal or command prompt.
3. GUI Window: After running the command, a GUI window titled "UVSim GUI" should appear.
4. Interacting with the GUI: Within the GUI window, you can interact with the program by clicking the provided buttons:
- Click "Load Program" to select a program file.
- Click "Stop Program" to halt the execution of the program.
- Click "Restart Program" to reset the emulator's state and load a new program file.
5. Selecting a Program File: When you click "Load Program," a file dialog will open, allowing you to select a program file.
6. Executing the Program: After selecting a program file, the program will load the file into the emulator's memory and execute it.
- Input Dialog: During the program execution, if there's an input operation (opcode 10) encountered in the program, an input dialog window will appear.
- Entering Input: In the input dialog window, you will see a label prompting you to enter a value for a specific memory address. Input a numerical value into the entry field provided
  in the dialog window. After entering the desired value, click the "OK" button in the input dialog window to confirm your input.
- Updating the Console: The input value you provided will be displayed in the console area of the GUI window, indicating that the input operation was successful.
- Continued Program Execution: The program will continue its execution, potentially encountering further input, output, or other operations based on the program's logic.
7. Once the program has executed completely, a confirmation dialog will open stating "Program execution completed successfully."
8. To exit the program, either click the red 'x' at the top left corner of the interface or use the stop button on the main.py page. 
