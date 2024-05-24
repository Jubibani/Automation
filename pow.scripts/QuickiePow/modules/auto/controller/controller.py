import tkinter as tk
from tkinter import messagebox

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Tkinter App")
        self.root.geometry("400x300")
        
        self.items = []
        self.deleted_items = []
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Create and place a Listbox to display items
        self.listbox = tk.Listbox(self.root, width=50, height=10)
        self.listbox.pack(pady=20)

        # Entry widget to add new items
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        # Button to add an item
        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Button to delete the last item
        self.delete_button = tk.Button(self.root, text="Delete Last Item", command=self.delete_last_item)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Button to undo the last deletion
        self.undo_button = tk.Button(self.root, text="Undo Delete", command=self.undo_delete)
        self.undo_button.pack(side=tk.LEFT, padx=10, pady=10)
    
    def add_item(self):
        item = self.entry.get()
        if item:
            self.items.append(item)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter an item.")
    
    def delete_last_item(self):
        if self.items:
            item = self.items.pop()
            self.deleted_items.append(item)
            self.update_listbox()
        else:
            messagebox.showwarning("Deletion Error", "No items to delete.")
    
    def undo_delete(self):
        if self.deleted_items:
            item = self.deleted_items.pop()
            self.items.append(item)
            self.update_listbox()
        else:
            messagebox.showwarning("Undo Error", "No deleted items to undo.")
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
