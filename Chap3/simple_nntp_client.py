#!/usr/bin/env python3

import nntplib, socket, getpass, pydoc, sys

print("Welcome to your NNTP client!")
host = input("Enter hostname: ")
username = input("Enter username (skip this to do an anonymous login): ")
if not username:
    username = None
    passwd = None
else:
    passwd = getpass.getpass()

try:
    n = nntplib.NNTP(host, user=username, password=passwd)
except socket.gaierror:
    print("Unable to reach host.")
    sys.exit()
except nntplib.NNTPPermanentError:
    print("Access denied on server.")
    sys.exit()

#get list of newsgroups
rsp, g_list = n.list()

prompt = "There are %s newsgroups available. Do you want to have listed them out? (y/n) " % len(g_list)
see = input(prompt)
if see.lower() == 'y':
    for item in g_list:
        print(item[0])

#ask for group name to get in
group_name = input("Enter the group name you want to get in: ")
try:
    rsp, ct, fst, lst, grp = n.group(group_name)
except nntplib.NNTPTemporaryError:
    print("Cannot load group.")
    print("Server may require authentication.")
    sys.exit()

print(n.description(group_name))
print("There are about %s articles available." % ct)

search = input("Enter space-separated keywords to get relevant articles (you can skip this to get all the articles): ").split()

if search:
    count = fst
    subjects = []
    while count <= lst:
        rsp, subject = n.xhdr('subject', count)

        #get the relvant subjects
        for word in search:
            if word in subject:
                subjects.append((count, subject))
                break
        else:
            body = n.body(count)
            for word in search:
                if word in body:
                    subjects.append((count, subject))
                    break
        count += 1

        '''
        we can also save the matching bodies, but that would take a lot
        of memory. Instead, a body would be loaded only if the user is
        interested.
        '''
else:
    rsp, subjects = n.xhdr('subject', str(fst)+'-'+str(lst))

print("There are %s relevant subjects available:" % len(subjects))

for mid, sub in subjects: #message id, subjects
    print(mid, sub)

choice = 'sub' #just to initiate
while choice:
    choice = input("Which article would you like to read now? Provide it's message id, or skip to quit: ")
    for mid, sub in subjects:
        if str(mid) == choice:
            #diplay article in separate page
            stuff = n.article(mid) #by the way we can load the article without checking the mid

            '''
            we could've used the string join method (that would've been faster),
            but we had to check each part for potential unicode errors, hence the loops.
            '''

            string = '%s\n%s\n' % (stuff[1][0], stuff[1][1])
            for line in stuff[1][2]:
                try:
                    string += line.decode('unicode_escape') + '\n'
                except UnicodeDecodeError:
                    pass
            pydoc.pager(string)
            break

print("Thank you.")
