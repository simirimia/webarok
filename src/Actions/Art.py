"""
Retrive album art

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
from Actions import ActionBase
from base64 import b64decode
from urllib import urlopen
from urllib import unquote
import os

class Art( ActionBase.ActionBase ):
    def do( self, param ):
        #print "Getting Art:"
        filename = b64decode( param )
        #print filename
        if len( filename ) == 0:
            #print "no filename given"
            return
        if filename.startswith( "file://" ):
            filename = filename[7:]
            filename = unquote( filename );
        print filename
        if not os.path.isfile( filename ):
            print "file does not exist" + str( filename )
            return
        if self.config.artfolder != "" and filename.startswith( self.config.artfolder ) == False:
            return

        f = urlopen( filename )
        print "sending art"
        self.out = f.read()
        return
