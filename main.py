# -*- coding:UTF-8 -*-
import sys
import locale
import http.server
import socketserver
def main():
    print("start")
    addr = ""
    port =80
    handler = http.server.CGIHTTPRequestHandler
    httpd = http.server.HTTPServer((addr, port), handler)
    print ("HTTP server is at: http://%s:%d/" % (addr, port))
    httpd.serve_forever()




if __name__=="__main__":
    main()