# -*- coding: utf-8 -*-
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

from Actions.ActionBase import CollectionActionBase
from MediaObjects.Collection import Collection
from json import JSONEncoder
#from string import atoi

class CollectionSearchArtist( CollectionActionBase ):
    def do( self, param ):
        collection = Collection()

        keyword = param;

        collection.getSongsByArtist( keyword )

        encoder = JSONEncoder()
        tmp = []
        for element in collection.tracklist:
            #print type( "Debug: Type of element: " + str(element) )
            if type( element ) == type( {} ):
                tmp.append( element )
            else:
                tmp.append( element.getDictionary() )

        self.out = encoder.encode( tmp )
        return

class CollectionSearchTitle( CollectionActionBase ):
    def do( self, param ):
        collection = Collection()

        keyword = param;

        collection.getSongsByTitle( keyword )

        encoder = JSONEncoder()
        tmp = []
        for element in collection.tracklist:
            #print type( "Debug: Type of element: " + str(element) )
            if type( element ) == type( {} ):
                tmp.append( element )
            else:
                tmp.append( element.getDictionary() )

        self.out = encoder.encode( tmp )
        return

class CollectionSearchAll( CollectionActionBase ):
    def do( self, param ):
        collection = Collection()
        keyword = param;
        #print keyword
        collection.getSongsByAll( keyword )

        encoder = JSONEncoder()
        tmp = []
        for element in collection.tracklist:
            #print type( "Debug: Type of element: " + str(element) )
            if type( element ) == type( {} ):
                tmp.append( element )
            else:
                tmp.append( element.getDictionary() )

        self.out = encoder.encode( tmp )
        return

class CollectionPutElementInTrackList( CollectionActionBase ):
    def do ( self, param ):
        #param is Sql-Id Index
        collection = Collection()
        collection.putTrackInTrackList( param )
        return

class CollectionPlayElement( CollectionActionBase ):
    def do ( self, param ):
        #param is Sql-Id Index
        collection = Collection()
        collection.playTrack( param )
        return
