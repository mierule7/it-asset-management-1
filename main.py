import tkinter as tk
from tkinter import ttk, messagebox

class AssetManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IT Asset Management")
        self.root.geometry("600x400")

        # Asset List
        self.assets = []

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry Fields
        tk.Label(self.root, text="Asset Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.asset_name_entry = tk.Entry(self.root)
        self.asset_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Asset Type:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.asset_type_entry = tk.Entry(self.root)
        self.asset_type_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Purchase Date:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.purchase_date_entry = tk.Entry(self.root)
        self.purchase_date_entry.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(self.root, text="Add Asset", command=self.add_asset).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Delete Selected", command=self.delete_selected).grid(row=4, column=0, columnspan=2, pady=10)

        # Treeview for displaying assets
        self.asset_tree = ttk.Treeview(self.root, columns=("Name", "Type", "Date"), show="headings")
        self.asset_tree.heading("Name", text="Asset Name")
        self.asset_tree.heading("Type", text="Asset Type")
        self.asset_tree.heading("Date", text="Purchase Date")
        self.asset_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Scrollbar for Treeview
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.asset_tree.yview)
        self.asset_tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=5, column=2, sticky="ns")

    def add_asset(self):
        name = self.asset_name_entry.get().strip()
        asset_type = self.asset_type_entry.get().strip()
        purchase_date = self.purchase_date_entry.get().strip()

        if not name or not asset_type or not purchase_date:
            messagebox.showerror("Error", "All fields are required!")
            return

        self.assets.append((name, asset_type, purchase_date))
        self.asset_tree.insert("", "end", values=(name, asset_type, purchase_date))

        # Clear entry fields
        self.asset_name_entry.delete(0, tk.END)
        self.asset_type_entry.delete(0, tk.END)
        self.purchase_date_entry.delete(0, tk.END)

    def delete_selected(self):
        selected_item = self.asset_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No item selected!")
            return

        for item in selected_item:
            self.asset_tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssetManagementApp(root)
    root.mainloop()