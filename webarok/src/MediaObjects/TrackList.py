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

from MediaObjects.MediaObjectBase import MediaObjectBase
import Backend

class TrackList( MediaObjectBase ):

    def __init__( self ):
        self.tracklist = []
        self.backend = Backend.TrackList.TrackList()
        self.backend_player = ""

    def appendSong( self, song ):
        self.tracklist.append( song )

    def getDictionary( self ):
        return { "tracklist" : self.tracklist }

    def getTrackListPart( self, startat, getto ):
        for i in range( startat, getto + 1 ):
            self.appendSong( self.backend.getSong( i ).getDictionary() )
        return

    def deleteTrack( self, index ):
        self.backend.delete( index )
        return

    def playTrack( self, index ):
        if self.backend.getLength() <= index:
            return
        current = self.backend.getCurrentTrack()
        if ( current == index ):
            return

        if self.backend_player == "":
            self.backend_player = Backend.Player.Player()

        difference = index - current
        if ( ( difference ) > 0 ):
            for i in range( difference ):
                    self.backend_player.next()
        else:
            difference = abs( difference )
            for i in range( difference ):
                self.backend_player.previous()

