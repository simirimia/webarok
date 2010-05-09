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
from MediaObjects.Song import Song
from dbus.exceptions import DBusException

class BaseDbusTrackList( MyDbus ):

    def __init__( self, program ):
        MyDbus.__init__( self, program )
        self.init()
        return

    def init(self):
        try:
            self.tracklist = self.getObject( '/TrackList' )
            self.initialized = True
        except DBusException:
            self.initialized = False
        return self.initialized

    def getSong( self, index ):
        if self.init() == False:
            return False
        dbus_song = self.tracklist.GetMetadata( index, dbus_interface = 'org.freedesktop.MediaPlayer' )
        song = Song()
        song.initFromDictionary( dbus_song, index, self.getCurrentTrack() )
        return song

    def getCurrentTrack( self ):
        if self.init() == False:
            return self.initialized
        dbus_index = self.tracklist.GetCurrentTrack( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return dbus_index.__int__()

    def getLength( self ):
        if self.init() == False:
            return False
        dbus_length = self.tracklist.GetLength( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return dbus_length.__int__()

    def delete( self, index ):
        if self.init() == False:
            return False
        self.tracklist.DelTrack( index, dbus_interface = 'org.freedesktop.MediaPlayer' )
        return
