# -*- coding: utf-8 -*-

"""

    Module :mod:``


    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
__import__('pkg_resources').declare_namespace(__name__)

from string import Template
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
import sqlite3
import pymysql

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
from core.utils.environ import get_main_db_details
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


main_db_details = get_main_db_details()

DB_TYPE = main_db_details['type']
DATABASE_NAME = main_db_details['name']


def create_session():
    """."""

    Session = sessionmaker()

    if DB_TYPE == 'sqlite':
        engine = create_engine('sqlite:///{}'.format(main_db_details['path']))

    elif DB_TYPE == 'mysql':
        engine = create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}'.format(
                main_db_details['username'],
                main_db_details['password'],
                main_db_details['host'],
                main_db_details['port'],
                main_db_details['name']
            )
        )

    Session.configure(bind=engine)

    return Session()


class DataBaseEntity(object):
    """."""
    instances = list()

    def __init__(self, query, pre_query='', desc='', params=None):
        """."""

        self.query = query
        self.pre_query = pre_query or None
        self.description = desc
        self.params = params if params else dict()

        self.__class__.instances.append(self)

    @classmethod
    def load_all(cls, DB_TYPE='primary_db'):

        if DB_TYPE == 'sqlite':
            import sqlite3 as sqlite
            connection = sqlite.connect(main_db_details['path'])

            cursor = connection.cursor()

            for each in cls.instances:
                if each.pre_query:
                    print 'performing PRE-PROCESS for {}... '.format(each.description),
                    try:
                        cursor.execute(each.pre_query)
                    except:
                        print 'FAILURE'
                    else:
                        print 'SUCCESS'

                print 'performing PROCESS for {}... '.format(each.description),
                try:
                    cursor.execute(each.query)
                except:
                    print 'FAILURE'
                else:
                    print 'SUCCESS'

            connection.commit()

        if DB_TYPE == 'mysql':

            from core.db.schema.mysql import MYSQL_SUBSTITUTE

            db = pymysql.connect("localhost","root","SivaCnSugi@123")

            cursor = db.cursor()

            cursor.execute('DROP DATABASE IF EXISTS {}'.format(DATABASE_NAME))
            cursor.execute('CREATE DATABASE {}'.format(DATABASE_NAME))
            cursor.execute('USE {}'.format(DATABASE_NAME))

            for each in cls.instances:
                _desc = Template(each.description).safe_substitute(each.params) if each.description else ''
                if each.pre_query:

                    query = Template(each.pre_query).safe_substitute(MYSQL_SUBSTITUTE)
                    query = Template(query).safe_substitute(each.params)

                    print '{}... '.format(_desc),
                    try:
                        cursor.execute(query)
                    except Exception as error:
                        print 'FAILURE: {}'.format(str(error))
                        db.rollback()
                    else:
                        print 'SUCCESS'
                        db.commit()

                print '{}... '.format(_desc),
                try:
                    query = Template(each.query).safe_substitute(MYSQL_SUBSTITUTE)
                    query = Template(query).safe_substitute(each.params)

                    cursor.execute(query)

                except Exception as error:
                    print 'FAILURE: {}'.format(str(error))
                    db.rollback()
                else:
                    print 'SUCCESS'
                    db.commit()


def main():

    if DB_TYPE == 'sqlite':
        from core.db.schema import sqlite

    elif DB_TYPE == 'mysql':
        from core.db.schema import mysql

    else:
        raise Exception('Invalid Database Type: {}'.format(DB_TYPE))

    DataBaseEntity.load_all(DB_TYPE)
