"""
control amarok tracklist via dbus

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

from MyDbus import MyDbus
from MyMySql import MyMySql
from dbus.exceptions import DBusException
import urllib

class Collection( MyDbus ):

    def __init__( self ):
        MyDbus.__init__( self, "org.kde.amarok" )        
        self.db = MyMySql()
        self.init()
        return
    
    def init(self):
        try:
            self.tracklist = self.getObject( '/TrackList' )
            self.initialized = True
        except DBusException:
            self.initialized = False
        return self.initialized

    def searchTitle( self, keyword ):
        keyword = self.prepareKeyword( keyword )
        self.db.cursor.execute("SELECT `tracks`.`url`, `artists`.`name`, `albums`.`name`, `tracks`.`title` \
                                FROM `tracks`, `artists`, `albums` \
                                WHERE `tracks`.`artist` = `artists`.`id` AND `tracks`.`album` = `albums`.`id` \
                                AND LOWER(`tracks`.`title`) LIKE LOWER('"+keyword+"') ORDER BY `artists`.`name`, `albums`.`name`, `tracks`.`title`")
        songs = self.db.cursor.fetchall() 
        return songs

    def searchArtist( self, keyword ):
        keyword = self.prepareKeyword( keyword )
        self.db.cursor.execute("SELECT `tracks`.`url`, `artists`.`name`, `albums`.`name`, `tracks`.`title` \
                                FROM `tracks`, `artists`, `albums` \
                                WHERE `tracks`.`artist` = `artists`.`id` AND `tracks`.`album` = `albums`.`id` \
                                AND LOWER(`artists`.`name`) LIKE LOWER('"+keyword+"') ORDER BY `artists`.`name`, `albums`.`name`, `tracks`.`title`")
        songs = self.db.cursor.fetchall() 
        return songs

    """
    Searches Artist, Title, Album  
    """
    def searchAll( self, keyword ):
        keyword = self.prepareKeyword( keyword )
        #print "DEBUG: " + keyword
        self.db.cursor.execute("SELECT `tracks`.`url`, `artists`.`name`, `albums`.`name`, `tracks`.`title` \
                                FROM `tracks`, `artists`, `albums` \
                                WHERE `tracks`.`artist` = `artists`.`id` AND `tracks`.`album` = `albums`.`id` \
                                AND (LOWER(`tracks`.`title`) LIKE LOWER('"+keyword+"') \
                                OR LOWER(`artists`.`name`) LIKE LOWER('"+keyword+"') \
                                OR LOWER(`albums`.`name`) LIKE LOWER('"+keyword+"')) ORDER BY `artists`.`name`, `albums`.`name`, `tracks`.`title`")
        songs = self.db.cursor.fetchall() 
        return songs
    
    def trackToPlayList( self, trackUrl, play):
        if self.init() == False:
            return False
        self.db.cursor.execute("SELECT `urls`.`rpath` FROM `urls` WHERE `urls`.`id` = "+str(trackUrl))
        url = self.db.cursor.fetchone()
        #print "DEBUG: URL: "+str(url[0][1:]);
        self.tracklist.AddTrack( str(url[0][1:]), play, dbus_interface = 'org.freedesktop.MediaPlayer' )
        return
        
    def prepareKeyword( self, keyword):        
        keyword=keyword.strip()
        keyword=urllib.unquote(keyword)
        keyword=keyword.replace('\\','\\\\')
        keyword=keyword.replace('_','\\_')
        keyword=keyword.replace('%','\\%')
        keyword=keyword.replace('\'','\\\'')
        return "%"+keyword+"%"