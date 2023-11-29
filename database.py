import sqlite3
class DB:
    def __init__(self):
        self.con = sqlite3.connect("database.sqlite")
        self.cursor = self.con.cursor()

    def get_user(self, user_id):
        try:
            self.cursor.execute("""SELECT name FROM users WHERE user_id = ?""", [user_id])
        except:
            return 0
        return 1

    def add_user(self, user_id, name):
        with self.con:
            return self.cursor.execute("""INSERT INTO users (user_id, name) VALUES (?, ?)""", [user_id, name])

    def add_to_laba(self, user_id, laba):
        with self.con:
            name = self.cursor.execute("""SELECT name FROM users WHERE user_id=(?)""", [user_id]).fetchone()[0]
            return self.cursor.execute(f"""INSERT INTO {laba} (user_id, name) VALUES (?, ?)""", [user_id, name])

    def delete_from_laba(self, user_id, laba):
        with self.con:
            if laba == 1:
                return self.cursor.execute("""DELETE FROM laba1 WHERE user_id=(?)""", [user_id])
            if laba == 2:
                return self.cursor.execute("""INSERT INTO laba2 (user_id) VALUES (?)""", [user_id])
            if laba == 3:
                return self.cursor.execute("""INSERT INTO laba3 (user_id) VALUES (?)""", [user_id])
            if laba == 4:
                return self.cursor.execute("""INSERT INTO laba4 (user_id) VALUES (?)""", [user_id])
            if laba == 5:
                return self.cursor.execute("""INSERT INTO laba5 (user_id) VALUES (?)""", [user_id])

    def show_queue(self, laba):
        with self.con:
            if laba == 1:
                return self.cursor.execute("""SELECT * FROM laba1""").fetchall()
            if laba == 2:
                return self.cursor.execute("""SELECT * FROM laba2""").fetchall()
            if laba == 3:
                return self.cursor.execute("""SELECT * FROM laba3""").fetchall()
            if laba == 4:
                return self.cursor.execute("""SELECT * FROM laba4""").fetchall()
            if laba == 5:
                return self.cursor.execute("""SELECT * FROM laba5""").fetchall()

