import sqlite3


class DatabaseTutorial:
    def __init__(self):
        self.database = "kuna.db"

    def create_databse(self):
        cr = sqlite3.connect(self.database)
        # conn_str = cr.cursor()
        return cr

    def create_table(self, conn_str, sql):
        conn_str.execute(sql)

    def insert_data(self,conn_str, sql):
        conn_str.execute(sql)
        conn_str.commit()


db_conn = DatabaseTutorial()
conn_str = db_conn.create_databse()
# db_conn.create_table(conn_str, "CREATE TABLE kuna (NAME VARCHAR(20))")
db_conn.insert_data(conn_str, "INSERT INTO kuna values ('happy')")