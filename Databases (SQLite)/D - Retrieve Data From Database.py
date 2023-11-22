# --------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# --------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# - fetchmany(size) => returns a number of record = size or None if no more rows are available.
# ------------------------------------------------------

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

users = ["ahmed", "ali", "abdo", "tark", "ibrahim", "khaled"]

for key, user in enumerate(users):

    cr.execute(f"insert into users(user_id, name) values({key + 1}, '{user}')")

# Fetch Data
cr.execute("select user_id, name from users")
print(cr.fetchone())
print(cr.fetchone())
print("=" * 50)
print(cr.fetchmany(2))
print("=" * 50)
print(cr.fetchall())

# Save (Commit) Changes
db.commit()

# Close Database
db.close()