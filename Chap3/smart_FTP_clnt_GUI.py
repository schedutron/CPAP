from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.button import Button

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
    the_buttons = ObjectProperty()
    history = ObjectProperty()
    bookmarks = ObjectProperty()
    downloads = ObjectProperty()
    bookmark_btn = None #the button which asks to bookmark a location
    f = None #FTP Object
    contents = [] #to store directory data

    def get(self):
        #removes the bookmark button if it exists
        if self.bookmark_btn:
            self.the_buttons.remove_widget(self.bookmark_btn)
            self.bookmark_btn = None

        #reads host name and directory name from input
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

            history_dict['history'].append('%s - %s' % (self.f.host, ctime()))
            self.history.values = history_dict['history'] #updates the history list for display
            self.update_db()

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

        self.location = "%s" % self.f.host + self.f.pwd()
        if self.location not in history_dict['bookmarks']:
            self.bookmark_btn = Button(text="Bookmark this location?")
            self.the_buttons.add_widget(self.bookmark_btn)
            self.bookmark_btn.bind(on_press=self.add_bookmark)

    def add_bookmark(self, *ignore): #ignore the callback arguments passed
        history_dict["bookmarks"].append(self.location)
        self.bookmarks.values = history_dict["bookmarks"]
        self.update_db()
        self.the_buttons.remove_widget(self.bookmark_btn) #updates the bookmarks list for displays

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
                with open(stuff, 'wb') as content:
                    #callback = Callback(content, size)
                    self.f.retrbinary("RETR %s" % stuff, content.write, 1024)
                    history_dict["downloads"].append("%s%s%s - %s" % (self.f.host, self.f.pwd(), stuff, ctime()))
                    self.downloads.values = history_dict["downloads"] #updates the downloads list for display
                self.status.text = "%s downloaded!" % stuff
            os.chdir('..')
            self.update_db()
            self.status.text = "All download(s) complete!"

    def behind(self):
        #move one step back in the directory tree
        try:
            self.f.cwd('..')
            self.dir_name_text_input.text = '/'.join(self.dir_name_text_input.text.split('/')[:-1])
            if not self.dir_name_text_input.text:
                self.dir_name_text_input.text = '/'
            self.get()
        except:
            self.dir_name_text_input.text = 'Unable to change directory.'

    def update_db(self): #writes to the pickle file
        with open('history.pkl', 'wb') as write_file:
            pickle.dump(history_dict, write_file)

with open('history.pkl', 'rb') as h:
    history_dict = pickle.load(h)

class FTPClientApp(App):
    def build(self):
        return Client()

ftpc_app = FTPClientApp()
ftpc_app.run()
