#!/usr/bin/env python3

import nntplib, socket, re

HOST = 'news.aioe.org'
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

    #to get the first available article. Using simply fst doesn't work.
    rng = "%s-%s" % (fst, fst)
    rsp, frm = n.xhdr('from', rng)
    count = 0
    while not frm:
        count += 1
        n = nntplib.NNTP(HOST)
        rsp, ct, fst, lst, grp = n.group(GRNM)
        rng = "%s-%s" % (fst+count, fst+count)
        rsp, frm = n.xhdr('from', rng)

    #now that a 'from' header has been found, get other things
    rsp, sub = n.xhdr('subject', rng)
    rsp, dat = n.xhdr('date', rng)
    print('''*** Found first article (#%s):

    From: %s
    Subject: %s
    Date: %s
    ''' % (fst+count, frm[0][1], sub[0][1], dat[0][1]))

    rsp, data = n.body(fst+count)
    ''' book has rsp, anum, mid, data --but that doesn't work as of this writing
        instead, anum and mid are present in data, which is a tuple(at index 0 and 1 respectively)
    '''
    displayFirst20(data[2])
    n.quit()

def displayFirst20(data):
    print("*** First (<=20) meaningful lines:\n")
    #print("\n\n-*-*-*-*- check\n\n%s\n\n" % str(data))
    count = 0
    lines = [line.rstrip() for line in data]
    lastBlank = True
    is_indented_code = False #to check whether a whitespace is unnecessary or part of an indented code
    for i in range(len(lines)):
        '''decode because lines are in binary format'''
        try:
            line = lines[i].decode('unicode_escape')
        except UnicodeDecodeError: #hope this prevents errors
            line = lines[i].decode()

        if line:
            lower = line.lower()
            if (lower.startswith('>') and not lower.startswith('>>>')) or\
                lower.startswith('|') or\
                lower.startswith('in article') or\
                lower.endswith('writes:') or\
                lower.endswith('wrote:'):
                    continue
            if not lastBlank or (lastBlank and line): #could be writeen as just lastBlank or line
                if re.match(r'\s', line): #regex to check if the line starts with a whitespace
                    if not is_indented_code:
                        try:
                            try:
                                previous = lines[i-1].decode('unicode_escape')
                            except (UnicodeDecodeError, OverflowError):
                                previous = lines[i-1].decode()
                            if previous.startswith(':'): #indentation happens only after a colon (:)
                                is_indented_code = True
                        except IndexError:
                            pass

                    if not is_indented_code:
                        line = line.lstrip() #removes the initial unnecessary whitespace
                elif is_indented_code: #if no more indentation occurs, and is_code is still True, it means indented code has ended
                    is_indented_code = False

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
