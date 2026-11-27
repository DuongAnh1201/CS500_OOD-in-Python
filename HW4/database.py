import sqlite3
class Database:
    def __init__(self, db_file: str):
        self.__conn = sqlite3.connect(db_file)

    def db_query(self, query, params):
        cursor = self.__conn.cursor()
        cursor.execute(query, params)
        self.__conn.commit()
        return cursor.fetchall()

    def create_tables(self,table_name: str, params = {}) -> None:
        columns = ""
        for name, col_type in params.items():
            columns += f", {name} {col_type}"
        columns = columns [2::] 
        sql = f"""CREATE TABLE IF NOT EXISTS {table_name} ({columns})"""
        self.db_query(sql, params)
        print()

    def close(self) -> None:
        self.__conn.close()


def main():
    db = Database("test.db")
    
    db.create_tables("guide_skill", {
    "guide_id": "TEXT PRIMARY KEY",
    "first_name": "TEXT NOT NULL",
    "last_name": "TEXT NOT NULL",
    "age": "INTEGER",
    "phone": "TEXT",
    "certified": "INTEGER",          # SQLite has no bool: store 0 / 1
})
    db.db_query(
    "INSERT INTO guide_skill (guide_id, first_name, last_name, age, phone, certified) VALUES (?, ?, ?, ?, ?, ?)",
    ("G001", "Duong Anh", "Nguyen", 20, "XXX", 123),
)

if __name__ =="__main__":
    main()