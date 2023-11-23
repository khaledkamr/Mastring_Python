
import sqlite3

db = sqlite3.connect("skills app.db")
cr = db.cursor()
cr.execute("CREATE TABLE if not exists Users (name TEXT, id INTEGER)")
cr.execute("CREATE TABLE if not exists skills (name TEXT, progress INTEGER, id INTEGER)")

def commit_close():
    db.commit()
    db.close()
    print("connection to database is closed")

uid = 1

inputMsg = """
What do you want to do?
'S' -> Show all skils
'A' -> Add new skill
'D' -> Delete skill
'U' -> Update skill progress
'Q' -> Quit the app
Choose option: 
"""
userInput = input(inputMsg).strip().capitalize()

commandsList = ['S', 'A', 'D', 'U', 'Q']

def show_skills():

    cr.execute(f"select * from skills where id = '{uid}'")
    res = cr.fetchall()
    print(f"you have {len(res)} skills")

    if (len(res) > 0):
        print(f"showing skills with progress:")
    
    for row in res:
        print(f"skill -> {row[0]:8}  ", end = "")
        print(f"progress -> {row[1]}%")
    
    commit_close()

def add_skill():

    sk = input("write skill name: ").strip().capitalize()

    cr.execute(f"select name from skills where name = '{sk}' and id = '{uid}'")
    res = cr.fetchone()

    if (res == None):
        prog = input("write skill progress: ").strip()
        cr.execute(f"insert into skills(name, progress, id) values('{sk}', '{prog}', '{uid}')")
    else:
        print("skill is exists, you can't add it")
        choise = input("would you like to update the skill?")

        if(choise == "yes"):
            prog = input("write the new skill progress ").strip()
            cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and id = '{uid}'")
        else:
            quit_app()

    commit_close()

def delete_skill():

    sk = input("write skill name: ").strip().capitalize()

    cr.execute(f"select * from skills where id = '{uid}'")
    skills = cr.fetchall()

    if (sk in skills):
        cr.execute(f"delete from skills where name = '{sk}' and id = '{uid}'")
    else:
        print("there is no such skill")
    
    commit_close()

def update_skill():

    sk = input("write skill name: ").strip().capitalize()
    prog = input("write the new skill progress ").strip()
    cr.execute(f"select * from skills where id = '{uid}'")
    skills = cr.fetchall()

    if (sk in skills):
        cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and id = '{uid}'")
    else:
        print("there is no such skill")
    
    commit_close()

def quit_app():
    
    commit_close()

if userInput in commandsList:

    if(userInput == 'S'):
        show_skills()
    elif(userInput == 'A'):
        add_skill()
    elif(userInput == 'D'):
        delete_skill()
    elif(userInput == 'U'):
        update_skill()
    else:
        print("App is closed")
else:
    print(f"Sorry command {userInput} not found")
