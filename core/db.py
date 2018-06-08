from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DB:
    def __init__(self, *args, **kwargs):
        self.sess = None
        self.engine = None

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def connect(self, *args, **kwargs):
        self.engine = create_engine(*args, **kwargs)
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.sess = Session()

    def get_session(self):
        return self.sess

    def get_engine(self):
        return self.engine
