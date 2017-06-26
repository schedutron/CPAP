#!/usr/bin/env python3

import nntplib, socket, getpass, pydoc, sys

def find(query, string):
    is_there = False
    for chunk in query: #OR
        chunk_qualified = False
        for word in chunk: #AND
            if word not in string:
                break
        else:
            chunk_qualified = True

        if chunk_qualified:
            is_there = True
            break

    return is_there

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
print("There are about %s articles available.\n" % ct)
print("""You can search through both the article bodies and subjects.
Use AND and OR accordingly:
subject
body
subject OR body
subject AND body""")
search_type = input("Type your choice: ")
print("""\nNow enter keywords to get relevant articles, and you can use
AND and OR here as well (and you can skip this to get all the articles).""")
search = input("Keywords: ")

both = False #for search type
either = False
chunks = search_type.split('OR')
if len(chunks) != 1:
    either = True
else:
    chunks = search_type.split('AND')
    if len(chunks) != 1:
        both = True

if not (either or both):
    if search_type.lower() == 'subject':
        in_subject = True
    else:
        in_body = True

if search:
    query = search.split(' OR ')
    query = [phrase.split(' AND ') for phrase in query]
    count = fst
    subjects = []
    while count <= lst:
        rsp, subject = n.xhdr('subject', count)
        #print("Sub:-----", subject)
        #get the relvant articles
        if not (either or both):
            if in_subject:
                if find(query, subject[0][1]):
                    subjects.append(subject[0])
            else:
                rsp, body = n.body(count)
                body = body[2]
                if find(query, body):
                    subjects.append(subject[0])
        elif either:
            if find(query, subject[0][1]):
                subjects.append(subject[0])
            else:
                rsp, body = n.body(count)
                body = body[2]
                if find(query, body):
                    subjects.append(subject[0])
        #both
        else:
            flag = False
            if find(query, subject[0][1]):
                rsp, body = n.body(count)
                body = body[2]
                if find(query, body):
                    subjects.append(subject[0])

        count += 1

        '''
        we can also save the matching bodies, but that would take a lot
        of memory. Instead, a body would be loaded only if the user is
        interested.
        '''
else:
    rsp, subjects = n.xhdr('subject', str(fst)+'-'+str(lst))

print("\nThere are %s relevant subjects available:\n" % len(subjects))

for mid, sub in subjects: #message id, subjects
    print(mid, sub)
print() #looks better

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
