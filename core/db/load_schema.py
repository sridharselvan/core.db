# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

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


db_type = 'sqlite'

if db_type == 'sqlite':
    from core.db.schema import sqlite

def main():
    DataBaseEntity.load_all()
