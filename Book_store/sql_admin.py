import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS admin (id PRIMARYKEY text, name text, dob text, phone text, index int)")

    def Insert(self, id, name, dob, phone, index):
        self.dbCursor.execute("INSERT INTO admin VALUES (?, ?, ?, ?, ?)", (id, name, dob, phone, index))
        self.dbConnection.commit()

    def Update(self, name, dob, phone, id):
        self.dbCursor.execute("UPDATE admin SET name = ?, dob = ?, phone = ? WHERE id = ?", (name, dob, phone, id))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM admin WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM admin WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Storage(self):
        self.dbCursor.execute("SELECT * FROM admin")
        records = self.dbCursor.fetchall()
        return records
    
    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()
