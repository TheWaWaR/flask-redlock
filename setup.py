#!/usr/bin/env python
"""
Flask-Redlock
----------------

Example
```````

.. code:: python

    from flask_redlock import RedisLock

    redis_lock = RedisLock()
    redis_lock.init_app(app)

    with redis_lock.lock('something.lock', 3000, retry=10, interval=0.2) as lock:
        if not lock:
            return 'busy!'

        # Do your work here ...

Links
`````

* `Github <https://github.com/TheWaWaR/flask-redlock>`

"""

from setuptools import setup

setup(
    name='Flask-Redlock',
    version='0.0.3',
    url='https://github.com/TheWaWaR/flask-redlock',
    license='MIT',
    author='Qian Linfeng',
    author_email='thewawar@gmail.com',
    description='Adds redis lock support to your Flask application',
    long_description=__doc__,
    packages=['flask_redlock'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'redlock-py>=1.0.8'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ]
)
