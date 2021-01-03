Flask-MySQL
===========

Flask-MySQL is a `Flask <http://flask.pocoo.org/>`_ extension that allows you to access a MySQL database.

You can report bugs and discuss features on the `issues page <https://github.com/cyberdelia/flask-mysql/issues>`_.


Installation
------------

Use pip to install ``flask-mysql`` : ::

  pip install flask-mysql


Configuration
-------------

To configure access to your MySQL database server by using these settings :

.. tabularcolumns:: |p{6.5cm}|p{8.5cm}|

================================= =========================================
``MYSQL_DATABASE_HOST``            default is 'localhost'
``MYSQL_DATABASE_PORT``            default is 3306
``MYSQL_DATABASE_USER``            default is None
``MYSQL_DATABASE_PASSWORD``        default is None
``MYSQL_DATABASE_DB``              default is None
``MYSQL_DATABASE_CHARSET``         default is 'utf-8'
================================= =========================================

Usage
-----

Initialize the extension : ::

  from flaskext.mysql import MySQL
  mysql = MySQL()
  mysql.init_app(app)

Obtain a cursor : ::

  cursor = mysql.get_db().cursor()

Multiple connection example: ::

  from flaskext.mysql import MySQL
  
  mysql_1 = MySQL(app, prefix="mysql1", host=os.getenv("db_host"), user=os.getenv("db_username"),password=os.getenv("db_pass"),db=os.getenv("db_name), autocommit=True, cursorclass=pymysql.cursors.DictCursor)
  mysql_2 = MySQL(app, prefix="mysql2", host="host2", user="UN", passwd="&&", db="DB",autocommit=True,cursorclass=pymysql.cursors.DictCursor)

  @app.route('/')
  @app.route('/index')
  def hello():
      cursor1 = mysql_1.get_db().cursor()
      #...
      cursor2 = mysql_2.get_db().cursor()
      #...
