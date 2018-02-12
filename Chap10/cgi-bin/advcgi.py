#!/usr/bin/env python

from cgi import FieldStorage
from os import environ
from cStringIO import StringIO
from urllib import quote, unquote

class AdvCGI(object):
    header = 'Content-Type: text/html\n\n'
    url = '/cgi-bin/advcgi.py'

    formhtml = '''<html><head><title>
    Advanced CGI Demo</title></head>
    <body><h2>Advanced CGI Demo Form</h2>
    <form method=post action="%s" enctype="multipart/form-data">
    <h3>My Cookie Setting</h3>
    <li><code><b>CPPuser = %s</b></code>
    <h3>Enter cookie value<br>
    <input name=cookie value="%s"> (<i>optional</i>)</h3>
    <h3>Enter your name<br>
    <input name=person value="%s"> (<i>required</i>)</h3>
    <h3>What languages can you program in?
    (<i>at least one required</i>)</h3>
    %s
    <h3>Enter file to upload <small>(max size 4K)</small></h3>
    <input type=file name=upfile value="%s" size=45>
    <p><input type=submit>
    </form></body></html>'''

    langSet = ('Python', 'Ruby', 'Java', 'C++', 'PHP', 'C', 'JavaScript')
    langItem = '<input type=checkbox name=lang value="%s"%s> %s\n'

    def getCPPCookies(self):  # reads cookies from client
        if 'HTTP_COOKIE' in environ:
            cookies = [x.strip() for x in environ['HTTP_COOKIE'].split(';')]
            for eachCookie in cookies:
                if len(eachCookie) > 6 and eachCookie[:3] == 'CPP':
                    tag = eachCookie[3:7]
                    try:
                        self.cookies[tag] = eval(unquote(eachCookie[8:]))
                    except (NameError, SyntaxError):
                        self.cookies[tag] = unquote(eachCookie[8:])
                if 'info' not in self.cookies:
                    self.cookies['info'] = ''
                if 'user' not in self.cookies:
                    self.cookies['user'] = ''
        else:
            self.cookies['info'] = self.cookies['user'] = ''
        
        if self.cookies['info'] != '':
            self.who, langStr, self.fn = self.cookies['info'].split(':')
            self.langs = langStr.split(',')
        else:
            self.who = self.fn = ' '
            self.langs = ['Python']
        
    def showForm(self):
        self.getCPPCookies()

        #put together language checkboxes
        langStr = []
        for eachLang in AdvCGI.langSet:
            langStr.append(AdvCGI.langItem % (eachLang,
            ' CHECKED' if eachLang in self.langs else '',
            eachLang))
        
        # see if user cookie is set up yet
        if not ('user' in self.cookies and self.cookies['user']):
            cookStatus = '<i>(cookie has not been set yet)</i>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']
        
        print '%s%s' % (AdvCGI.header, AdvCGI.formhtml %(
            AdvCGI.url, cookStatus, userCook, self.who,
            ''.join(langStr), self.fn))
    
    errhtml = '''<html><head><title>
    Advanced CGI Demo</title></head>
    <body><h3>ERROR</h3>
    <b>%s</b><p>
    <form><input type=button value=Back
    onclick="window.history.back()"></form>
    </body></html>'''

    def showError(self):
        print AdvCGI.header + AdvCGI.errhtml % (self.error)

    reshtml = '''<html><head><title>
    Advanced CGI Demo</title></head>
    <body><h2>Your Uploaded Data</h2>
    <h3>Your cookie value is: <b>%s</b></h3>
    <h3>Your name is: <b>%s</b></h3>
    <h3>Your can program in the following languages:</h3>
    <ul>%s</ul>
    <h3>Your uploaded file...<br>
    Name: <i>%s</i><br>
    Content:</h3>
    <pre>%s</pre>
    Click <a href="%s"><b>here</b></a> to return to the form.
    </body></html>'''

    def setCPPCookies(self):  # tell client to store cookies
        for eachCookie in self.cookies.keys():
            print 'Set-Cookie: CPP%s=%s; path=/' % \
                (eachCookie, quote(self.cookies[eachCookie]))
    
    def doResults(self):  # display results page
        MAXBYTES = 4096
        langList = ''.join(
            '<li>%s<br>' % eachLang for eachLang in self.langs)
        filedata = self.fp.read(MAXBYTES)
        if len(filedata) == MAXBYTES and f.read():
            filedata = '%s%s' % (filedata,
            '... <b><i>(file truncated due to size)</i></b>')
        self.fp.close()
        if filedata == '':
            filedate = '<b><i>(file not given or upload error)</i></b>'
        filename = self.fn

        # see if user cookie set up yet
        if not ('user' in self.cookies and self.cookies['user']):
            cookStatus = '<i>(cookie has not been set yet)</i>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']
        
        # set cookies
        self.cookies['info'] = ':'.join(
            (self.who, ','.join(self.langs), filename)
        )
        self.setCPPCookies()

        print '%s%s' % (AdvCGI.header, AdvCGI.reshtml % (
            cookStatus, self.who, langList,
            filename, filedata, AdvCGI.url))

    def go(self):  # determine which page to return
        self.cookies = {}
        self.error = ''
        form = FieldStorage()
        if not form.keys():
            self.showForm()
            return
        
        if 'person' in form:
            self.who = form['person'].value.strip().title()
            if self.who == '':
                self.error = 'Your name is required (blank)'
        else:
            self.error = 'Your name is required (missing)'
        
        self.cookies['user'] = unquote(form['cookie'].value.strip()) if 'cookie' in form else ''
        if 'lang' in form:
            langData = form['lang']
            if isinstance(langData, list):
                self.langs = [eachLang.value for eachLang in langData]
            else:
                self.langs = [langData.value]
        else:
            self.error = 'At least one language required.'
        
        if 'upfile' in form:
            upfile = form['upfile']
            self.fn = upfile.filename or ''
            if upfile.file:
                self.fp = upfile.file
            else:
                self.fp = StringIO('(no data)')
        else:
            self.fp = StringIO('(no tile)')
            self.fn = ''
        
        if not self.error:
            self.doResults()
        else:
            self.showError()

if __name__ == '__main__':
    page = AdvCGI()
    page.go()
