#!/usr/bin/env python

from cStringIO import StringIO
import sys

from wsgiref.simple_server import make_server, demo_app

def simple_wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type:', 'text/plain')]
    start_response(status, headers)
    return ['Hello, World!']


def run_wsgi_app(app, environ):
    body = StringIO()

    def start_response(status, headers):
        body.write('Status: %s\r\n' % status)
        for header in headers:
            body.write('%s: %s\r\n' % header)
        return body.write
    
    iterable = app(environ, start_response)
    try:
        if not body.getvalue():
            raise RuntimeError("start_response() not called by app!")
        body.write('\r\n%s\r\n' % '\r\n'.join(line for line in iterable))
    finally:
        if hasattr(iterable, 'close') and callable(iterable.close):
            iterable.close()
    
    sys.stdout.write(body.getvalue())
    sys.stdout.flush()

httpd = make_server('', 8000, demo_app)
print "Started app serving on port 8000..."
httpd.serve_forever()
