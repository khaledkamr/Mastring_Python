# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------

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