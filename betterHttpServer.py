#!/bin/python

# This program is released under the terms of the GNU GPL version 3 or any later version.

import http.server
import socketserver
import argparse

parser = argparse.ArgumentParser(
    prog = "BetterHttpServer",
    description = "Additional functionality to the SimpleHTTPServer Python module to output headers")

parser.add_argument('--header', type=str, default="User-Agent")
parser.add_argument('-p', '--port', type=int, metavar="[0-65536]", default=8000)
parser.add_argument('-a', '--all-Headers', action='store_true') 

args = parser.parse_args()

header = args.header
port = args.port
allHeaderFlag = args.all_Headers

class SpecificHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        print(self.headers.get(header))
        http.server.SimpleHTTPRequestHandler.do_GET(self)


class AllHeadersHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        print(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

if (allHeaderFlag != True):
    Handler = SpecificHandler
else:
    Handler = AllHeadersHandler

httpd = socketserver.TCPServer(("", port), Handler)

httpd.serve_forever()
