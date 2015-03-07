"""
Base  class for all posible actions

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


from Configuration import Configuration
from Backend.Collection import Collection

class ActionBase( object ):

    def __init__( self ):
        self.out = ""
        self.config = Configuration.Configuration()

    def do( self, param ):
        pass

class PlayerActionBase( ActionBase ):
    
    if Configuration.Configuration().player == "vlc":
        from Backend.VlcPlayer import VlcPlayer
        player = VlcPlayer()
    elif Configuration.Configuration().player == "xbmc":
        from Backend.XbmcPlayer import XbmCPlayer
        player = XbmCPlayer()
    else: # amarok is default player
        from Backend.AmarokPlayer import AmarokPlayer
        player = AmarokPlayer()
        
    def __init__(self):
        # just testing... 
        from Backend.BaseDbusPlayer import BaseDbusPlayer
        try:
            self.player = BaseDbusPlayer('test')
        except:
            pass
        
    def bla( self, param ):
        return

class TrackListActionBase( ActionBase ):
    #tracklist = TrackList()

    if Configuration.Configuration().player == "vlc":
        from Backend.VlcTrackList import VlcTrackList
        tracklist = VlcTrackList()
#    elif Configuration.Configuration().player == "xbmc":
#        from Backend.XbmcPlayer import XbmCPlayer
#        player = XbmCPlayer()
    else: # amarok is default player
        from Backend.AmarokTrackList import AmarokTrackList
        tracklist = AmarokTrackList()

    def bla( self, param ):
        return

class CollectionActionBase( ActionBase ):
    collection = Collection()

    def bla( self, param ):
        return




