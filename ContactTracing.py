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
        self.entries = []
        self.file_path = ""
        self.edit_index = None

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
        self.label = tk.Label(self.window, width=30, background='pink', 
                              text="Basic Information", 
                              font=("Helvetica", 20, "bold"))
        self.label.pack(pady=10)

        self.file_button = tk.Button(self.window, width=20, 
                                     text="Select File", 
                                     background='white', 
                                     font=("Times New Roman", 12, "bold"), 
                                     command=self.select_file) #this is to select file we want to open.
        self.file_button.pack(pady=10)

        self.add_button = tk.Button(self.window, width=20, 
                                    text="Add Contact", 
                                    background='white', 
                                    font=("Times New Roman", 12, "bold"),
                                    command=self.add_contact) #we will make add contact to add information
        self.add_button.pack(pady=15)

        self.edit_button = tk.Button(self.window, width=20, 
                                     text="Edit Contact", 
                                     background='white', 
                                     font=("Times New Roman", 12, "bold"),
                                     command=self.edit_contact) #we wil make edit contact  function to edit all the inputted contact of the user
        self.edit_button.pack(pady=10)

        self.delete_button = tk.Button(self.window, width=20, 
                                       text="Delete Contact", 
                                       background='white', 
                                       font=("Times New Roman", 12, "bold"),
                                       command=self.delete_contact) #we will make delete contact to delete information we wish to remove.
        self.delete_button.pack(pady=15)

        self.view_button = tk.Button(self.window, width=20, 
                                     text="View Contacts", 
                                     background='white', 
                                     font=("Times New Roman", 12, "bold"),
                                     command=self.view_contacts) #we will make view contacts function to view all the information
        self.view_button.pack(pady=10)

        self.search_button = tk.Button(self.window, width=20, 
                                       text="Search Contact Information", 
                                       background='white', 
                                       font=("Times New Roman", 12, "bold"), 
                                       command=self.search_contact) #we will make search address book function to search all the information of the user.
        self.search_button.pack(pady=15)

        self.exit_button = tk.Button(self.window, width=10, 
                                     text="Exit", background='white', 
                                     font=("Times New Roman", 12, "bold"),
                                     command=self.on_exit) #we will make on_exit function
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
    def save_contact(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        address = self.address_entry.get()
        email_address = self.email_address_entry.get()
        contact_number = self.contact_number_entry.get()
        age = self.age_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        #add error handlings for the information listed by the user.
        if not first_name or not last_name or not address:
            messagebox.showerror("Error!", "Please fill all the fields.")
            return

                        #add uppercase so it could still accept capitalized letters
        if not re.match(r'^[a-zA-Z\s]+$', first_name):
            messagebox.showerror("Error", "First name should only contain letters and spaces.")
            return
                        #add uppercase so it could still accept capitalized letters
        if not re.match(r'^[a-zA-Z\s]+$', last_name):
            messagebox.showerror("Error", "Last name should only contain letters and spaces.")
            return
                        #add string operator to know where the string is to be specified
        if not re.match(r'^[\+\d\s]+$', contact_number):
            messagebox.showerror("Error", "Contact number should only contain '+', digits, and spaces.")
            return

        # Validate the maximum of 15 integers
        contact_number_digits = re.findall(r'\d', contact_number)
        num_digits = len(contact_number_digits)
        if num_digits < 5 or num_digits > 14:
            messagebox.showerror("Error", "Contact number should contain between 5 and 14 digits.")
            return
        
        #To ensure that they will input their correct email format
        if "@" not in email_address or "." not in email_address:
            messagebox.showerror("Error", "Please enter a valid email address. It must contain '@' and '.'")
            return

        # Check if the contact is being edited
        if self.edit_index is not None:
            # Update the existing entry
            self.entries[self.edit_index][0] = first_name
            self.entries[self.edit_index][1] = last_name
            self.entries[self.edit_index][2] = address
            self.entries[self.edit_index][3] = email_address
            self.entries[self.edit_index][4] = contact_number
            self.entries[self.edit_index][5] = age
            self.entries[self.edit_index][6] = date
            self.entries[self.edit_index][7] = time

        else:
            # Add a new entry
            self.entries.append([first_name, last_name, address,email_address, contact_number, age, date, time ])

        self.add_window.destroy()
        messagebox.showinfo("Success", "Contact saved successfully.")

    #Create Method: edit contact
    def edit_contact(self):
        #select entry number from the list
        if not self.entries:
            messagebox.showerror("Error", "No contacts available.")
            return

        self.edit_window = tk.Toplevel(self.window)
        self.edit_window.title("Edit Contact")

        self.edit_label = tk.Label(self.edit_window, text="Select Entry Number:")
        self.edit_label.grid(row=0, column=0, padx=10, pady=5)
        self.edit_entry = tk.Entry(self.edit_window)
        self.edit_entry.grid(row=0, column=1, padx=10, pady=5)

        self.edit_button = tk.Button(self.edit_window, text="Edit", command=self.update_contact)
        self.edit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)


    #Create Method: update contacts
    def update_contact(self):
        entry_num = self.edit_entry.get()

        if not entry_num.isdigit():
            messagebox.showerror("Error", "Entry number must be a valid integer.")
            return

        entry_num = int(entry_num)

        if entry_num < 1 or entry_num > len(self.entries):
            messagebox.showerror("Error", "Invalid entry number.")
            return
        else:
            self.edit_window.destroy()
        try:
            self.edit_index = entry_num - 1  
            contact = self.entries[self.edit_index]

            self.edit_window = tk.Toplevel(self.window)
            self.edit_window.title("Edit Contact")

            #Infomation for First Name
            self.first_name_label = tk.Label(self.edit_window, text="First Name:")
            self.first_name_label.grid(row=0, column=0, padx=10, pady=5)
            self.first_name_entry = tk.Entry(self.edit_window)
            self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)


            #Infomation for Last Name
            self.last_name_label = tk.Label(self.edit_window, text="Last Name:")
            self.last_name_label.grid(row=1, column=0, padx=10, pady=5)
            self.last_name_entry = tk.Entry(self.edit_window)
            self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

            #Infomation for Address
            self.address_label = tk.Label(self.edit_window, text="Address:")
            self.address_label.grid(row=2, column=0, padx=10, pady=5)
            self.address_entry = tk.Entry(self.edit_window)
            self.address_entry.grid(row=2, column=1, padx=10, pady=5)

            #Infomation for Email-Address
            self.email_address_label = tk.Label(self.edit_window, text="Email Address:")
            self.email_address_label.grid(row=3, column=0, padx=10, pady=5)
            self.email_address_entry = tk.Entry(self.edit_window)
            self.email_address_entry.grid(row=3, column=1, padx=10, pady=5)

            #Infomation for Contact Number
            self.contact_number_label = tk.Label(self.edit_window, text="Contact Number:")
            self.contact_number_label.grid(row=4, column=0, padx=10, pady=5)
            self.contact_number_entry = tk.Entry(self.edit_window)
            self.contact_number_entry.grid(row=4, column=1, padx=10, pady=5)

            #Infomation for Age
            self.age_label = tk.Label(self.edit_window, text="Age:")
            self.age_label.grid(row=5, column=0, padx=10, pady=5)
            self.age_entry = tk.Entry(self.edit_window)
            self.age_entry.grid(row=5, column=1, padx=10, pady=5)

            #Infomation for Date
            self.date_label = tk.Label(self.edit_window, text="Date:")
            self.date_label.grid(row=6, column=0, padx=10, pady=5)
            self.date_entry = tk.Entry(self.edit_window)
            self.date_entry.grid(row=6, column=1, padx=10, pady=5)

            #Infomation for Time
            self.time_label = tk.Label(self.edit_window, text="Time:")
            self.time_label.grid(row=7, column=0, padx=10, pady=5)
            self.time_entry = tk.Entry(self.edit_window)
            self.time_entry.grid(row=7, column=1, padx=10, pady=5)

            self.save_button = tk.Button(self.edit_window, text="Save", command=self.save_edit)
            self.save_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

            self.first_name_entry.insert(tk.END, contact[0])
            self.last_name_entry.insert(tk.END, contact[1])
            self.address_entry.insert(tk.END, contact[2])
            self.email_address_entry.insert(tk.END, contact[3])
            self.contact_number_entry.insert(tk.END, contact[4])
            self.age_entry.insert(tk.END, contact[5])
            self.date_entry.insert(tk.END, contact[6])
            self.time_entry.insert(tk.END, contact[7])

        except ValueError:
                messagebox.showinfo("Invalid Input","Entry number must be a valid number.")


    #Create Method: save_edit 
    def save_edit(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        address = self.address_entry.get()
        email_address = self.email_address_entry.get()
        contact_number = self.contact_number_entry.get()
        age = self.age_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        if not first_name or not last_name or not address:
                messagebox.showerror("Error", "Please fill in all fields.")
                return
            
        contact = (first_name, last_name, address, email_address, contact_number, age, date, time)

                        #add uppercase so it could still accept capitalized letters
        if not re.match(r'^[a-zA-Z\s]+$', first_name):
            messagebox.showerror("Error", "First name should only contain letters and spaces.")
            return
                        #add uppercase so it could still accept capitalized letters
        if not re.match(r'^[a-zA-Z\s]+$', last_name):
                messagebox.showerror("Error", "Last name should only contain letters and spaces.")
                return
                         
                        #add \d to specify integer values
        if not re.match(r'^[\+\d\s]+$', contact_number):
            messagebox.showerror("Error", "Contact number should only contain '+', digits, and spaces.")
            return
        
        if "@" not in email_address or "." not in email_address:
            messagebox.showerror("Error", "Please enter a valid email address. It must contain '@' and '.'")
            return
        
        if not re.match(r'^[\+\d\s]+$', age):
            messagebox.showerror("Error", "Age should only contain digits.")
            return
        
            
        if self.edit_index is not None:
            if self.edit_index >= len(self.entries):
                messagebox.showerror("Error", "Invalid entry index.")
                return

            self.entries[self.edit_index] = contact
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            self.entries.append(contact)
            messagebox.showinfo("Success", "Contact updated successfully.")
        
        self.edit_window.destroy()


    #Create Method: delete contact
    def delete_contact(self):
        if not self.entries:
            messagebox.showerror("Error", "No contacts available.")
            return
        
        self.delete_window = tk.Toplevel(self.window)
        self.delete_window.title("Delete Contact")

        self.delete_label = tk.Label(self.delete_window, text="Enter Entry Number:")
        self.delete_label.grid(row=0, column=0, padx=10, pady=5)
        self.delete_entry = tk.Entry(self.delete_window)
        self.delete_entry.grid(row=0, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(self.delete_window, text="Delete", command=self.remove_contact)
        self.delete_button.grid(row=1, column=0, columnspan=0, padx=10, pady=5)

    def remove_contact(self):
        entry_num = self.delete_entry.get()

        if not entry_num.isdigit():
            messagebox.showerror("Error", "Entry number must be a valid integer.")
            return

        entry_num = int(entry_num)

        if entry_num < 1 or entry_num > len(self.entries):
            messagebox.showerror("Error", "Invalid entry number.")
            return  
        
        #I put -1 because if the user input 1, the position of it in the sequence is 2
        self.entries.pop(entry_num - 1)
        self.delete_window.destroy()
        messagebox.showinfo("Success", "Contact deleted successfully.")


    #Create Method: view contact
    def view_contacts(self):
        if not self.entries:
            messagebox.showinfo("Info", "Contact information is empty.")
            return

        self.view_window = tk.Toplevel(self.window)
        self.view_window.title("View Contacts")
        self.view_window.geometry("1000x900")

        self.canvas = tk.Canvas(self.view_window)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.view_window, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.view_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.view_frame)
        labels = ["Entry #", "First Name", "Last Name", "Address", "Email-Address","Contact Number","Age", "Date", "Time"]

        for col, label in enumerate(labels):
            column_label = tk.Label(self.view_frame, text=label, padx=10, pady=5)
            column_label.grid(row=0, column=col)

        for i, contact in enumerate(self.entries, 1):
            entry_number_label = tk.Label(self.view_frame, text=str(i), padx=10, pady=5)
            entry_number_label.grid(row=i, column=0)

            for col, value in enumerate(contact, 1):
                entry_label = tk.Label(self.view_frame, text=value, padx=10, pady=5)
                entry_label.grid(row=i, column=col)

        self.view_frame.grid_columnconfigure(0, weight=1)
        self.view_frame.grid_rowconfigure(0, weight=1)

        self.scrollbar.config(command=self.canvas.yview)

    def search_contact (self):
        if not self.entries:
            messagebox.showinfo("Info", "Contact information is empty.")
            return
        self.search_window = tk.Toplevel(self.window)
        self.search_window.title("Search Contact information")

        self.criteria_label = tk.Label(self.search_window, text="Search Criteria:")
        self.criteria_label.grid(row=0, column=0, padx=10, pady=5)

        self.criteria_var = tk.StringVar()
        self.criteria_var.set("First Name")

        self.criteria_dropdown = tk.OptionMenu(self.search_window, self.criteria_var, "First Name", "Last Name",
                                               "Address", "Contact Number","Date")
        self.criteria_dropdown.grid(row=0, column=1, padx=10, pady=5)

        self.query_label = tk.Label(self.search_window, text="Query:")
        self.query_label.grid(row=0, column=0, padx=10, pady=5)

        self.query_entry = tk.Entry(self.search_window)
        self.query_entry.grid(row=0, column=1, padx=10, pady=5)

        self.search_button = tk.Button(self.search_window, text="Search", command=self.perform_search) #we will make a function for perform_search
        self.search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.results_text = tk.Text(self.search_window, width=50, height=10)
        self.results_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    #perform search function to search for the information in the list


    def perform_search(self):
        criteria = self.criteria_var.get()
        query = self.query_entry.get()

        if not query:
            messagebox.showerror("Please enter a query.")
            return

        # Convert all query and entry strings to lowercase for case-insensitive search
        query = query.lower()
        self.entries = [[entry_item.lower() if isinstance(entry_item, str) else entry_item for entry_item in entry] for entry in self.entries]

        results = []
        if criteria == "First Name":
            results = [entry for entry in self.entries if query in entry[0]]
        elif criteria == "Last Name":
            results = [entry for entry in self.entries if query in entry[1]]
        elif criteria == "Address":
            results = [entry for entry in self.entries if query in entry[2]]
        elif criteria == "Email-address":
            results = [entry for entry in self.entries if query in entry[3]]
        elif criteria == "Contact Number":
            results = [entry for entry in self.entries if query in entry[4]]
        elif criteria == "Age":
            results = [entry for entry in self.entries if query in str(entry[5])]
        elif criteria == "Date":
            results = [entry for entry in self.entries if query in str(entry[6])]
        elif criteria == "Time":
            results = [entry for entry in self.entries if query in str(entry[7])] #I forgot to put []

    
    def display_search_results(self, results):
        self.results_text.delete("1.0", tk.END)
        if not results:
            self.results_text.insert(tk.END, "No results found.")
        else:
            for result in results:
                self.results_text.insert(tk.END, f"First Name: {result[0]}\n")
                self.results_text.insert(tk.END, f"Last Name: {result[1]}\n")
                self.results_text.insert(tk.END, f"Address: {result[2]}\n")
                self.results_text.insert(tk.END, f"Email-address: {result[3]}\n")
                self.results_text.insert(tk.END, f"Contact Number: {result[4]}\n")
                self.results_text.insert(tk.END, f"Age: {result[5]}\n")
                self.results_text.insert(tk.END, f"Date: {result[6]}\n")
                self.results_text.insert(tk.END, f"Time: {result[7]}\n")
                self.results_text.insert(tk.END, "-------------------------\n")


    #add functions to validate email, phone number if there are same contacts
    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email)

    def validate_phone(self, phone):
        pattern = r"^\d{10}$"
        return re.match(pattern, phone)

    def get_selected_index(self):
        selection = self.view_window.focus()
        if selection:
            index = int(self.view_window.item(selection)["text"].split(":")[1].strip())
            return index
        else:
            messagebox.showinfo("Info", "Please select a contact.")
            return None

    def on_exit(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to exit?")
        if confirmed:
            self.save_to_file()
            self.window.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.save_to_file()
            self.window.destroy()


    def run(self):
        pass

contact_tracing = ContactTracing()
contact_tracing.run()
