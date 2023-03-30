# Staff ID: str
# Staff name: str
# DoB: str
# Address: str
# Phone number: str
# Salary
# (Staff level)

#Can: Modify books info, input books, see books & store info, see & modify customers list

class Staff:
    def __init__(self, id, name, dob, address, phone, salary):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__address = address
        self.__phone = phone
        self.__salary = salary
    
    def set_id(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_dob(self, dob):
        self.__dob = dob
    
    def get_dob(self):
        return self.__dob
    
    def set_addr(self, address):
        self.__address = address
    
    def get_addr(self):
        return self.__address
    
    def set_phone(self, phone_num):
        self.__phone = phone_num
    
    def get_phone_num(self):
        return self.__phone
    
    #For admins
    def set_salary(self, salary):
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary    
    
    #Only staff & admin available, don't need this
    #def set_level(self):
    #    print(f"Choose staff level: \n
    #          1. ")
        