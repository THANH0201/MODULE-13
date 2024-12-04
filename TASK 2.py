import mariadb
import json
from flask import Flask, Response
#from flask_cors import CORS

app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

conn = mariadb.connect(
    host='127.0.0.1',
    port=3307,
    database='flightgame',
    user='root',
    password='123456',
    autocommit=True
)

@app.route('/airport/<icao>')
def get_airport(icao):
    sql = '''
    SELECT ident as 'icao', name, municipality 
    FROM airport 
    WHERE ident = %s
    '''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)