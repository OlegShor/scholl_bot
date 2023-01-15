import sqlite3

def sql_start():
    global db, cur
    db = sqlite3.connect('test1.db')
    cur = db.cursor()
    if db:
        print("db contct")
    cur.execute("""CREATE TABLE IF NOT EXISTS admin(tmid PRIMARY KEY , name)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS techer(tmid PRIMARY KEY , name)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS student(tmid PRIMARY KEY , name)""")
    db.commit()

async def sql_add_admin(state):
    async with state.proxy() as data:
        if tuple(data.values())[0] == 'admin':
            cur.execute("""INSERT INTO admin VALUES(?, ?)""", tuple(data.values())[1:3])
        elif tuple(data.values())[0] == 'techer':
            cur.execute("""INSERT INTO teacher VALUES(?, ?)""", tuple(data.values())[1:3])
        elif tuple(data.values())[0] == 'student':
            cur.execute("""INSERT INTO student VALUES(?, ?)""", tuple(data.values())[1:3])
        db.commit()

def admin_chek(id):
    id = [id]
    b = cur.execute("select tmid from admin where tmid = ?", id).fetchone()
    if b != None:
        return 1
    else:
        return 0
