""""Define DBStorage class"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from os import environ


class DBStorage:
    """Defines storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        database = environ.get('HBNB_MYSQL_DB')

        database_url = "mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, database)

        self.__engine = create_engine(database_url, pool_pre_ping=True)
        if environ.get('HBNB_ENV') == 'test':
            Base.MetaData.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}
        class_list = [State, City]

        if cls:
            class_list = [cls]

        for cls in class_list:
            table = cls.__table__
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj

        return objects

    def new(self, obj):
        """add the object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """commit changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current db session obj if not None"""
        if obj:
            self.__session.delete(obj)
            session.commit()

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
