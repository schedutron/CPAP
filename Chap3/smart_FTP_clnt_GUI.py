from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

#this is just a download client, upload functionality absent
from ftplib import FTP, error_perm
import re, pickle, sys, os #maybe sqlite3 is a better option here instead of pickle
from time import ctime

class DirItemButton(ListItemButton):
    def __init__(self, **kwargs):
        ListItemButton.__init__(self, **kwargs)
        self.size_hint_y = None
        self.height = "20dp"

class Client(BoxLayout):
    host_name_text_input = ObjectProperty()
    dir_name_text_input = ObjectProperty()
    dir_contents = ObjectProperty()
    status = ObjectProperty()
    f = None #FTP Object
    contents = [] #to store directory data

    def get(self):
        hname = self.host_name_text_input.text
        dname = self.dir_name_text_input.text
        #login to host
        if not self.f or hname != self.f.host:
            try:
                self.f = FTP(hname)
                self.f.login() #only anonymous login support for now
            except:
                self.host_name_text_input.text = "Cannot connect. Try again."
                return

        #cd to the directory
        try:
            self.f.cwd(dname)
        except:
            self.dir_name_text_input.text = "Unable to access your provided directory."
            return

        #display its contents
        self.contents = []
        self.f.dir(self.contents.append)

        extract = r'\d[ ]([^: ]+)' #pattern for extracting the names
        fnames = [re.findall(extract, item)[-1] for item in self.contents]

        self.dir_contents.adapter.data = []
        for i in range(len(fnames)):
            to_be_appended = fnames[i]
            if self.contents[i][0] == 'd': #check whether it's a directory
                to_be_appended += '/'
            self.dir_contents.adapter.data.append(to_be_appended) #adds contents to the dir_contents_view

        self.dir_contents._trigger_reset_populate()

    def download(self):
        #if items are selected
        if self.dir_contents.adapter.selection:
            #create a folder to put download contents in, name it ctime() or let the user name it with a popup
            name = ctime()
            os.mkdir(name)
            os.chdir(name)
            #download each item
            for item in self.dir_contents.adapter.selection:
                stuff = item.text
                self.status.text = "Downloading %s" % stuff
                print self.update_status()
                with open(stuff, 'wb') as content:
                    #callback = Callback(content, size)
                    self.f.retrbinary("RETR %s" % stuff, content.write, 1024)
                    #history["downloads"].append("%s%s%s - %s" % (chunks[1], dirname, item, ctime()))
                self.status.text = "%s downloaded!" % stuff
            os.chdir('..')
            #self.status.text = "All download(s) complete!"

    def behind(self):
        #move one step back in the directory tree
        try:
            self.f.cwd('..')
            self.dir_name_text_input.text = '/' + '/'.join(self.dir_name_text_input.text.split('/')[:-1])
            self.get()
        except:
            self.dir_name_text_input.text = 'Unable to change directory.'

class FTPClientApp(App):
    def build(self):
        return Client()

ftpc_app = FTPClientApp()
ftpc_app.run()
