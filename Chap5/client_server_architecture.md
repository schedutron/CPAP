##Windowing Server
A windowing server is an essential requirement for GUI programs. It runs on a computer with an
attached display. The server is what enables GUI programs to run. Without a windowing server,
a GUI application can't be executed. What this server does is that it provides a windowing environment
in which GUI programs can run. The event-driven nature of GUI programming adheres to the client-
server architecture because the server constantly listens for 'events' (which are like requests
for a web server), and responds to the client by giving it the details of the event. Then,
the client does some processing from those details then gives an appropriate cue (for further action)
or result to the user.

Things get more interesting in a networking environment.There, one computer can choose another computer's
windowing server for displaying it's GUI application. Thus, you can have a GUI program displayed on
one computer while its processing is done on some other computer!


##Windows Client
A windows client is simply a GUI program containing the specific details of the appliations process, as
well as its look-and-feel. As mentioned earlier, such programs require a widowing server for their execution.