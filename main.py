from models.db import DB

db = DB()

print(db.conn.cursor('select 1'))