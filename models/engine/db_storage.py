#!/usr/bin/python3
"""defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from os import getenv


class DBStorage:
    """ class storage
    Attributes: __engine, __session
    """
    __engine = None
    __session = None

    def __init__(self):
        """funct doc"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """querie on the currect database session"""
        objects_dictionary = {}

        if cls is None:
            objects_list = self.__session.query(State).all()
            objects_list.extend(self.__session.query(City).all())
            objects_list.extend(self.__session.query(User).all())
            objects_list.extend(self.__session.query(Place).all())
            objects_list.extend(self.__session.query(Review).all())
            objects_list.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects_list = self.__session.query(cls).all()

        for obj in objects_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects_dictionary[key] = obj

        return objects_dictionary

    def new(self, obj):
        """adds new object to the current db"""
        self.__session.add(obj)

    def save(self):
        """commits changes of the current db"""

        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current db"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""

        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()

    def close(self):
        """closes the session"""
        self.__session.close()
