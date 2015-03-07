"""
(c) webarok project
http://sourceforge.net/projects/webarok/

This file is part of Webarok.

Webarok is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Webarok is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Webarok.  If not, see <http://www.gnu.org/licenses/>.
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from Webarokserver import Dispatcher

class MyHandler( BaseHTTPRequestHandler ):

    def setup( self ):
        BaseHTTPRequestHandler.setup( self )
        self.d = Dispatcher.Dispatcher()
        return

    def do_GET( self ):

        self.d.path = self.path
        self.d.dispatch()

        if self.d.status == 200:
            self.send_response( 200 )
            self.end_headers()
            self.wfile.write( self.d.out )
            self.d.reset()
            return True
        elif self.d.status == 404:
            self.send_error( 404, 'File Not Found: %s' % self.path )
            self.d.reset()
            return False
        else:
            self.send_response( 500 )
            self.wfile.write( "500 Internal server error" )
            self.d.reset()
            return False


def main():

    try:
        server = HTTPServer( ( '', 8085 ), MyHandler )
        server.server_name = "Webarok Server"
        server.serve_forever()
        print "Server is up and running"
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()


