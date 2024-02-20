#!/usr/bin/python3
"""
Creates a unique FileStorage instance for your application
"""

from os import environ

# get storage type from ENVIRON
storage_type = environ.get("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
