import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS books (id PRIMARYKEY text, title text, genre text, author text, year text, quantity int, target_audience text, price int, i int)")

    def Insert(self, id, title, genre, author, year, quantity, target_audience, price, i):
        self.dbCursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, title, genre, author, year, quantity, target_audience, price, i))
        self.dbConnection.commit()

    def Update(self, title, genre, author, year, quantity, target_audience, price, id):
        self.dbCursor.execute("UPDATE books SET title = ?, genre = ?, author = ?, year = ?, quantity = ? WHERE id = ?", (title, genre, author, year, quantity, target_audience, price, id))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM books WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM books WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Storage(self):
        self.dbCursor.execute("SELECT * FROM books")
        records = self.dbCursor.fetchall()
        return records

    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()