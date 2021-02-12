from flask import Flask, render_template
import mysql.connector as mariadb
import yaml

app = Flask(__name__)
db = yaml.load(open('db.yaml'))

config = {
    'user':     db['mariadb_user'],
    'password': db['mariadb_password'],
    'host':     db['mariadb_host'],
    'database': db['mariadb_db']
}


@app.route('/')
def index():
    return render_template('index.html')

# Return all ingredients in a table
@app.route('/ingredients', )
def ingredients():
    try:
        print("In try block")
        connection = mariadb.connect(**config)
        print("made connection")
        cur = connection.cursor()
        print("created cursor")
        cur.execute('SELECT * FROM ingredients')
        print("Executed")
        #connection.commit()
        #print("commited")
        ingredients = cur.fetchall()
        print("fetchedall")
        return render_template('ingredients.html',ingredients=ingredients)
    except:
        return "error"

if __name__ == '__main__':
    app.run(host='192.168.1.63',debug=True)

