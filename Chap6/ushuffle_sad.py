#!/usr/bin/env python3

import time
from distutils.log import warn as printf
from os.path import dirname
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT  # Okay only in Python3 :(
from random import randrange as rand
from sqlalchemy import Column, Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base

from password import PASSWORD
from ushuffle_dbU import DBNAME, NAMELEN, randName, FIELDS, tformat, cformat,\
RDBMSs, scanf

DSNs = {
    'mysql': 'mysql://root@localhost/%s/%s' % (DBNAME, PASSWORD),
    'sqlite': 'sqlite:///:memory:',
    'postgresql': 'postgresql+psycopg2://binaryBoy:%s@localhost/%s' % (PASSWORD, DBNAME)
}

Base = declarative_base()
class Users(Base):
    __tablename__ = 'users'
    login = Column(String(NAMELEN))
    userid = Column(Integer, primary_key=True)
    projid = Column(Integer)
    def __str__(self):
        return ''.join(map(tformat, (self.login, self.userid, self.projid)))


class SQLAlchemyTest(object):
    def __init__(self, dsn):
        try:
            eng = create_engine(dsn)
        except ImportError:
            raise RuntimeError()
        
        try:
            eng.connect()
        except exc.OperationalError:
            eng = create_engine(dirname(dsn))
            conn = eng.connect()
            try:
                conn.connection.connection.set_isolation_level(0)
                conn.execute('CREATE DATABASE %s' % DBNAME).close()
                conn.connection.connection.set_isolation_level(1)
            except exc.OperationalError:
                raise RuntimeError()
            
            eng = create_engine(dsn)
        
        Session = orm.sessionmaker(bind=eng)
        self.ses = Session()
        self.users = Users.__table__
        self.eng = self.users.metadata.bind = eng

    def insert(self):
        self.ses.add_all(Users(login=who, userid=userid, projid=rand(1, 5)) \
            for who, userid in randName()
        )
    
    def update(self):
        fr = rand(1, 5)
        to = rand(1, 5)
        i = self.ses.query(
            Users
        ).filter_by(projid=fr).update({'projid':to})
        
        self.ses.commit()
        return fr, to, i

    def delete(self):
        rm = rand(1, 5)
        i = self.ses.query(
            Users
        ).filter_by(projid=rm).delete()
        self.ses.commit()
        return rm, i

    def dbDump(self, newest5=False):
        printf("\n%s" % ''.join(map(cformat, FIELDS)))
        if not newest5:
            users = self.ses.query(Users).all()
        else:
            users = self.ses.query(Users).order_by(Users.userid.desc())[:5]  # I don't see any need of offset here.
        for user in users:
            printf(user)
        self.ses.commit()
    
    def __getattr__(self, attr):
        return getattr(self.users, attr)

    def finish(self):
        self.ses.connection().close()
    

def setup():
    return RDBMSs[scanf(
    '''
    Choose a database system:

    (M)ySQL
    (G)adfly
    (S)QLite
    (P)ostgreSQL

    Enter choice: ''').strip().lower()[0]]


def main():
    printf("*** Connect to %r database" % DBNAME)
    db = setup()
    if db not in DSNs:
        printf("\nERROR: %r not supported, exit" % db)
        return

    try:
        orm = SQLAlchemyTest(DSNs[db])
    except RuntimeError:
        printf("\nERROR: %r not supported, exit" % db)
        return

    printf("\n*** Create users table (drop old one if appl.)")
    orm.drop(checkfirst=True)
    orm.create()

    printf("\n*** Insert names into table")
    orm.insert()
    orm.dbDump()
    print("\n*** Top 5 newest employees")
    orm.dbDump(newest5=True)

    printf("\n*** Move users to a random group")
    fr, to, num = orm.update()
    
    printf("\t(%d users moved) from (%d) to (%d)" % (num, fr, to))
    orm.dbDump()

    printf("\n*** Randomly delete group")
    start_time = time.time()
    rm, num = orm.delete()
    end_time = time.time()
    print("Time taken: %s" % (end_time - start_time))
    printf("\t(group #%d; %d users removed)" % (rm, num))
    orm.dbDump()

    printf("\n Drop users table")
    orm.drop()
    printf("\n*** Close cxns")
    orm.finish()

if __name__ == "__main__":
    main()