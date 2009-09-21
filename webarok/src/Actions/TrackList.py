"""
Tracklist related actions

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

from Actions.ActionBase import TrackListActionBase
from MediaObjects.TrackList import TrackList
from json import JSONEncoder
#from string import atoi

class TrackListLength( TrackListActionBase ):
    def do( self, param ):
        length = TrackListActionBase.tracklist.getLength()
        self.length = length
        encoder = JSONEncoder()
        self.out = encoder.encode( {'length':length} )
        return

class TrackListGet( TrackListActionBase ):
    def do( self, param ):

        tlength = TrackListLength()
        tlength.do( "" )

        print "Get TrackList: " + param
        t = param.rsplit( '&' )
        print t
        p = t[0].rsplit( '=' )
        print p
        if p[0] == 'from':
            startat = int( p[1] );
        else:
            startat = 0
        print "Start at: " + startat.__str__()

        try:
            p = t[1].rsplit( '=' )
            if p[0] == 'to':
                getto = int( p[1] );
            else:
                getto = startat + 10
            print "getto: " + getto.__str__()
        except:
            print "exept happend"
            getto = tlength.length - 1


        print "List length is: " + tlength.length.__str__()
        if tlength.length < startat - 1:
            print "Not enough elements in TrackList"
            return

        if tlength.length < getto - 1:
            getto = tlength.length - 1

        tracklist = TrackList()
        tracklist.getTrackListPart( startat, getto )

        encoder = JSONEncoder()
        tmp = []
        for element in tracklist.tracklist:
            print type( element )
            if type( element ) == type( {} ):
                tmp.append( element )
            else:
                tmp.append( element.getDictionary() )

        self.out = encoder.encode( tmp )
        return

class TrackListGetElement( TrackListActionBase ):
    def do ( self, param ):
        #param is TrackLIst index
        song = TrackListActionBase.tracklist.getSong( int( param ) )
        print "Song in Action TrackListGetElement"
        print song.getDictionary()
        self.out = song.getDictionary
        return

class TrackListDeleteElement( TrackListActionBase ):
    def do( self, param ):
        print "TrackListDeleteElement calld with: " + param
        #param is TrackList index
        tracklist = TrackList()
        tracklist.deleteTrack( int( param ) )
        return

class TrackListPlayElement( TrackListActionBase ):
    def do ( self, param ):
        #param ist TrackList Index
        tracklist = TrackList()
        tracklist.playTrack( int( param ) )
        return
