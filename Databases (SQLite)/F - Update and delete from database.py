# ---------------------------------------------
# -- Database => SQLite => Update and Delete --
# ---------------------------------------------

import sqlite3

db = sqlite3.connect("app.db")
cr = db.cursor()

# Update data
cr.execute("update users set name = 'khaled' where user_id = 1")
cr.execute("update users set name = 'ahmed' where user_id = 2")

# Delete Data
cr.execute("delete from users where user_id = 3")

cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

db.commit()
db.close()