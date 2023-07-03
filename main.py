# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import sqlite3

from controller.CustomerManager import CustomerManager
from view.View import View


class Application():
    def __init__(self,title,geometry):
        super().__init__() 
        self.customer_manager = CustomerManager()
        self.view= View(title,geometry,self.customer_manager)
        self.view.create_menu()
        self.view.create_table_view()
        self.view.refresh_table()

##Iniciar la aplicación:
if __name__ == "__main__":
    app = Application("Prueba","1024x768")
    app.view.mainloop()
