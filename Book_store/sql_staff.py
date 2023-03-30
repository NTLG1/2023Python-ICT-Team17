import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS staff (id PRIMARYKEY text, name text, dob text, address text, phone text, salary int, index i)")

    def Insert(self, id, name, dob, address, phone, salary, i):
        self.dbCursor.execute("INSERT INTO staff VALUES (?, ?, ?, ?, ?, ?, ?)", (id, name, dob, address, phone, salary, i))
        self.dbConnection.commit()

    def Update(self, name, dob, address, phone, salary, id):
        self.dbCursor.execute("UPDATE staff SET name = ?, dob = ?, address = ?, phone = ?, salary = ? WHERE id = ?", (name, dob, address, phone, salary, id))
        self.dbConnection.commit()

    def Update_Index(self, i):
        self.dbCursor.execute("UPDATE staff SET i = i-1 WHERE i > ?", (i, ))
        self.dbConnection.commit()

    def Update_salary(self,salary,id):
        self.dbCursor.execute("UPDATE staff SET salary = ? WHERE id = ?", (salary, id))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM staff WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM staff WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Storage(self):
        self.dbCursor.execute("SELECT * FROM staff")
        records = self.dbCursor.fetchall()
        return records

    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()