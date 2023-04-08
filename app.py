from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('/home/krisanov/project/skachki/data/skachki.db')
c = db.cursor()

c.execute("""
SELECT * FROM jockeys""")
all_jockeys = c.fetchall()

c.execute("""
SELECT * FROM horses""")
all_horses=c.fetchall()

c.execute("""
SELECT * FROM battles""")
all_battles=c.fetchall()

db.close()

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/append', methods=['POST', 'GET'])
def append():
    if request.method == "POST":
        name=request.form.get('name', type=str)
        age=request.form.get('age', type=int)
        address=request.form.get('address', type=str)

        name_horse=request.form.get('name_horse', type=str)
        age_horse=request.form.get('age_horse', type=int)
        pol=request.form.get('pol', type=str)

        battle=request.form.get('battle', type=str)
        hippodrome=request.form.get('hippodrome', type=str)
        date=request.form.get('date', type=str)
        if name and age and address:
            with sqlite3.connect('skachki.db') as db:
                c = db.cursor()
                # Добавь блок трай, для добавления в бд
                # хотя пох
                c.execute('INSERT INTO jockeys (name,address,age) VALUES (?,?,?)',
                (name,address,age)          
                )
                db.commit()
                flash="Успешно добавили жокея!"
            return redirect('jockeys')
        if name_horse and age_horse and pol:
            with sqlite3.connect('skachki.db') as db:
                c = db.cursor()
                c.execute('INSERT INTO horses (name,pol,age) VALUES (?,?,?)',
                (name_horse,pol,age_horse)          
                )
                db.commit()
            return redirect('horses')
        if battle and hippodrome and date:
            with sqlite3.connect('skachki.db') as db:
                c = db.cursor()
                c.execute('INSERT INTO battles (battle,date,hippodrome) VALUES (?,?,?)',
                (battle,date,hippodrome)          
                )
                db.commit()
            return redirect('battles')
    else:
        return render_template('append.html')

@app.route('/jockeys')
def jockeys():
    jockeys=[]
    for j in all_jockeys:
        # капец дурацкий синтаксис для отображения на стр
        jockeys.append({"name": j[0], "age":j[2], "address":j[1]})
    return render_template('jockeys.html', jockeys=jockeys)

@app.route('/horses')
def horses():
    horses=[]
    for h in all_horses:
        horses.append({"name": h[0], "age":h[2], "address":h[1]})
    return render_template('horses.html', horses=horses)

@app.route('/battles')
def battles():
    battles=[]
    for h in all_battles:
        battles.append({"battle": h[0], "hipodrom":h[2], "date":h[1]})
    return render_template('battles.html', battles=battles)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='5010')
