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

class Collection( MediaObjectBase ):

    def __init__( self ):
        self.tracklist = []
        self.backend = Backend.Collection.Collection()

    def appendSong( self, song ):
        self.tracklist.append( song )

    def getDictionary( self ):
        return { "searchresults" : self.tracklist }

    def getSongsByArtist( self, keyword ):
        songs = self.backend.searchArtist( keyword )
        for song in songs:
            d = { "url":song[0],
                  "artist":song[1],
                  "album":song[2],
                  "title":song[3] }
            self.appendSong( d )        
        return

    def getSongsByTitle( self, keyword ):
        songs = self.backend.searchTitle( keyword )
        for song in songs:
            d = { "url":song[0],
                  "artist":song[1],
                  "album":song[2],
                  "title":song[3] }
            self.appendSong( d )        
        return

    def getSongsByAll( self, keyword ):
        songs = self.backend.searchAll( keyword )
        for song in songs:
            d = { "url":song[0],
                  "artist":song[1],
                  "album":song[2],
                  "title":song[3] }
            self.appendSong( d )        
        return

    def playTrack( self, trackUrl ):
        self.backend.trackToPlayList( trackUrl, True )
        return

    def putTrackInTrackList( self, trackUrl ):
        self.backend.trackToPlayList( trackUrl, False )
        return

