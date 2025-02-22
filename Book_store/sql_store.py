import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS store (id PRIMARYKEY text, name text, address text, phone text)")

    def Insert(self, id, name, address, phone):
        self.dbCursor.execute("INSERT INTO store VALUES (?, ?, ?, ?)", (id, name, address, phone))
        self.dbConnection.commit()

    def Update(self, name, address, phone, id):
        self.dbCursor.execute("UPDATE store SET name = ?, address = ?, phone = ?, id = ?", (name, address, phone, id))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM store WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM store WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Storage(self):
        self.dbCursor.execute("SELECT * FROM store")
        records = self.dbCursor.fetchall()
        return records

    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()