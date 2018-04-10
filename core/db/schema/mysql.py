# -*- coding: utf-8 -*-

"""

    Module :mod:``


    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
from core.db import DataBaseEntity
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


MYSQL_SUBSTITUTE = {
    'auto_increment': 'AUTO_INCREMENT',
    'primary_key': 'PRIMARY KEY',

    'type_integer': 'INTEGER',
    'type_string': 'VARCHAR',
    'type_datetime': 'DATETIME',
    'type_timestamp': 'TIMESTAMP',

    'uniq': 'UNIQUE',
    'default': 'DEFAULT',
    'not_null': 'NOT NULL',

    'cur_timestamp': 'CURRENT_TIMESTAMP',
}


DataBaseEntity(
    query=(
        '''CREATE TABLE $tablename'''
        '''('''
        '''    SCHEDULE_TYPE_IDN $type_integer $auto_increment $primary_key, '''
        '''    SCHEDULE_TYPE $type_string(10) $not_null, '''
        '''    CRT_DT $type_timestamp $default $cur_timestamp $not_null, '''
        '''    UPD_DT $type_timestamp $default $cur_timestamp ON UPDATE $cur_timestamp $not_null '''
        ''')'''
    ),
    desc='''Create table: $tablename''',
    params = {
        'tablename': 'CODE_SCHEDULE_TYPE',
    }
)


DataBaseEntity(
    query=('''INSERT INTO CODE_SCHEDULE_TYPE (SCHEDULE_TYPE, CRT_DT, UPD_DT) '''
           '''VALUES ('OneTime',$cur_timestamp,$cur_timestamp)'''),
    desc='''--> Data Load for CODE_SCHEDULE_TYPE table'''
)

DataBaseEntity(
    query=('''INSERT INTO CODE_SCHEDULE_TYPE (SCHEDULE_TYPE, CRT_DT, UPD_DT) '''
           '''VALUES ('Daily',$cur_timestamp,$cur_timestamp)'''),
    desc='''--> Data Load for CODE_SCHEDULE_TYPE table'''
)

DataBaseEntity(
    query=('''INSERT INTO CODE_SCHEDULE_TYPE (SCHEDULE_TYPE, CRT_DT, UPD_DT) '''
           '''VALUES ('Weekly',$cur_timestamp,$cur_timestamp)'''),
    desc='''--> Data Load for CODE_SCHEDULE_TYPE table'''
)


DataBaseEntity(
    query=(
        '''CREATE  TABLE $tablename'''
        '''('''
        '''    STATUS_IDN $type_integer $primary_key $auto_increment $not_null,'''
        '''    STATUS $type_string(10) $not_null $uniq ,'''
        '''    CRT_DT $type_timestamp $default $cur_timestamp $not_null, '''
        '''    UPD_DT $type_timestamp $default $cur_timestamp ON UPDATE $cur_timestamp $not_null '''
        ''')'''
    ),
    desc='''Create table: $tablename''',
    params = {
        'tablename': 'CODE_STATUS',
    }
)


DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('success',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)
DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('failure',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)
DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('error',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)
DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('loggedin',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)
DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('loggedout',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)
DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('timedout',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)
DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('initiated',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)
DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('inprocess',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)
DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('completed',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)
DataBaseEntity(
    query='''INSERT INTO CODE_STATUS (STATUS,CRT_DT,UPD_DT) VALUES ('missed',$cur_timestamp,$cur_timestamp)''',
    desc='''--> Data Load for CODE_STATUS table'''
)


DataBaseEntity(
    query=(
        '''CREATE TABLE $tablename'''
        '''('''
        '''    USER_IDN $type_integer $primary_key $auto_increment $not_null,'''
        '''    FIRST_NAME $type_string(25) $not_null,'''
        '''    LAST_NAME $type_string(25),'''
        '''    USER_NAME $type_string(25) $not_null,'''
        '''    HASH1 $type_string(64) $not_null,'''
        '''    HASH2 $type_string(64),'''
        '''    PHONE_NO1 $type_integer $not_null,'''
        '''    PHONE_NO2 $type_integer,'''
        '''    EMAIL_ID $type_string(50),'''
        '''    CRT_DT $type_timestamp $default $cur_timestamp $not_null, '''
        '''    UPD_DT $type_timestamp $default $cur_timestamp ON UPDATE $cur_timestamp $not_null, '''
        '''    IS_ACTIVE $type_integer $default 1'''
        ''')'''
    ),
    desc='''Create table: $tablename''',
    params={
        'tablename': 'USER'
    }
)


DataBaseEntity(
    query='''INSERT INTO USER (FIRST_NAME, LAST_NAME, USER_NAME, HASH1, PHONE_NO1) VALUES ('a','a','YQ==', 'YQ==', 1)''',
    desc='''--> User a created CODE_STATUS table'''
)


DataBaseEntity(
    query=(
        '''CREATE  TABLE $tablename'''
        '''('''
        '''    USER_SESSION_IDN $type_integer $primary_key $auto_increment $not_null,'''
        '''    USER_IDN $type_integer $not_null, '''
        '''    CLIENT_IP $type_string(12) $not_null,'''
        '''    BROWSER_NAME $type_string(100),'''
        '''    BROWSER_VERSION $type_string(100),'''
        '''    ATTEMPTED_ON $type_timestamp $not_null $default $cur_timestamp,'''
        '''    STATUS_IDN $type_integer $not_null,'''
        '''    IS_ACTIVE $type_integer $default 1,'''
        '''    UNIQUE_SESSION_CD $type_string(50),'''
        '''    FOREIGN KEY(user_idn) REFERENCES USER(USER_IDN),'''
        '''    FOREIGN KEY(status_idn) REFERENCES CODE_STATUS(STATUS_IDN)'''
        ''')'''
    ),
    desc='''Create table: $tablename''',
    params={
        'tablename': 'USER_SESSION'
    }
)


DataBaseEntity(
    query=(
        '''CREATE TABLE $tablename'''
        '''('''
        '''    USER_ACTIVITY_IDN $type_integer $primary_key $auto_increment $not_null, '''
        '''    IS_AUTHORIZED $type_integer $not_null, '''
        '''    CRT_DT $type_timestamp $default $cur_timestamp $not_null, '''
        '''    STATUS_IDN $type_integer $not_null, '''
        '''    USER_SESSION_IDN $type_integer $not_null, '''
        #'''    FOREIGN KEY(USER_IDN) REFERENCES USER(USER_IDN),'''
        '''    FOREIGN KEY(STATUS_IDN) REFERENCES CODE_STATUS(STATUS_IDN),'''
        '''    FOREIGN KEY(USER_SESSION_IDN) REFERENCES USER_SESSION(USER_SESSION_IDN)'''
        ''')'''
    ),
    desc='''Create table: $tablename''',
    params={
        'tablename': 'USER_ACTIVITY'
    }
)


DataBaseEntity(
    query=(
        '''CREATE TABLE $tablename'''
        '''('''
        '''    JOB_DETAILS_IDN $type_integer $primary_key $auto_increment $not_null $uniq, '''
        '''    JOB_ID $type_string(50) $not_null, '''
        '''    SCHEDULE_TYPE_IDN $type_integer $not_null, '''
        '''    START_DATE $type_timestamp $not_null, '''
        '''    RECURRENCE $type_string(200), '''
        '''    DAY_OF_WEEK $type_string(25), '''
        '''    PARAMS $type_string(100), '''
        '''    NEXT_RUN_TIME $type_string(25), '''
        '''    IS_ACTIVE $type_integer $not_null $default 1, '''
        '''    USER_IDN $type_integer $not_null, '''
        '''    CRT_DT $type_timestamp $default $cur_timestamp $not_null, '''
        '''    UPD_DT $type_timestamp $default $cur_timestamp ON UPDATE $cur_timestamp $not_null, '''
        '''    FOREIGN KEY(USER_IDN) REFERENCES USER(USER_IDN), '''
        '''    FOREIGN KEY(SCHEDULE_TYPE_IDN) REFERENCES CODE_SCHEDULE_TYPE(SCHEDULE_TYPE_IDN)'''
        ''')'''
    ),
    desc='''Create table: $tablename''',
    params={
        'tablename': 'JOB_DETAILS',
    }
)


DataBaseEntity(
    query=(
        '''CREATE TABLE $tablename'''
        '''('''
        '''    JOB_RUN_LOG_IDN $type_integer $primary_key $auto_increment $not_null $uniq, '''
        '''    JOB_ID $type_string(50) $not_null, '''
        '''    STATUS_IDN $type_integer $not_null, '''
        '''    MESSAGE $type_string(500), '''
        '''    ERROR_TRACE $type_string(500),'''
        '''    CRT_DT $type_timestamp $default $cur_timestamp $not_null, '''
        '''    UPD_DT $type_timestamp $default $cur_timestamp ON UPDATE $cur_timestamp $not_null, '''
        #'''    FOREIGN KEY(JOB_ID) REFERENCES JOB_DETAILS(JOB_ID),'''
        '''    FOREIGN KEY(STATUS_IDN) REFERENCES CODE_STATUS(STATUS_IDN)'''
        ''')'''
    ),
    desc='''Create table: $tablename''',
    params={
        'tablename': 'JOB_RUN_LOG'
    }
)
