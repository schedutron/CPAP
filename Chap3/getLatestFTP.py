#!/usr/bin/env python3
import ftplib, os, socket
HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print("ERROR: cannot reach '%s'" % HOST)
        return
    print("*** Connected to '%s'" % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print("ERROR: cannot login anonymously")
        f.quit()
        return
    print("*** Logged in as 'anonymous'")

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print("ERROR: cannot cd to '%s'" % DIRN)
        f.quit()
        return

    print("*** Changed to '%s' folder" % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print("ERROR: cannot read file '%s'" % FILE)
        os.unlink(FILE)
    else:
        print("Downloaded '%s' to CWD" % FILE)
    f.quit()
    return

if __name__ == "__main__":
    main()
