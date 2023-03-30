import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS customers (id PRIMARYKEY text, name text, dob text, address text, phone text, i int)")

    def Insert(self, id, name, dob, address, phone, i):
        self.dbCursor.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)", (id, name, dob, address, phone, i))
        self.dbConnection.commit()

    def Update(self, name, dob, address, phone, id):
        self.dbCursor.execute("UPDATE customers SET name = ?, dob = ?, address = ?, phone = ? WHERE id = ?", (name, dob, address, phone, id))
        self.dbConnection.commit()

    def Update_Index(self, i):
        self.dbCursor.execute("UPDATE customers SET i = i-1 WHERE i > ?", (i))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM customers WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM customers WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Storage(self):
        self.dbCursor.execute("SELECT * FROM customers")
        records = self.dbCursor.fetchall()
        return records
    
    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()
