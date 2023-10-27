class Diary:
    def __init__(self,contact="",phone=0,email=""):
        self.__contact = contact
        self.__phone = phone
        self.__email = email
        self.contacts = []
    
    @property
    def contact(self):
        return self.__contact
    
    @contact.setter
    def contact(self,value):
        self.__contact = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value
    
    def add_contact(self):
        contacts_tuple = (self.__contact,self.__phone,self.__email)
        self.contacts.append(contacts_tuple)
    
    def view_contacts(self):
        return self.contacts
    
    def search_contact(self,value):
        for contacts_tuple in self.contacts:
            if value in contacts_tuple:
                return contacts_tuple
        return None

    def modify_contact(self,value):
        for position,contacts_tuple in enumerate(self.contacts):
            if value in contacts_tuple:
                verification_1 = input("Desea cambiar el nombre? S/N ").upper()
                if verification_1 == "S":
                    new_name = input("Ingrese el nuevo nombre: ").title()
                else:
                    new_name = self.__contact
                verification_2 = input("Desea cambiar el numero? S/N ").upper()
                if verification_2 == "S":
                    new_phone = input("Ingrese el nuevo numero: ")
                else:
                    new_phone = self.__phone
                verification_3 = input("Desea cambiar el correo? S/N ").upper()
                if verification_3 == "S":
                    new_email = input("Ingrese el nuevo correo: ")
                else:
                    new_email = self.__email.title()

                self.contacts[position] = (new_name, new_phone, new_email)

                return f"Contacto modificado: {contacts_tuple} -> {(new_name, new_phone, new_email)}"
    
        return "Contacto no encontrado"
