from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask + MySQL app running inside Docker!"

@app.route('/data')
def data():
    try:
        conn = mysql.connector.connect(
            host="mysql-db",
            user="root",
            password="rootpass",
            database="testdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

