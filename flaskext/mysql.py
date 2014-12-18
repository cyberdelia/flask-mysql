# -*- coding: UTF-8 -*-
from __future__ import absolute_import
import MySQLdb

try:
    from flask import _app_ctx_stack as _ctx_stack
except ImportError:
    from flask import _request_ctx_stack as _ctx_stack

class MySQL(object):
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        self.app = app
        self.app.config.setdefault('MYSQL_DATABASE_HOST', 'localhost')
        self.app.config.setdefault('MYSQL_DATABASE_PORT', 3306)
        self.app.config.setdefault('MYSQL_DATABASE_USER', None)
        self.app.config.setdefault('MYSQL_DATABASE_PASSWORD', None)
        self.app.config.setdefault('MYSQL_DATABASE_DB', None)
        self.app.config.setdefault('MYSQL_DATABASE_CHARSET', 'utf8')
        self.app.config.setdefault('MYSQL_USE_UNICODE', True)
        #Flask 0.9 or later
        if hasattr(app, 'teardown_appcontext'):
            self.app.teardown_request(self.teardown_request)
        #Flask 0.7 to 0.8
        elif hasattr(app, 'teardown_request'):
            self.app.teardown_request(self.teardown_request)
        #Older versions
        else:
            self.app.after_request(self.teardown_request)

    def connect(self):
        kwargs = {}
        if self.app.config['MYSQL_DATABASE_HOST']:
            kwargs['host'] = self.app.config['MYSQL_DATABASE_HOST']
        if self.app.config['MYSQL_DATABASE_PORT']:
            kwargs['port'] = self.app.config['MYSQL_DATABASE_PORT']
        if self.app.config['MYSQL_DATABASE_USER']:
            kwargs['user'] = self.app.config['MYSQL_DATABASE_USER']
        if self.app.config['MYSQL_DATABASE_PASSWORD']:
            kwargs['passwd'] = self.app.config['MYSQL_DATABASE_PASSWORD']
        if self.app.config['MYSQL_DATABASE_DB']:
            kwargs['db'] = self.app.config['MYSQL_DATABASE_DB']
        if self.app.config['MYSQL_DATABASE_CHARSET']:
            kwargs['charset'] = self.app.config['MYSQL_DATABASE_CHARSET']
        if self.app.config['MYSQL_USE_UNICODE']:
            kwargs['use_unicode'] = self.app.config['MYSQL_USE_UNICODE']
        return MySQLdb.connect(**kwargs)

    def teardown_request(self, exception):
        ctx = _ctx_stack.top
        if hasattr(ctx, "mysql_db"):
            ctx.mysql_db.close()

    def get_db(self):
        ctx = _ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, "mysql_db"):
                ctx.mysql_db = self.connect()
            return ctx.mysql_db
