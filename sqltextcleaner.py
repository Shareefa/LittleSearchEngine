import pymysql

class textFormatter:
    def __init__(self):
        self.connect()
        self.name = 'bob'


    def out(self):
        print(self.name)

    def connect(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = "Wertcool123",
            db = 'resources',
            port = 3306
        )

        self.cursor = self.conn.cursor

    def editText():
        pass

if __name__ == '__main__':
    formatter = textFormatter()
    formatter.out()
