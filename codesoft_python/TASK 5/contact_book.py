import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.configure(bg="#ADD8E6")  # Light blue background

        self.contacts = []

        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        # Input fields
        tk.Label(self.root, text="Name", bg="#ADD8E6").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Phone Number", bg="#ADD8E6").grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Email", bg="#ADD8E6").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Address", bg="#ADD8E6").grid(row=3, column=0)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(self.root, text="Add Contact", command=self.add_contact, bg="#90EE90").grid(row=4, column=0, columnspan=2)  # Light green button
        tk.Button(self.root, text="View Contacts", command=self.view_contacts, bg="#FFD700").grid(row=5, column=0, columnspan=2)  # Gold button
        tk.Button(self.root, text="Search Contact", command=self.search_contact, bg="#87CEEB").grid(row=6, column=0, columnspan=2)  # Sky blue button
        tk.Button(self.root, text="Update Contact", command=self.update_contact, bg="#FFB6C1").grid(row=7, column=0, columnspan=2)  # Light pink button
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact, bg="#FFA07A").grid(row=8, column=0, columnspan=2)  # Light salmon button

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required!")

    def view_contacts(self):
        if self.contacts:
            contacts_str = "\n".join([f"{c['name']} - {c['phone']}" for c in self.contacts])
            messagebox.showinfo("Contact List", contacts_str)
        else:
            messagebox.showinfo("Contact List", "No contacts found.")

    def search_contact(self):
        search_term = self.name_entry.get()
        found_contacts = [c for c in self.contacts if search_term.lower() in c["name"].lower()]

        if found_contacts:
            contacts_str = "\n".join([f"{c['name']} - {c['phone']}" for c in found_contacts])
            messagebox.showinfo("Search Results", contacts_str)
        else:
            messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        search_term = self.name_entry.get()
        found_contact = None
        
        for contact in self.contacts:
            if search_term.lower() in contact["name"].lower():
                found_contact = contact
                break
        
        if found_contact:
            # Populate fields with existing data
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, found_contact["name"])
            
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, found_contact["phone"])
            
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, found_contact["email"])
            
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, found_contact["address"])

            self.contacts.remove(found_contact)  # Remove the old contact entry
            messagebox.showinfo("Update", "Update the fields and click 'Add Contact' to save changes.")
        else:
            messagebox.showinfo("Update", "No contact found with that name.")

    def delete_contact(self):
        search_term = self.name_entry.get()
        if search_term:
            original_length = len(self.contacts)
            self.contacts = [c for c in self.contacts if search_term.lower() not in c["name"].lower()]
            if len(self.contacts) < original_length:
                messagebox.showinfo("Success", "Contact(s) deleted successfully!")
            else:
                messagebox.showinfo("Error", "No matching contact found to delete.")
        else:
            messagebox.showerror("Error", "Please enter a name to delete.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
