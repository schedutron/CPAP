#!/usr/bin/env python3

import nntplib, socket

HOST = 'nntp.aioe.org'
GRNM = 'comp.lang.python'
#USER = 'someUserName' --just in case authentication is required
#PASS = 'somePass'

def main():
    try:
        n = nntplib.NNTP(HOST)
        #, user=USER, password=PASS) --if authentication required
    except socket.gaierror as e:
        print("ERROR: cannot reach host '%s'" % HOST)
        print(' ("%s")' % eval(str(e))[1]) #what's the need of eval? Why not just str(e)? This itself creates another error
        return
    except nntplib.NNTPPermanentError as e:
        print("ERROR: access denied on '%s'" % HOST)
        print(' ("%s")' % str(e))
        return
    print("*** Connected to host '%s'" % HOST)

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError as ee:
        print("Error: cannot load group '%s'" % GRNM)
        print(' ("%s")' % str(ee)) #book had e instead of ee, perhaps printing error in book
        print(" Server may require authentication")
        print(" Uncomment/edit login line above")
        n.quit()
        return
    except nntplib.NNTPTemporaryError as ee: #this is exactly the above exception! But book has it! Maybe the order matters here
        print("ERROR: group '%s' unavailable" % GRNM)
        print(' ("%s")' % str(ee)) #book used e instead of ee
        n.quit()
        return
    print("*** Found newsgroup '%s'" % GRNM)

    rng = "%s-%s" % (lst, lst)
    rsp, frm = n.xhdr('from', rng)
    rsp, sub = n.xhdr('subject', rng)
    rsp, dat = n.xhdr('date', rng)
    print('''*** Found last article (#%s):

    From: %s
    Subject: %s
    Date: %s
    ''' % (lst, frm[0][1], sub[0][1], dat[0][1]))

    rsp, data = n.body(lst)
    ''' book has rsp, anum, mid, data --but that doesn't work as of this writing
        instead, anum and mid are present in data, which is a tuple(at index 0 and 1 respectively)
    '''
    displayFirst20(data[2])
    n.quit()

def displayFirst20(data):
    print("*** First (<=20) meaningful lines:\n")
    #print("\n\n-*-*-*-*- check\n\n%s\n\n" % str(data))
    count = 0
    lines = (line.rstrip() for line in data)
    lastBlank = True
    for line in lines:
        line = line.decode('unicode_escape')
        '''decode because lines are in binary format, unicode_escape used to avoid potential
        "can't decode" error(s)'''
        if line:
            lower = line.lower()
            if (lower.startswith('>') and not lower.startswith('>>>')) or\
                lower.startswith('|') or\
                lower.startswith('in article') or\
                lower.endswith('writes:') or\
                lower.endswith('wrote:'):
                    continue
            if not lastBlank or (lastBlank and line): #could be writeen as just lastBlank or line
                print(' %s' % line)
                if line:
                    count += 1
                    lastBlank = False
                else:
                    lastBlank = True
            if count == 20:
                break
if __name__ == "__main__":
    main()
