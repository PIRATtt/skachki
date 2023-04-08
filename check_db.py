import sqlite3

db = sqlite3.connect('/home/krisanov/project/skachki/data/skachki.db')
c = db.cursor()

print(c.execute("""SELECT * FROM chance""").fetchall())

listTables=c.execute("""
SELECT name FROM sqlite_master WHERE type='table';
""").fetchall()

newlist=[]
for l in listTables:
    newlist.append(l[0])

if 'jockeys' in  newlist and 'horses' in newlist and 'battles' in newlist:
    print('Table is good!')
else:
    print('Error table!!!')

db.commit()
db.close()
