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

class PlayerStatus( MediaObjectBase ):

    def __init__( self ):
        self.stopped = True
        self.paused = False
        self.playing = False

    def initFromDbus( self, param ):
        self.stopped = False
        self.paused = False
        self.playing = False

        if param[0] == 0:
            self.playing = True
        if param[0] == 1:
            self.paused = True
        if param[0] == 2:
            self.stopped = True

        return

    def getDictionary( self ):
        if self.stopped == True:
            return { 'status' : 'stopped' }
        if self.paused == True:
            return { 'status' : 'paused' }
        if self.playing == True:
            return { 'status' : 'playing' }

        return {}
