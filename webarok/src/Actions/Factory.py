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
from Actions.Collection import CollectionSearchArtist
from Actions.Collection import CollectionSearchTitle
from Actions.Collection import CollectionSearchAll
from Actions.Collection import CollectionPutElementInTrackList
from Actions.Collection import CollectionPlayElement
from Configuration import Configuration

class Factory( object ):

    def __init__( self ):
        self.config = Configuration.Configuration()
        self.next = ""
        self.previous = ""
        self.play = ""
        self.stop = ""
        self.pause = ""
        self.unpause = ""
        self.seek = ""
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
        self.searchtitle = ""
        self.searchartist = ""
        self.searchall = ""
        self.searchplayelement = ""
        self.searchputelementtotracklist = ""
        return

    def get( self, name ):
        if (self.config.useCollection == True):
            if name == "SearchTitle":
                if self.searchtitle == "":
                    self.searchtitle = CollectionSearchTitle()
                return self.searchtitle

            if name == "SearchArtist":
                if self.searchartist == "":
                    self.searchartist = CollectionSearchArtist()
                return self.searchartist

            if name == "SearchAll":
                if self.searchall == "":
                    self.searchall = CollectionSearchAll()
                return self.searchall

            if name == "SearchPlayElement":
                if self.searchplayelement == "":
                    self.searchplayelement = CollectionPlayElement()
                return self.searchplayelement

            if name == "SearchPutElementToTrackList":
                if self.searchputelementtotracklist == "":
                    self.searchputelementtotracklist = CollectionPutElementInTrackList()
                return self.searchputelementtotracklist

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
        if name == "Unpause":
            if self.unpause == "": 
                self.unpause = PlayerControls.Unpause()
            return self.unpause
        if name == "Previous":
            if self.previous == "":
                self.previous = PlayerControls.Previous()
            return self.previous
        if name == "Play":
            if self.play == "":
                self.play = PlayerControls.Play()
            return self.play
        if name == "Seek":
            if self.seek == "":
                self.seek = PlayerControls.Seek()
            return self.seek

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
