#!/usr/bin/env python
from multiprocessing import Process, Pipe
from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
import socket
import urllib


ROOT = "."


class VLC(object):

    def __init__(self, host):
        self.host = host

    def play(self, url):
        return urllib.urlopen('http://%s:8080/requests/status.xml?command=in_play&input=%s&option=novideo' % (self.host, urllib.quote(url)))


def webserver(conn):
    PORT = 4807

    class MyOwnHandler(SimpleHTTPRequestHandler):

        def translate_path(self, path):
            global ROOT
            return ROOT + path.split('?')[0]

    httpd = SocketServer.TCPServer(("", PORT), MyOwnHandler)

    conn.send(["starting", PORT])
    httpd.serve_forever()

if __name__ == '__main__':
    import os.path
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('-m', '--myip', dest='myip')
    parser.add_option('-t', '--target', dest='target')
    parser.add_option('-p', '--play', dest='play')
    (options, args) = parser.parse_args()
    path = os.path.abspath(options.play)
    ROOT, file_ = os.path.split(path)
    vlc = VLC(options.target)
    parent_conn, child_conn = Pipe()
    p = Process(target=webserver, args=(child_conn,))
    p.start()
    print parent_conn.recv()   # prints "[42, None, 'hello']"
    print "muhahhahaha"
    if options.myip is None:
        myip = socket.gethostbyname(socket.gethostname())
    else:
        myip = options.myip
    print vlc.play('http://%s:4807/%s' % (myip, file_)).read()
    p.join()
