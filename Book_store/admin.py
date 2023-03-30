#ID
#Name
#DoB
#Phone

#Can: Modify Staffs, modify store info, input staff, see staff info, see books & store info

class Admin:
    def __init__(self, id, name, dob, phone):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__phone = phone

    def get_id(self):
        return self.__id
    
        
