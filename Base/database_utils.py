import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='password',
            db='bootcamp'
        )

    def execute_query(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            self.connection.commit()
            return result

    def close_connection(self):
        self.connection.close()

def save_test_result(result):
    db = Database()
    db.execute_query("INSERT INTO task_conclusion (result) VALUES (%s)", (result,))
    db.close_connection()
