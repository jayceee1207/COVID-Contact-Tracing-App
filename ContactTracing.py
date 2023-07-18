#John Carlo R. Ablay
#BS Computer Engineering 1-5
#Final Project: COVID Contact Tracing App

import tkinter as tk
from tkinter import messagebox, filedialog
import csv 
import re 

#PSEUDOCODE

#Create class ContactTracing and the GUI
class ContactTracing:
    def __init__ (self):
        self.window = tk.Tk
        self.window.title = ("Covid-19 Contact Tracing App")

        self.window.geometry("500x500")
        self.window.configure(bg="green")
        self.window.resizable(True, True)
    #Add file and its path
    #To open a CSV file where informatio of user will be stored
    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select Existing File", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, mode="r") as file:
                    reader = csv.reader(file)
                    contacts = list(reader)
                    self.entries.extend(contacts)  # Add contacts to the entries list
                    self.file_path = file_path
                    messagebox.showinfo("Success", "File added successfully.")
            except FileNotFoundError:
                messagebox.showerror("File Not Found", "The selected file does not exist.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add file: {str(e)}")

    #Create Method: save to file 
    def save_to_file(self):
        if not self.file_path:
            self.save_as_file() #We will make method for save files
        else:
            try:
                with open(self.file_path, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(self.entries)
                messagebox.showinfo("Success", "Contact Information was saved successfully.")
            except IOError:
                messagebox.showerror("Error", "Failed to save contact information to file.")
    #Create Method: save as file

        #Save contact information

    #Create Method: add contact

        #Infomation for Last Name

        #Infomation for First Name

        #Infomation for Address

        #Infomation for Email-Address

        #Infomation for Contact Number

        #Infomation for Age

        #Infomation for Date

        #Infomation for Time

    #Create Method:save contact

        #add error handlings for the information listed by the user.

    #Create Method: edit contact

        #select entry number from the list

    #Create Method: update contacts

        #Infomation for Last Name

        #Infomation for First Name

        #Infomation for Address

        #Infomation for Email-Address

        #Infomation for Contact Number

        #Infomation for Age

        #Infomation for Date

        #Infomation for Time

    #Create Method: save_edit 

    #Create Method: delete contact

    #Create Method: view contact

    #Create Method: search contact

        #search criteria: 

contact_tracing = ContactTracing()
contact_tracing.run()
