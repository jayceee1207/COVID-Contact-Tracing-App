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
    def save_as_file(self):
        #Save contact information
        file_path = filedialog.asksaveasfilename(title="Save Contact Information", defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(self.entries)
                self.file_path = file_path
                messagebox.showinfo("Success", "Contact information was saved successfully.")
            except IOError:
                messagebox.showerror("Error", "Failed to save contact information to file.")
        
    #Create widgets for default screen for user after opening
    def create_widgets(self):
        self.label = tk.Label(self.window, width=30, text="Contact Tracing App")
        self.label.pack(pady=10)

        self.file_button = tk.Button(self.window, width=20, text="Select File", background='white', command=self.select_file) #this is to select file we want to open.
        self.file_button.pack(pady=10)

        self.add_button = tk.Button(self.window, width=20, text="Add Contact", background='white', command=self.add_contact) #we will make add contact to add information
        self.add_button.pack(pady=15)

        self.edit_button = tk.Button(self.window, width=20, text="Edit Contact", background='white', command=self.edit_contact) #we wil make edit contact  function to edit all the inputted contact of the user
        self.edit_button.pack(pady=10)

        self.delete_button = tk.Button(self.window, width=20, text="Delete Contact", background='white', command=self.delete_contact) #we will make delete contact to delete information we wish to remove.
        self.delete_button.pack(pady=15)

        self.view_button = tk.Button(self.window, width=20, text="View Contacts", background='white', command=self.view_contacts) #we will make view contacts function to view all the information
        self.view_button.pack(pady=10)

        self.search_button = tk.Button(self.window, width=20, text="Search Address Book", background='white', font=("Times New Roman", 12, "bold"), command=self.search_address_book) #we will make search address book function to search all the information of the user.
        self.search_button.pack(pady=15)

        self.exit_button = tk.Button(self.window, width=10, text="Exit", background='white', command=self.on_exit) #we will make on_exit function
        self.exit_button.pack(pady=10)

    #Create Method: add contact
    def add_contact(self):
        self.add_window = tk.Toplevel(self.window)
        self.add_window.title("Add Contact")

        #Infomation for Last Name
        self.first_name_label = tk.Label(self.add_window, text="First Name:")
        self.first_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.first_name_entry = tk.Entry(self.add_window)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        #Infomation for First Name
        self.last_name_label = tk.Label(self.add_window, text="Last Name:")
        self.last_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.last_name_entry = tk.Entry(self.add_window)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        #Infomation for Address
        self.address_label = tk.Label(self.add_window, text="Address:")
        self.address_label.grid(row=2, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.add_window)
        self.address_entry.grid(row=2, column=1, padx=10, pady=5)

        #Infomation for Email-Address
        self.email_address_label = tk.Label(self.add_window, text="Email Address:")
        self.email_address_label.grid(row=3, column=0, padx=10, pady=5)
        self.email_address_entry = tk.Entry(self.add_window)
        self.email_address_entry.grid(row=3, column=1, padx=10, pady=5)

        #Infomation for Contact Number
        self.contact_number_label = tk.Label(self.add_window, text="Contact Number:")
        self.contact_number_label.grid(row=4, column=0, padx=10, pady=5)
        self.contact_number_entry = tk.Entry(self.add_window)
        self.contact_number_entry.grid(row=4, column=1, padx=10, pady=5)

        #Infomation for Age
        self.age_label = tk.Label(self.add_window, text="Age:")
        self.age_label.grid(row=5, column=0, padx=10, pady=5)
        self.age_entry = tk.Entry(self.add_window)
        self.age_entry.grid(row=5, column=1, padx=10, pady=5)

        #Infomation for Date
        self.date_label = tk.Label(self.add_window, text="Date (MM/DD/YEAR):")
        self.date_label.grid(row=6, column=0, padx=10, pady=5)
        self.date_entry = tk.Entry(self.add_window)
        self.date_entry.grid(row=6, column=1, padx=10, pady=5)

        #Infomation for Time
        self.time_label = tk.Label(self.add_window, text="Time:")
        self.time_label.grid(row=7, column=0, padx=10, pady=5)
        self.time_entry = tk.Entry(self.add_window)
        self.time_entry.grid(row=7, column=1, padx=10, pady=5)

        self.save_button = tk.Button(self.add_window, text="Save", command=self.save_contact) #save contact will be made to save information for the user
        self.save_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)


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
