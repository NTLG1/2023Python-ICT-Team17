#ID
#Title
#Genre
#Author
#Year of publication
#Target audience: Children(3-16)😭, Young adults(17-30), Middle-aged adults(31-45), Old adults(>45)
#(Date of importation)
#(Import) quantity
#Price

class Book:
    def __init__(self, id, title, genre, author, year, quantity, target_audience, price):
        self.__id = id
        self.__title = title
        self.__genre = genre
        self.__author = author
        self.__pub_year = year
        self.__quantity = quantity
        self.__target_audience = target_audience
        self.__price = price
        
    def set_id(self, id):
        self.__id = id
        
    def get_id(self):
        return self.__id
    
    def set_title(self, title):
        self.__title = title
    
    def get_title(self):
        return self.__title
    
    def set_genre(self, genre):
        self.__genre = genre
    
    def get_genre(self):
        return self.__genre
    
    def set_author(self, author):
        self.__author = author
    
    def get_author(self):
        return self.__author
    
    def set_year(self, year):
        self.__pub_year = year
    
    def get_pub_year(self):
        return self.__pub_year
    
    def set_quantity(self, quantity):
        self.__quantity = quantity
    
    def get_quantity(self):
        return self.__quantity
    
    def set_target(self):
        print(f"Choose the target audience of this book:\n"
              f"1. Children (3-16) \n"
              f"2. Young adults (17-30) \n"
              f"3. Middle-aged adults (30-45) \n"
              f"4. Old adults (Above 45) \n")
        op = int(input(f"Your choice: "))
        match op:
            case 1:
                self.__target_audience = "Children"
            case 2:
                self.__target_audience = "Young adults"
            case 3:
                self.__target_audience = "Middle-aged adults"
            case 4:
                self.__target_audience = "Old adults"
            case _:
                print(f"Invalid choice!")
                
    def get_target(self):
        return self.__target_audience
    
    def set_price(self):
        price = int(input("Enter price (VND): "))
        self.__price = price
        
    def get_price(self):
        return self.__price
    
        
    
    