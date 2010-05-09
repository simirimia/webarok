# -*- coding: utf-8 -*-
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

class Volume( object ):

    def __init__( self ):
        self.volume = 0
        return

    def initFromDbus( self, d ):
        self.volume = d
        return

    def up( self ):
        self.volume += 5
        return

    def down( self ):
        self.volume -= 5
        return

    def getDictionary( self ):
        return { 'volume' : self.volume }

