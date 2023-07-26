#VIRUTRACK COVID-Contact-Tracing-App



## This is the front-part of my program, ViruTrack: COVID-19 Contact Tracing App. There seven buttons as you can see: 
![1](https://github.com/jayceee1207/COVID-Contact-Tracing-App/assets/129476395/433bae95-d86a-4090-b0ee-83d5242d2afa)


### 1. SELECT FILE:

![2](https://github.com/jayceee1207/COVID-Contact-Tracing-App/assets/129476395/3350d394-85af-4e2c-a2c0-c14f41250e02)


##### Select File button allows the user to open a file. In my program, the main file that it accept is CSV CSV (Comma-Separated Values) files.  CSV files typically have a smaller file size compared to other formats like Excel (.xlsx) or databases. This compactness makes them ideal for scenarios where file size and storage efficiency are crucial considerations.

### 2. ADD INFORMATION:

![3](https://github.com/jayceee1207/COVID-Contact-Tracing-App/assets/129476395/9e5e194b-c881-4caf-b056-41d6d17ee07d)


##### When the Add Information button is pressed, a new window appears and a series of questions are displayed, including those for Name, Age, Address, Email, Contact Number, Date and Time, and Temperature. Additionally, we will inquire as to whether they have recently experienced COVID symptoms or if they have come into contact with anyone else who is exhibiting these symptoms. In addition, they will be required to declare their sincerity when responding to questions. 

### 3. EDIT INFORMATION:

![4](https://github.com/jayceee1207/COVID-Contact-Tracing-App/assets/129476395/5f43bd3d-3bb2-49e7-8246-8a67d00b9b3d)

##### When the button for editing information is pressed, users just enter the entry number where "View Information" may be seen. The Edit Information window will then appear, allowing them to edit and save their prior response. To see if the information has changed, they can view it again in the program that lets them view information.  

### 4. DELETE INFORMATION:

![5](https://github.com/jayceee1207/COVID-Contact-Tracing-App/assets/129476395/e74a76a6-d3d6-4e9b-a25b-caaa8dc37f00)

##### When the button for deleting information is pressed, users just enter the entry number where "View Information" may be seen. The Delete Information window will then appear, allowing them to delete their response. To see if the information has changed, they can view it again in the view information window.

### 5. VIEW INFORMATION:

![6](https://github.com/jayceee1207/COVID-Contact-Tracing-App/assets/129476395/57d02108-4d99-42f1-b167-5e84cbfb8446)


##### When the button for viewing information is pressed, the window will appear including all the information inputted by the users with their basic information and their covid-related questions.

### 6. SEARCH INFORMATION:
![7](https://github.com/jayceee1207/COVID-Contact-Tracing-App/assets/129476395/55415182-2005-4f3a-b82d-85d84f9b3665)

##### When the button for searching information is pressed, there will be a search criteria, they can search according to the: First Name, Last Name, Address, Date, and Time. After that, they can input any letter that corresponds to the information they are looking for. The result will pop with the summary of the inputted information by the user.

### 7.EXIT:
![8](https://github.com/jayceee1207/COVID-Contact-Tracing-App/assets/129476395/8144d40e-8323-40b5-bf58-2f6de3271c3c)

##### When the button for exit is pressed, the program will ask for the confirmation whether they want to exit the program. If the user wishes to, all the information inputted will be saved automatically.


##Module Used:

### tkinter
##### It is the standard Python interface to the Tk GUI toolkit. It provides a set of tools and widgets to create graphical user interfaces. With tkinter, you can create windows, dialogs, buttons, text boxes, and more. It's widely used for creating simple GUI applications.

### PhotoImage
##### This class in tkinter is used to display images in a GUI application. It supports GIF, PGM, PPM, and PNG image formats.

### messagebox
##### It is a module within tkinter that provides a simple way to display dialog boxes with messages to the user. These dialog boxes can be used for showing information, warnings, errors, or asking for simple user input.

### filedialog
##### Another module within tkinter, it provides dialog boxes to allow the user to interact with the file system. You can use it to open or save files, choose directories, and more.

### PIL
##### PIL stands for Python Imaging Library. However, since Python 3.1, the "PIL" library has been renamed to "Pillow" and is used to manipulate images. It supports opening, manipulating, and saving various image file formats.

### ImageTk
##### It is a module within PIL/Pillow that allows you to display images in a tkinter GUI application. It provides an interface between Pillow images and tkinter.

### csv
##### This is a built-in Python module that provides functionality for both reading from and writing to CSV (Comma-Separated Values) files. It's useful for handling tabular data in a simple text-based format.

### re
##### This module stands for regular expressions. It provides support for pattern matching with strings. Regular expressions are powerful tools for searching, matching, and manipulating text based on specific patterns.

### os
##### This is another built-in Python module that provides a way to interact with the operating system. It allows you to perform various operations related to files, directories, processes, and more. It's commonly used for tasks like file manipulation, path handling, and environment information retrieval.





