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

class BaseDbusPlayer( MyDbus.MyDbus ):

    def __init__( self, program ):
        print "initializing Backend/DbusbasePlayer"
        MyDbus.MyDbus.__init__( self, program )
        self.dbus_object_name = '/Player'
        self.dbus_interface_name = 'org.freedesktop.MediaPlayer'
        self.init()
        return

    def init(self):
        if self.initialized == True:
            return True
        try:
            self.player = self.getObject( self.dbus_object_name )
            self.initialized = True
        except  DBusException:
            self.initialized = False
        return self.initialized

    ## Player Controls
    def previous( self ):
        if self.init() == False:
            return False
        self.player.Prev( dbus_interface = self.dbus_interface_name )
        return True
    def play( self ):
        if self.init() == False:
            return False
        self.player.Play( dbus_interface = self.dbus_interface_name )
        return True
    def pause( self ):
        if self.init() == False:
            return False
        self.player.Pause( dbus_interface = self.dbus_interface_name )
        return True
    def unpause( self ):
        print "unpause in basedbusplayer"
        # by default, to unpause a player
        # issue a play command
        if self.init() == False:
            return False
        self.player.Play( dbus_interface = self.dbus_interface_name )
    def stop( self ):
        if self.init() == False:
            return False
        self.player.Stop( dbus_interface = self.dbus_interface_name )
        return True
    def next( self ):
        if self.init() == False:
            return False
        self.player.Next( dbus_interface = self.dbus_interface_name )
        return True


    ## Volume
    def volumeGet( self ):
        if self.init() == False:
            return False 
        dbus_volume = self.player.VolumeGet( dbus_interface = self.dbus_interface_name )
        volume = Volume.Volume()
        volume.initFromDbus( dbus_volume )
        return volume
    def volumeSet( self, v ):
        if self.init() == False:
            return False
        self.player.VolumeSet( v.volume, dbus_interface = self.dbus_interface_name )
        return True

    def volumeMute( self ):
        if self.init() == False:
            return False
        self.player.Mute( dbus_interface = self.dbus_interface_name )
        return True

    ## Metadata
    def getCurrentSong( self ):
        if self.init() == False:
            return False
        # crrent metadata
        dbus_song = self.player.GetMetadata( dbus_interface = self.dbus_interface_name )
        song = Song.Song()

        # get current position from tracklist
        # use TrackListActionBase to get the correct traclist 
#        tracklist = Backend.TrackList.TrackList()
        from Actions.ActionBase import TrackListActionBase
        tracklist = TrackListActionBase.tracklist
        current = tracklist.getCurrentTrack()
        song.initFromDictionary( dbus_song, current, current )

        # current position
        dbus_position = self.player.PositionGet( dbus_interface = self.dbus_interface_name )
        song.setCurrentPosition( dbus_position )
        return song

    def getStatus( self ):
        if self.init() == False:
            return False
        dbus_status = self.player.GetStatus( dbus_interface = self.dbus_interface_name )
        status = PlayerStatus()
        status.initFromDbus( dbus_status )
        return status
