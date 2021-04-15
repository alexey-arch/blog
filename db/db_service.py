import pymysql

class DbService:
    instance = None
    connection = None
    cursor = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.connection = pymysql.connect(
                host='127.0.0.1',
                user='userdb',
                password='Fks#23Pq12%Dbvr',
                db='blog',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            cls.cursor = cls.connection.cursor()
        return cls.instance

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

        return self.cursor.description 

    def close(self):
        if self.cursor is not None:
            self.cursor.close()

        if self.connection is not None:
            self.connection.close()

if __name__ == '__main__':
    print('Вы запустили этот модуль напрямую!')

        