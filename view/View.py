import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    def __init__(self,title,geometry,customer_manager):
        super().__init__()
        self.title("Gestión de Clientes")
        self.geometry("1024x768")
        self.customer_manager=customer_manager
    def create_menu(self):
        self.menu_bar = tk.Menu(self)
        customers_menu = tk.Menu(self.menu_bar, tearoff=0)
        customers_menu.add_command(
            label="Dar de alta", command=self.add_customer)
        customers_menu.add_command(
                label="Modificar", command=self.update_customer)
        customers_menu.add_command(
                label="Eliminar", command=self.delete_customer)
        customers_menu.add_command(
                label="Listar todos", command=self.list_all_customers)
        self.menu_bar.add_cascade(label="Clientes", menu=customers_menu)
        self.config(menu=self.menu_bar)

    def create_table_view(self):
        self.table_frame = tk.Frame(self)
        self.table_frame.pack(padx=10, pady=10)

        self.table = ttk.Treeview(self.table_frame,show="headings",columns=(
            "id", "name", "surname", "address"))
        self.table.heading("id", text="Código")
        self.table.heading("name", text="Nombre")
        self.table.heading("surname", text="Apellido")
        self.table.heading("address", text="Dirección")
        self.table.pack()

    def refresh_table(self):
        self.table.delete(*self.table.get_children())
        customers = self.customer_manager.get_all_customers()
        if customers:
            for customer in customers:
                self.table.insert("", "end", values=(
                    customer.id, customer.name, customer.surname, customer.address))
        else:
            self.table.insert("", "end", values=(
                "No hay clientes cargados.", "", "", ""))
            
    def add_customer(self):
        add_window = tk.Toplevel(self)
        add_window.title("Agregar un cliente")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Nombre:").pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Apellido:").pack()
        surname_entry = tk.Entry(add_window)
        surname_entry.pack()

        tk.Label(add_window, text="Dirección:").pack()
        address_entry = tk.Entry(add_window)
        address_entry.pack()

        def save_customer():
            name = name_entry.get()
            surname = surname_entry.get()
            address = address_entry.get()

            customer = Customer(id, name, surname, address)
            self.customer_manager.insert_customer(customer)
            add_window.destroy()
            self.refresh_table()

        tk.Button(add_window, text="Guardar", command=save_customer).pack()

    def delete_customer(self):
        delete_window = tk.Toplevel(self)
        delete_window.title("Eliminar un cliente")
        delete_window.geometry("200x100")

        tk.Label(delete_window, text="Código:").pack()
        id_entry = tk.Entry(delete_window)
        id_entry.pack()

        def delete():
            id = int(id_entry.get())
            self.customer_manager.delete_customer(id)
            delete_window.destroy()
            self.refresh_table()

        tk.Button(delete_window, text="Eliminar", command=delete).pack()

    def update_customer(self):
        update_window = tk.Toplevel(self)
        update_window.title("Modificar un cliente")
        update_window.geometry("300x200")

        tk.Label(update_window, text="Código:").pack()
        id_entry = tk.Entry(update_window)
        id_entry.pack()

        tk.Label(update_window, text="Nombre:").pack()
        name_entry = tk.Entry(update_window)
        name_entry.pack()

        tk.Label(update_window, text="Apellido:").pack()
        surname_entry = tk.Entry(update_window)
        surname_entry.pack()

        tk.Label(update_window, text="Dirección:").pack()
        address_entry = tk.Entry(update_window)
        address_entry.pack()

        def update():
            id = int(id_entry.get())
            customer = self.customer_manager.get_customer(id)
            if customer:
                customer.name = name_entry.get()
                customer.surname = surname_entry.get()
                customer.address = address_entry.get()
                self.customer_manager.update_customer(customer)
                update_window.destroy()
                self.refresh_table()

        tk.Button(update_window, text="Modificar", command=update).pack()

    def list_all_customers(self):
        self.refresh_table()
        customers = self.customer_manager.get_all_customers()
        if customers:
            for customer in customers:
                print(f"Código: {customer.id}")
                print(f"Nombre: {customer.name}")
                print(f"Apellido: {customer.surname}")
                print(f"Dirección: {customer.address}")
                print("-------------------")
        else:
            print("No se encontraron clientes.")

    def quit(self):
        self.customer_manager.close_connection()
        self.destroy()


        

        
