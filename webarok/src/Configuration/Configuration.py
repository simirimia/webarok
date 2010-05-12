"""
Base  class for all posible actions

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

class Configuration( object ):
    def __init__( self ):
        self.artfolder = "/home/***PLEASE CHANGE THIS***/.kde/share/apps/amarok/albumcovers/"
        #self.artfolder = "/home/verena/.kde/share/apps/amarok/albumcovers/"
        self.staticTheme = "default"
        
        # check if mysql module is available
        # only used in context with Amarok as player 
        try:
            import MySQLdb
            self.useCollection = True
            self.mysql_host = "localhost"
            self.mysql_user = "amarokuser"
            self.mysql_pass = "amarok"
            self.mysql_db   = "amarokdb"
#            } 
        except:
            self.useCollection = False
         
        # type of player  
        # VLC needs to be started with "vlc --control dbus" explicitly
        # otherwise the DBUS server is not started
        
        self.player = 'amarok'    
        #self.player = 'vlc'
        #self.player = 'xbmc'    
        return

