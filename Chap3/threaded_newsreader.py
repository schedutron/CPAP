#!/usr/bin/env python3
# Still has unicode problems in displaying articles. (Not an error by the way) :(
#this can be made more dynamic
import nntplib, socket, getpass, pydoc, sys, re, pickle, subprocess
from smtplib import SMTP

def display_meaningful(data, string):
    lines = [line.rstrip() for line in data]
    lastBlank = True
    is_indented_code = False #to check whether a whitespace is unnecessary or part of an indented code
    for i in range(len(lines)):
        '''decode because lines are in binary format'''
        try:
            line = lines[i].decode('unicode_escape')
        except (UnicodeDecodeError, OverflowError): #hope this prevents errors
            line = lines[i].decode()

        if line:
            lower = line.lower()
            if (lower.startswith('>')) or\
                lower.startswith('|') or\
                lower.startswith('in article') or\
                lower.endswith('writes:') or\
                lower.endswith('wrote:'):
                    continue
            if not lastBlank or (lastBlank and line): #could be writeen as just lastBlank or line
                if re.match(r'\s', line): #regex to check if the line starts with a whitespace
                    if not is_indented_code:
                        try:
                            if string.endswith(':'): #indentation happens only after a colon (:)
                                is_indented_code = True
                        except Exception:
                            pass
                    if not is_indented_code:
                        line = line.lstrip() #removes the initial unnecessary whitespace
                elif is_indented_code: #if no more indentation occurs, and is_code is still True, it means indented code has ended
                    is_indented_code = False

                string +=  '\n' + repr(line)[1:-1] # Makes line raw. Won't work for tab-indented lines.
                if line:
                    lastBlank = False
                else:
                    lastBlank = True
    return string

def send_msg(subject, personal=False, to=False):
    if not personal:
        #reply to thread or post an article in the newsgroup
        with open('message', 'w') as msg:
            msg.write('From: YOUR_NAME_HERE <blahBlah@blah.org>\n')
            msg.write('Newsgroups: %s\n' % group_name)
            msg.write('Subject: %s\n' % subject)
        subprocess.call(['nano', 'message'])

        with open('message', 'rb') as msg:
            try:
                n.post(msg)
            except EOFError:
                new = nntplib.NNTP(host, user=username, password=passwd)
                rsp, ct, fst, lst, grp = new.group(group_name)
                new.post(msg)
    else:
        #personal reply to the article's author
        email = input("Enter your gmail: ") #sorry for the specific generalization
        email_pass = getpass.getpass("Enter your gmail password: ")

        with open('message', 'w') as msg:
            msg.write('From: YOUR_NAME_HERE <%s>\n' % email)
            msg.write('To: %s\n' % to[0])
            msg.write('Subject: %s\n\n' % subject)
        subprocess.call(['nano', 'message'])
        with open('message', 'rb') as msg:
            msg_to_be_sent = msg.read()

        s = SMTP('smtp.gmail.com')
        s.starttls()
        s.login(email, email_pass)
        errs = s.sendmail(email, to, msg_to_be_sent)
        assert len(errs) == 0, errs #not in book
        s.quit()

        print("Message sent successfully!")

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
    quit()
except nntplib.NNTPPermanentError:
    print("Access denied on server.")
    quit()

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
    quit()

print(n.description(group_name))
print("There are about %s articles available.\n" % ct)

rsp, subjects = n.xhdr('subject', str(fst)+'-'+str(lst))

with open('unwanted.pkl', 'rb') as unwanted:
    unwanted_list = pickle.load(unwanted)

for pair in subjects: #removes unwanted threads
    if pair in unwanted_list:
        subjects.remove(pair)

threads = {} #first mid : articles
#maybe using just the mid's would be more efficient

same_thread = re.compile(r'(?i)(re|fwd?):') #to catch replies, forwards etc
for mid, subject in subjects:
    if same_thread.match(subject):
        for key in threads:
            if threads[key][0][1] == subject[subject.index(' ')+1:]:
                threads[key].append((mid, subject)) #groups with the appropriate 'original' subject
    else:
        threads[mid] = [(mid, subject)]
