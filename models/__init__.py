#!/usr/bin/python3
"""
0;276;0ccreates a unique FileStorage instance for your application
"""

from os import environ

if environ.get('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
