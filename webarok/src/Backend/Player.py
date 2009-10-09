"""
Contral amarok player via dbus

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

import MyDbus
import Backend
from MediaObjects import Song
from MediaObjects import Volume
from MediaObjects.PlayerStatus import PlayerStatus
from dbus.exceptions import DBusException

class Player( MyDbus.MyDbus ):

    def __init__( self ):
        MyDbus.MyDbus.__init__( self, "org.kde.amarok" )
        self.init()
        return

    def init(self):
        if self.initialized == True:
            return True
        try:
            self.player = self.getObject( '/Player' )
            self.initialized = True
        except  DBusException:
            self.initialized = False
        return self.initialized

    ## Player Controls
    def previous( self ):
        if self.init() == False:
            return False
        self.player.Prev( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return True
    def play( self ):
        if self.init() == False:
            return False
        self.player.Play( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return True
    def pause( self ):
        if self.init() == False:
            return False
        self.player.Pause( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return True
    def stop( self ):
        if self.init() == False:
            return False
        self.player.Stop( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return True
    def next( self ):
        if self.init() == False:
            return False
        self.player.Next( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return True


    ## Volume
    def volumeGet( self ):
        if self.init() == False:
            return False 
        dbus_volume = self.player.VolumeGet( dbus_interface = 'org.freedesktop.MediaPlayer' )
        volume = Volume.Volume()
        volume.initFromDbus( dbus_volume )
        return volume
    def volumeSet( self, v ):
        if self.init() == False:
            return False
        self.player.VolumeSet( v.volume, dbus_interface = 'org.freedesktop.MediaPlayer' )
        return True

    def volumeMute( self ):
        if self.init() == False:
            return False
        self.player.Mute( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return True

    ## Metadata
    def getCurrentSong( self ):
        if self.init() == False:
            return False
        # crrent metadata
        dbus_song = self.player.GetMetadata( dbus_interface = 'org.freedesktop.MediaPlayer' )
        song = Song.Song()

        # get current position from tracklist
        tracklist = Backend.TrackList.TrackList()
        current = tracklist.getCurrentTrack()
        song.initFromDictionary( dbus_song, current, current )

        # current position
        dbus_position = self.player.PositionGet( dbus_interface = 'org.freedesktop.MediaPlayer' )
        song.setCurrentPosition( dbus_position )
        return song

    def getStatus( self ):
        if self.init() == False:
            return False
        dbus_status = self.player.GetStatus( dbus_interface = 'org.freedesktop.MediaPlayer' )
        print "Status in Backend:"
        print dbus_status
        status = PlayerStatus()
        status.initFromDbus( dbus_status )
        return status
