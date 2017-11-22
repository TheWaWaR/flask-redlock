# coding: utf-8

import time
from contextlib import contextmanager

from redlock import Redlock


__version__ = '0.0.3'


class LockTimeout(Exception):
    def __init__(self, resource, ttl, retry, interval):
        self.resource
        self.ttl = ttl
        self.retry = retry
        self.interval = interval

    def __repr__(self):
        return 'resource={}, ttl={}, retry={}, interval={}'.format(
            self.resource, self.ttl, self.retry, self.interval
        )


class RedisLock(object):

    def __init__(self, host=None, port=6379, db=None):
        self.host = host
        self.port = port
        self.db = db
        if self.host and self.db:
            self.setup()

    def init_app(self, app):
        self.host = app.config['REDIS_HOST']
        self.port = app.config['REDIS_PORT']
        self.db = app.config['REDIS_DB']
        self.setup()

    def setup(self):
        self.dlm = Redlock([{
            "host": self.host,
            "port": self.port,
            "db": self.db
        }])

    @contextmanager
    def lock(self, resource, ttl, retry=1, interval=0.1):
        the_retry = 0
        while the_retry < retry:
            the_lock = self.dlm.lock(resource, ttl)
            if the_lock:
                break
            the_retry += 1
            time.sleep(interval)
        yield the_lock
        if the_lock:
            self.dlm.unlock(the_lock)
