# -*- coding: UTF-8 -*-
from __future__ import absolute_import
import MySQLdb
import sqlalchemy.pool as pool

from flask import _request_ctx_stack


class MySQL(object):
    def __init__(self, app=None, pooled=False, max_overflow=10, pool_size=5):
        self.pooled = pooled
        self.max_overflow = max_overflow
        self.pool_size = pool_size
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
        self.app.teardown_request(self.teardown_request)
        self.app.before_request(self.before_request)
        if self.pooled:
            self.pooled_connection()

    def pooled_connection(self):
        self.pool = pool.QueuePool(self.connect, 
                                   max_overflow=self.max_overflow, 
                                   pool_size=self.pool_size)

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

    def before_request(self):
        ctx = _request_ctx_stack.top
        if self.pooled:
          ctx.mysql_db = self.pool.connect()
        else:
          ctx.mysql_db = self.connect()

    def teardown_request(self, exception):
        ctx = _request_ctx_stack.top
        if hasattr(ctx, "mysql_db"):
            ctx.mysql_db.close()

    def get_db(self):
        ctx = _request_ctx_stack.top
        if ctx is not None:
            return ctx.mysql_db
