# -*- coding: utf-8 -*-

from flaskext.mysql import MySQL
from flask import Flask, json


app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'passwd'
app.config['MYSQL_DATABASE_DB'] = 'test'

@app.route('/')
def get_root():
  cursor = mysql.get_db().cursor()
  cursor.execute('select * from t1')
  return json.dumps(cursor.fetchone())


if __name__ == '__main__':
  app.run()
