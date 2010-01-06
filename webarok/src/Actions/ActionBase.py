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
from Backend.AmarokPlayer import AmarokPlayer
#from Backend.VlcPlayer import VlcPlayer
from Backend.TrackList import TrackList

class ActionBase( object ):

    def __init__( self ):
        self.out = ""
        self.config = Configuration.Configuration()

    def do( self, param ):
        pass

class PlayerActionBase( ActionBase ):
    player = AmarokPlayer()
    #player = VlcPlayer()
    
    def bla( self, param ):
        return

class TrackListActionBase( ActionBase ):
    tracklist = TrackList()

    def bla( self, param ):
        return




