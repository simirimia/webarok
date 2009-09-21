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

from MediaObjectBase import MediaObjectBase
from base64 import b64encode

class Song( MediaObjectBase ):

    def __init__( self ):
        self.album = ""
        self.artist = ""
        self.title = ""
        self.arturl = ""
        self.mtime = 0
        self.rating = 0
        self.time = 0
        self.tracknumber = 0
        self.year = ""
        self.genre = ""
        self.albumart_remote_url = ""
        self.is_current = False
        self.position = 0
        self.tracklistindex = 0

    def getDictionary( self ):
        d = { "title":self.title,
              "artist":self.artist,
              "album":self.album,
              "time":self.time,
              "mtime":self.mtime,
              "albumartremoteurl":self.albumart_remote_url,
              "tracklistindex":self.tracklistindex }
        if self.is_current == True:
            d['is_current'] = self.is_current
            d['position'] = self.position
        return d

    def setCurrentPosition( self, position ):
        self.is_current = True
        self.position = position.__int__()

    def initFromDictionary( self, dict, tracklistindex = -1, current_song_index = -2 ):
        if len( dict ) == 0:
            self.__init__();
            return

        self.album = dict["album"]
        self.artist = dict["artist"]
        self.title = dict["title"]
        self.arturl = dict["arturl"]
        self.mtime = dict["mtime"].__int__()
        self.rating = dict["rating"].__int__()
        self.time = dict["time"].__int__()
        self.tracknumber = dict["tracknumber"].__int__()
        self.year = dict["year"]
        self.genre = dict["genre"]
        self.albumart_remote_url = b64encode( dict["arturl"] )
        self.tracklistindex = tracklistindex
        if tracklistindex == current_song_index:
            print "Found current song in init from dictionary"
            self.is_current = True
        return

