#!/usr/bin/env python3

from distutils.log import warn as printf
from random import randrange as rand
import couchdb
from ushuffle_dbU import randName, FIELDS, tformat, cformat

DBNAME = 'test_users'

class CouchTest(object):
    def __init__(self):
        try:
            self.couch = couchdb.Server()
            del self.couch[DBNAME]
        except couchdb.http.ResourceNotFound:
            try:
                self.users = self.couch.create(DBNAME)
            except couchdb.http.ResourceNotFound:
                raise RuntimeError()
        else:
            self.users = self.couch.create(DBNAME)

    
    def insert(self):
        for who, uid in randName():
            self.users.save(
            dict(login=who, userid=uid, projid=rand(1, 5))
            )
    
    def update(self):
        fr = rand(1, 5)
        to = rand(1, 5)
        i = -1
        for uid in self.users:
            user = self.users[uid]
            if user['projid'] == fr:
                user['projid'] = to
                self.users.save(user)
                i += 1
        return fr, to, i+1

    def delete(self):
        rm = rand(1, 5)
        i = -1
        for uid in self.users:
            user = self.users[uid]
            if user['projid'] == rm:
                self.users.delete(user)
                i += 1
        return rm, i+1

    def dbDump(self):
        printf("\n%s" % "".join(map(cformat, FIELDS)))
        for user in self.users:
            printf("".join(map(tformat, (self.users[user][k] for k in FIELDS))))
    
    def finish(self):
        del self.couch  # Can't find a proper method to disconnect.
    

def main():
    printf("*** Connect to %r database" % DBNAME)
    try:
        couch = CouchTest()
    except RuntimeError:
        printf("\nERROR: MongoDB server unreachable, exit")
        return

    printf("\n*** Insert names into table")
    couch.insert()
    couch.dbDump()

    printf("\n*** Move users to a random group")
    fr, to, num = couch.update()
    printf("\t(%d users moved) from (%d) to (%d)" % (num, fr, to))
    couch.dbDump()

    printf("\n*** Randomly delete group")
    rm, num = couch.delete()
    printf("\t(group #%d; %d users removed)" % (rm, num))
    couch.dbDump()

    printf("\n*** Drop users table")
    del couch.couch[DBNAME]
    printf("\n*** Close cxns")
    couch.finish()

if __name__ == "__main__":
    main()
