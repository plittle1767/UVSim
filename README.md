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
- Download the UVSim project file. This can be done by clicking "<>code", "Download ZIP", and then unzip the file.

## How to Start the Program
1. Make sure all the required modules (Standard Python Library) are accessible in the Python environment where you intend to run this program.
2. Execute the Python file using a Python interpreter. You can do this by running python main.py in your terminal or command prompt.
3. GUI Window: After running the command, you will be taken to the UVSim GUI application interface.
4. Interacting with the GUI: Within the GUI window, you can interact with the program by clicking the provided buttons.

## Running the Program and Simulators
The UVSim Emulator allows you to execute programs and simulate computer operations by doing the following:
1. Add simulator to the screen by creating a new simulator. (See Adding Simulators section)
2. Click on the tab that has been created by the "Add new simulator" button in step 1.
3. Your selected file will appear in the text editor and has simultaneously been loaded to the program. (You can click the "Save and Load File" button if you desire to check that the file is loaded to the program. By doing so, you will see "File read successfully" in your console.)
4. Click on the "Run" button to execute the program.
5. Monitor the output in the output console.
6. Use the "Stop" button to halt program execution.

## Adding Simulators
1. To begin adding simulators, click the "Add new simulator" button. This will open a tab in which you can select files you would like to test.
2. Once a file is selected, the tab for it will appear in the main page under "All Simulations" as well as in the workspace panel to the left.
3. You can repeat step 1 and 2 to create multiple simulations. 

## File Management 
1. To load a new program file, select "File" in the menu bar and then "Open New File." Select the new file you would like to load.
2. To save and load the file prior to running the program, simply click the "Save and Load File" button.

## Editing Selected Files
Once a file is loaded or created, you can edit its contents in the text editor provided by doing the following:
1. Make your desired changes to the code.
2. Use the "Save and Load File" button to save your changes in preparation for running the program.

## Predefined Theme Customization
The UVSim Emulator provides options for customizing the user interface by doing the following:
1. Click on the "Themes" menu in the top right corner of the program with a color pallet icon bar. (When clicked, a drop down menu of Green, Blue, Teal, Purple, and Customer will appear.)
2. To customize the interface with a predefined color theme select Green, Blue, Teal, or Purple in the dropdown menu.

## Custom Theme 
Users can personalize their experience by setting custom color themes:
1. Click on the "Themes" menu in the top right corner of the program with a color pallet icon bar.
2. Select "Custom" in the drop down menu.
3. Enter Hex Color Codes:
- Users will be presented with a dialog box containing four input fields, each corresponding to different aspects of the application's UI:

   - Text Color: Sets the color of the text throughout the application. (Ensure it contrasts well with the background for readability.)
   - Primary Color: Used for most of the interactive elements like buttons and links. (Choose a color that stands out but is pleasant to the eye.)
   - Secondary Color: This color is used for elements that are not in the foreground but still need distinction.
   - Tertiary Color: Used for accents and less dominant elements.

- Each field requires a valid hex color code. Hex color codes start with a # followed by six hexadecimal digits (e.g., #FFFFFF for white). Invalid entries will prompt an error and will not be accepted.

4. After filling out all the color fields with valid hex codes, the "Apply Theme" button will become enabled. Click the "Apply Theme" button to apply the colors to the application's UI.

## Exiting the UVSim Emulator 
The program can be exited in several ways depending on your operating system and how the application is running:
1. Close the Web Browser: If you are running the UVSim Emulator in a web browser, you can simply close the browser window or tab containing the application. This will terminate the program.
2. Terminate the Python Process: If you started the UVSim Emulator using a Python script (main.py), you can terminate the program by stopping the Python process.
- On Windows: You can press Ctrl + C in the command prompt window where the Python process is running.
- On macOS or Linux: You can use the Ctrl + Z or Ctrl + C keyboard shortcuts to send a termination signal to the Python process.
