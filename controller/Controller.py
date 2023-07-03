from entidad.Customer import Customer

class Controller:
    def __init__(self,view,model):
        self.view=view
        self.model=model
        self.view.set_controller(self)
    def createCustomer(self,name,surname,address):
     customer = Customer(id, name, surname, address)
     self.model.insert_customer(customer)
    def deleteCustomer(self,id):
         customer = self.model.get_customer(id)
         if customer:
                self.model.delete_customer(id)
    def updateCustomer(self,id,name,surname,address):
        customer = self.model.get_customer(id)
        if customer:
                customer.name = name
                customer.surname = surname
                customer.address = address
                self.model.update_customer(customer)
    def getAllCustomers(self):
            return self.model.get_all_customers()
    def getCustomer(self,id):
            return self.model.get_customer(id)
      

      
