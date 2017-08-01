import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = "Wertcool123",
    db = 'resources',
    port = 3306
)

cur = conn.cursor()

cur.execute("SELECT  id title keywords from files")
print (cur.description)

num = 0

while num < 2:
    res = cur.fetchall()
    print(res)
    num = num + 1

cur.close()
conn.close()
