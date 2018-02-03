# -*- coding: utf-8 -*-

"""

    Module :mod:``


    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
import sqlite3 as sqlite
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
from core.db import DataBaseEntity
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


conn = sqlite.connect(r"db.sqlite")
conn.close()


DataBaseEntity(
    query='''PRAGMA foreign_keys = ON;''',
    desc='''pre condition'''
)


DataBaseEntity(
    query=(
        '''CREATE TABLE IF NOT EXISTS user ('''
        '''user_idn INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'''
        '''first_name varchar(25) NOT NULL,'''
        '''last_name varchar(25),'''
        '''user_name varchar(25) NOT NULL,'''
        '''hash1 VARCHAR(64) NOT NULL,'''
        '''hash2 VARCHAR(64),'''
        '''phone_no1 number NOT NULL,'''
        '''phone_no2 number,'''
        '''email_id varchar(50),'''
        '''crt_dt DATETIME,'''
        '''upd_dt DATETIME,'''
        '''is_active number(1) DEFAULT 1)'''
    ),
    desc='''Create User table''',
    pre_query='''DROP TABLE IF EXISTS USER'''
)


DataBaseEntity(
    query=(
        '''CREATE  TABLE  IF NOT EXISTS "main"."code_status" ('''
        '''status_idn INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,'''
        '''status VARCHAR NOT NULL  UNIQUE ,'''
        '''crt_dt DATETIME NOT NULL  DEFAULT CURRENT_TIMESTAMP,'''
        '''upd_dt DATETIME NOT NULL)'''
    ),
    desc='''Create code_status table''',
    pre_query='''DROP TABLE IF EXISTS CODE_STATUS'''
)


DataBaseEntity(
    query='''INSERT INTO "main"."code_status" ("status","crt_dt","upd_dt") VALUES ('success',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);'''
)
DataBaseEntity(
    query='''INSERT INTO "main"."code_status" ("status","crt_dt","upd_dt") VALUES ('failure',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);'''
)
DataBaseEntity(
    query='''INSERT INTO "main"."code_status" ("status","crt_dt","upd_dt") VALUES ('error',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);'''
)
DataBaseEntity(
    query='''INSERT INTO "main"."code_status" ("status","crt_dt","upd_dt") VALUES ('loggedin',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);'''
)
DataBaseEntity(
    query='''INSERT INTO "main"."code_status" ("status","crt_dt","upd_dt") VALUES ('loggedout',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);'''
)
DataBaseEntity(
    query='''INSERT INTO "main"."code_status" ("status","crt_dt","upd_dt") VALUES ('timedout',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);'''
)


DataBaseEntity(
    query=(
        '''CREATE  TABLE  IF NOT EXISTS "main"."user_session" ('''
        '''"user_session_idn" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,'''
        '''"user_idn" INTEGER NOT NULL ,'''
        '''"client_ip" VARCHAR NOT NULL ,'''
        '''"browser_name" VARCHAR,'''
        '''"browser_version" VARCHAR,'''
        '''"attempted_on" DATETIME NOT NULL  DEFAULT CURRENT_TIMESTAMP,'''
        '''"status_idn" INTEGER NOT NULL,'''
        '''"is_active" INTEGER DEFAULT 1'''
        '''"unique_session_cd" VARCHAR DEFAULT (null),'''
        '''    FOREIGN KEY(user_idn) REFERENCES user(user_idn),'''
        '''    FOREIGN KEY(status_idn) REFERENCES code_status(status_idn))'''
    ),
    desc='''Create user_session table''',
    pre_query='''DROP TABLE IF EXISTS USER_SESSION'''
)


DataBaseEntity(
    query=(
        '''CREATE  TABLE  IF NOT EXISTS "main"."user_activity" ('''
        '''user_activity_idn INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,'''
        '''is_authorized INTEGER NOT NULL ,'''
        '''crt_dt DATETIME NOT NULL  DEFAULT CURRENT_TIMESTAMP,'''
        '''status_idn INTEGER NOT NULL ,'''
        '''user_session_idn INTEGER NOT NULL,'''
        #'''FOREIGN KEY(user_idn) REFERENCES user(user_idn),'''
        '''    FOREIGN KEY(status_idn) REFERENCES code_status(status_idn),'''
        '''    FOREIGN KEY(user_session_idn) REFERENCES user_session(user_session_idn))'''
    ),
    desc='''Create user_activity table''',
    pre_query='''DROP TABLE IF EXISTS USER_ACTIVITY'''
)
