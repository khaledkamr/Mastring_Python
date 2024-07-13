# Databases => SQLite => Training On Everything 
```python []
import sqlite3

def getAllData():

    try: 
        # connect to database
        db = sqlite3.connect("app.db")
        print("connected to database successfully")

        # Setting up the cursor
        cr = db.cursor()

        # Fetch data from database
        cr.execute("select * from users")

        res = cr.fetchall()
        
        print(f"database has {len(res)} rows")
        print("showing data:")

        for row in res:
            print(f"UserID: {row[0]}  ", end = "")
            print(f"Username: {row[1]}")

    except sqlite3.Error as Error:
        print(f"Error reading data {Error}")

    finally:
        if(db):
            # close database connection
            db.close()
            print("connection to database is closed")
    

getAllData()
```
#### Output
```
connected to database successfully
database has 6 rows
showing data:
UserID: 1  Username: ahmed
UserID: 2  Username: ali
UserID: 3  Username: abdo
UserID: 4  Username: tark
UserID: 5  Username: ibrahim
UserID: 6  Username: khaled
connection to database is closed
```