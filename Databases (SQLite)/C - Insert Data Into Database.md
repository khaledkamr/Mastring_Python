# Databases => SQLite => Insert Data Into Database 
- cursor => All Operation in SQL Done By Cursor Not The Connection Itself
- commit => Save All Changes
```python []
# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

# Create The Tables and Fields
cr.execute("CREATE TABLE if not exists users (user_id INTEGER, name TEXT)")
cr.execute("CREATE TABLE if not exists skills (name TEXT, progress INTEGER, user_id INTEGER)")

# Inserting Data
cr.execute("insert into users(user_id, name) values(1, 'khaled')")
cr.execute("insert into users(user_id, name) values(2, 'yossif')")
cr.execute("insert into users(user_id, name) values(3, 'yassen')")

users = ["ahmed", "ali", "abdo", "tark", "ibrahim", "khaled"]
for key, user in enumerate(users):
    cr.execute(f"insert into users(user_id, name) values({key + 1}, '{user}')")

# Save (Commit) Changes
db.commit()

# Close Database
db.close()
```