print() #looks better

for key in threads.keys():
    print(key, threads[key][0][1]) #mid with subject

unlike = input("\nWould you like to 'unlike' one of these threads so that they don't show up again? (y/n) ")
if unlike.lower() == 'y':
    to_be_removed = input("Enter the thread number for the unwanted thread: ")
    with open('unwanted.pkl', 'wb') as unwanted:
        unwanted_list.append((to_be_removed, threads[to_be_removed][0][1]))
        pickle.dump(unwanted_list, unwanted)
    print("Thread '%s' added to unwanted threads." % threads[to_be_removed][0][1])

choice = 'mid' #to initiate the loop
while choice:

    choice = input('\nType the mid of the thread you want to get in, or skip to quit: ')
    if not choice:
        break
    try:
        thread = threads[choice]
    except KeyError:
        print("There is no thread with mid %s." % choice)
    for mid, sub in thread:
        print(mid, sub)
    print()

    while 1:
        ar_num_str = input("Enter an article's number to read it, (next/prev/num) or skip to quit: ")
        if not ar_num_str:
            break
        if ar_num_str == 'next':
            try:
                if ar_ind == len(thread) - 1:
                    ar_ind = 0
                else:
                    ar_ind += 1
            except NameError:
                ar_ind = 0
        elif ar_num_str == 'prev':
            try:
                if ar_ind == 0:
                    ar_ind = len(thread) - 1
                else:
                    ar_ind -= 1
            except NameError:
                ar_ind = len(thread) - 1
        else:
            try:
                ar_num = int(ar_num_str)
                for i in range(len(thread)):
                    if ar_num_str == thread[i][0]:
                        ar_ind = i
                        break
                else:
                    print("Please enter an article number within the current thread.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

        ar_num = thread[ar_ind][0]
        rsp, sub = n.xhdr('subject', ar_num) #or we can access it from thread
        rsp, frm = n.xhdr('from', ar_num)
        rsp, dat = n.xhdr('date', ar_num)

        rsp, body = n.body(ar_num)
        body = body[2]

        string = '%s\n%s-%s\n%s\n' % (frm[0][1], sub[0][0], sub[0][1], dat[0][1])

        string = display_meaningful(body, string)
        pydoc.pager(string)
        wanna_mail = input("Do you want to reply to this article? (y/n) ")
        if wanna_mail.lower() == 'y':
            personal = input("Do you want to personally reply to this article's author? (y/n) ")
            if personal.lower() == 'y':
                to = [frm[0][1][frm[0][1].find('<')+1:-1]]
                send_msg('Re: '+thread[0][1]+'\n', personal=True, to=to)
            else:
                reply_header = 'On ' + dat[0][1] + ', ' + frm[0][1][:frm[0][1].find('<')-1] + ' wrote:\n'
                for line in body:
                    try:
                        reply_header += '> ' + repr(line.decode('unicode_escape'))[1:-1] + '\n' #repr turns the string to raw
                    except UnicodeDecodeError:
                        pass

                rsp_for_id, message_id_for_reply = n.xhdr('message-id', ar_num) #to be used with In-Reply-To header
                send_msg('Re: '
                        +thread[0][1]+'\n'+'References: '
                        +message_id_for_reply[0][1]
                        +'\nIn-Reply-To: '
                        +message_id_for_reply[0][1]
                        + '\n\n'
                        +reply_header
                        )
                print("Article posted!")
    try:
        del ar_ind #for article navigation to work
    except NameError:
        pass

    wanna_mail = input("Do you want to post to this thread? (y/n) ")
    if wanna_mail.lower() == 'y':
        rsp, message_id_stringy = n.xhdr('message-id', thread[0][0]) #to be used with In-Reply-To header
        send_msg('Re: '+thread[0][1]+'\n'+'References: '+message_id_stringy[0][1])
        print("Article posted!")

wanna_mail = input("Do you want to post to this newsgroup? (y/n) ")
if wanna_mail.lower() == 'y':
    send_msg('YOUR_SUBJECT_HERE')
    print("Article posted!")
