import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

matplotlib.use('Agg')  # Use the non-GUI backend before importing pyplot


# Database Setup
def init_db():
    conn = sqlite3.connect("assets.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS assets (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        category TEXT,
                        serial TEXT,
                        status TEXT,
                        assigned_to TEXT,
                        purchase_date TEXT)''')
    conn.commit()
    conn.close()

# Function to add asset
def add_asset():
    name = name_entry.get()
    category = category_entry.get()
    serial = serial_entry.get()
    status = status_entry.get()
    assigned_to = assigned_to_entry.get()
    purchase_date = purchase_date_entry.get()
    
    if not name or not category or not serial:
        messagebox.showerror("Error", "Name, Category, and Serial are required!")
        return
    
    conn = sqlite3.connect("assets.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO assets (name, category, serial, status, assigned_to, purchase_date) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, category, serial, status, assigned_to, purchase_date))
    conn.commit()
    conn.close()
    load_assets()
    clear_entries()

# Function to load assets
def load_assets():
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect("assets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# Function to clear entries
def clear_entries():
    name_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    serial_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)
    assigned_to_entry.delete(0, tk.END)
    purchase_date_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("IT Asset Management")
root.geometry("800x500")

# Input Fields
frame = ttk.Frame(root, padding=10)
frame.pack(fill="x")

ttk.Label(frame, text="Name:").grid(row=0, column=0)
name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1)

ttk.Label(frame, text="Category:").grid(row=1, column=0)
category_entry = ttk.Entry(frame)
category_entry.grid(row=1, column=1)

ttk.Label(frame, text="Serial:").grid(row=2, column=0)
serial_entry = ttk.Entry(frame)
serial_entry.grid(row=2, column=1)

ttk.Label(frame, text="Status:").grid(row=0, column=2)
status_entry = ttk.Entry(frame)
status_entry.grid(row=0, column=3)

ttk.Label(frame, text="Assigned To:").grid(row=1, column=2)
assigned_to_entry = ttk.Entry(frame)
assigned_to_entry.grid(row=1, column=3)

ttk.Label(frame, text="Purchase Date:").grid(row=2, column=2)
purchase_date_entry = ttk.Entry(frame)
purchase_date_entry.grid(row=2, column=3)

# Buttons
button_frame = ttk.Frame(root, padding=10)
button_frame.pack(fill="x")

ttk.Button(button_frame, text="Add Asset", command=add_asset).pack(side="left")

tree = ttk.Treeview(root, columns=("ID", "Name", "Category", "Serial", "Status", "Assigned To", "Purchase Date"), show="headings")
for col in tree['columns']:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(fill="both", expand=True)

init_db()
load_assets()
root.mainloop()
