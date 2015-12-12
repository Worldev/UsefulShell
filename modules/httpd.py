#!/usr/bin/env python3
import logging, logging.handlers
import logging.config
import http.server
import socketserver
import queue

def run():
    """ This function opens a port in your localhost.
        The default port is 8000 in order to not cause trouble
        to any apache/php server in 8080, even though, you will be prompted."""
    que = queue.Queue(-1)
    queue_handler = logging.handlers.QueueHandler(que)
    handler_listener = logging.StreamHandler()
    listener = logging.handlers.QueueListener(que, handler_listener)
    httplog = logging.getLogger('tcpserver')
    httplog.addHandler(queue_handler)
    formatter = logging.Formatter('%(threadName)s: %(message)s')
    handler_listener.setFormatter(formatter)
    listener.start()
    try:
        PORT = int(input("Port [8000]: "))
    except ValueError:
        PORT = 8000


    Handler = http.server.SimpleHTTPRequestHandler
    try:
        httpd = socketserver.TCPServer(("", PORT), Handler)
        print("serving at port", PORT)

        httplog.info('HOST: localhost')
        httplog.info('PORT: ' + str(PORT))
        try:
            httpd.serve_forever()
            listener.stop()
        except KeyboardInterrupt:
            print('Server stopped.'+"\n")
    except OSError:
        print('I couldn\'t stablish connection to this port.')
        print("\n")
        print('Only one usage of each socket address (protocol/network address/port) is normally permitted.')
        print("\n")
        print('Check if you have another connection to the port %s and close it.' % PORT)