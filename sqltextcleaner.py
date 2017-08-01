import pymysql
import re
from nltk.corpus import stopwords

class textFormatter:
    def __init__(self):
        self.connect()
        self.pattern = re.compile('[\W_]+')
        self.stopwords = stopwords.words('english')

    def connect(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = "Wertcool123",
            db = 'resources',
            port = 3306
        )

        self.cursor = self.conn.cursor()



    def pullPushWords(self, table, colName):
        self.cursor.execute("SELECT id, {} FROM {}".format(colName, table))
        num = 10;
        for row in self.cursor.fetchall():
            lowerStr = row[1].lower()
            editedStr = self.pattern.sub(" ", lowerStr)
            wordList = editedStr.split(' ')
            newWordList = []
            for word in wordList:
                if len(word)>=3 and word not in self.stopwords:
                    newWordList.append(word)
            newText = " ".join(newWordList)

            self.cursor.execute("UPDATE {} SET {}=\'{}\' WHERE id=\'{}\'".format(table,colName, newText, row[0]))
            self.conn.commit()



    def close(self):
        self.cursor.close()
        self.conn.close()

    def main(self,table, *args):
        for arg in args:
            self.pullPushWords(table, arg)

        self.close()



if __name__ == '__main__':
    formatter = textFormatter()
    formatter.main("files", 'keywords')
