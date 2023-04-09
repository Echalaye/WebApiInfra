from flask import Flask
import mysql.connector
from mysql.connector import Error
import sys
import json
import decimal

# Connect to MariaDB Platform
try:
    conn = mysql.connector.connect(
        user="django",
        password="django",
        host="10.110.1.15",
        port=3306,
        database="PokemonDB"

    )
except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

app = Flask(__name__)


@app.route("/")
def pokemon():
    cur.execute("SELECT * from pokemon")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        tabVal = []
        for val in result:
            if isinstance(val, decimal.Decimal):
                tabVal.append(float(val))
            else:
                tabVal.append(val)
        newresult = tabVal
        json_data.append(dict(zip(row_headers, newresult)))

    # return the results!
    return json.dumps(json_data)


@app.route("/base_stat")
def baseStat():
    cur.execute("SELECT * from base_stat")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return json.dumps(json_data)


@app.route("/ability")
def ability():
    cur.execute("SELECT * from ability")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return json.dumps(json_data)


@app.route("/pokemon_ability")
def pokemonAbility():
    cur.execute("SELECT * from pokemon_ability")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return json.dumps(json_data)


@app.route("/move")
def move():
    cur.execute("SELECT * from move")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return json.dumps(json_data)


@app.route("/pokemon_move")
def pokemonMove():
    cur.execute("SELECT * from pokemon_move")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return json.dumps(json_data)


@app.route("/type")
def type():
    cur.execute("SELECT * from type")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return json.dumps(json_data)


@app.route("/pokemon_type")
def pokemonType():
    cur.execute("SELECT * from pokemon_type")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return json.dumps(json_data)
