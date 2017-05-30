#!usr/bin/env python

from time import ctime
import SocketServer

class AsyncRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print "Connection from: %s" % str(self.client_address)
        request_msg = self.rfile.readline(1024)
        self.wfile.write("[%s] %s" % (ctime(), request_msg))
        self.wfile.flush()

def up_and_run():
    tcp_server = SocketServer.ForkingTCPServer(
        ("0.0.0.0", 9000),
        RequestHandlerClass=AsyncRequestHandler,
        bind_and_activate=False)

    tcp_server.allow_reuse_address = True
    tcp_server.server_bind()
    tcp_server.server_activate()

    tcp_server.serve_forever()

if __name__ == "__main__":
    print "Waiting for connection..."
    up_and_run()
