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

class Player( MyDbus.MyDbus ):

    def __init__( self ):
        MyDbus.MyDbus.__init__( self, "org.kde.amarok" )
        self.player = self.getObject( '/Player' )
        return

    ## Player Controls
    def previous( self ):
        self.player.Prev( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return
    def play( self ):
        self.player.Play( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return
    def pause( self ):
        self.player.Pause( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return
    def stop( self ):
        self.player.Stop( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return
    def next( self ):
        self.player.Next( dbus_interface = 'org.freedesktop.MediaPlayer' )
        return


    ## Volume
    def volumeGet( self ):
        dbus_volume = self.player.VolumeGet( dbus_interface = 'org.freedesktop.MediaPlayer' )
        volume = Volume.Volume()
        volume.initFromDbus( dbus_volume )
        return volume
    def volumeSet( self, v ):
        self.player.VolumeSet( v.volume, dbus_interface = 'org.freedesktop.MediaPlayer' )
        return


    ## Metadata
    def getCurrentSong( self ):
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
        dbus_status = self.player.GetStatus( dbus_interface = 'org.freedesktop.MediaPlayer' )
        print "Status in Backend:"
        print dbus_status
        status = PlayerStatus()
        status.initFromDbus( dbus_status )
        return status
