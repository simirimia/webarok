"""
Get the correct action instance 

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

from Actions import CurrentSong
from Actions import PlayerControls
from Actions import Volume
from Actions import Art
from Actions.PlayerStatus import PlayerStatus
from Actions.TrackList import TrackListLength
from Actions.TrackList import TrackListGet
from Actions.TrackList import TrackListGetElement
from Actions.TrackList import TrackListDeleteElement
from Actions.TrackList import TrackListPlayElement

class Factory( object ):

    def __init__( self ):
        self.next = ""
        self.previous = ""
        self.play = ""
        self.stop = ""
        self.pause = ""
        self.volumeget = ""
        self.volumeup = ""
        self.volumedown = ""
        self.volumemute = ""
        self.currentsong = ""
        self.art = ""
        self.playerstatus = ""
        self.tracklistlength = ""
        self.tracklist = ""
        self.tracklistelement = ""
        self.tracklistdeleteelement = ""
        self.tracklistplayelement = ""
        return

    def get( self, name ):

        if name == "TrackListPlayElement":
            if self.tracklistplayelement == "":
                self.tracklistplayelement = TrackListPlayElement()
            return self.tracklistplayelement

        if name == "TrackListDeleteElement":
            if self.tracklistdeleteelement == "":
                self.tracklistdeleteelement = TrackListDeleteElement()
            return self.tracklistdeleteelement

        if name == "TrackListGetElement":
            if self.tracklistelement == "":
                self.tracklistelement = TrackListGetElement()
            return self.tracklistelement

        if name == "TrackListGet":
            if self.tracklist == "":
                self.tracklist = TrackListGet()
            return self.tracklist

        if name == "TrackListLength":
            if self.tracklistlength == "":
                self.tracklistlength = TrackListLength()
            return self.tracklistlength

        if name == "Art":
            if self.art == "":
                self.art = Art.Art()
            return self.art

        if name == "PlayerStatus":
            if self.playerstatus == "":
                self.playerstatus = PlayerStatus()
            return self.playerstatus

        if name == "CurrentSong":
            if self.currentsong == "":
                self.currentsong = CurrentSong.CurrentSong()
            return self.currentsong

        if name == "Next":
            if self.next == "":
                self.next = PlayerControls.Next()
            return self.next
        if name == "Stop":
            if self.stop == "":
                self.stop = PlayerControls.Stop()
            return self.stop
        if name == "Pause":
            if self.pause == "":
                self.pause = PlayerControls.Pause()
            return self.pause
        if name == "Previous":
            if self.previous == "":
                self.previous = PlayerControls.Previous()
            return self.previous
        if name == "Play":
            if self.play == "":
                self.play = PlayerControls.Play()
            return self.play

        if name == "VolumeGet":
            if self.volumeget == "":
                self.volumeget = Volume.VolumeGet()
            return self.volumeget
        if name == "VolumeUp":
            if self.volumeup == "":
                self.volumeup = Volume.VolumeUp()
            return self.volumeup
        if name == "VolumeDown":
            if self.volumedown == "":
                self.volumedown = Volume.VolumeDown()
            return self.volumedown
        if name == "VolumeMute":
            if self.volumemute == "":
                self.volumemute = Volume.VolumeMute()
            return self.volumemute

        return
