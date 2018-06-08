# -*- coding: utf-8 -*-
from __future__ import print_function
import os

from sqlite3 import dbapi2 as sqlite
import yaml

from core import DB
from core.models import *

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # read yaml file
    config = None
    yaml_file = current_dir + '/env.yaml'
    with open(yaml_file, 'r') as f:
        config = yaml.load(f)

    db_master = config['db_master'][0]
    db = DB()
    db.connect('sqlite+pysqlite:///file.db', module=sqlite)
    sess = db.get_session()
    engine = db.get_engine()

    # create tables
    if not engine.dialect.has_table(engine, User.__table__.__str__()):
        User.__table__.create(engine)

    # insert data
    user = User(email='test@example.com', first_name='First', last_name='Last')
    sess.add(user)

    # query
    user = sess.query(User).first()
    print(user)
