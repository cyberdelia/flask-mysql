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

