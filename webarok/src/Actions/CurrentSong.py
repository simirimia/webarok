"""
Get Metadata for the current song

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

from Actions import ActionBase

from Theme_default import SongView

class CurrentSong( ActionBase.PlayerActionBase ):

    def do( self, param ):
        # getting the data
        if ActionBase.PlayerActionBase.player.isInitialized() == False:
            self.out = ""
            return False
        
        song = ActionBase.PlayerActionBase.player.getCurrentSong()
        # initializing the view
        #theme = __import__( "Theme_" + self.config.theme )
        #print theme
        #view = theme.SongView.SongView( song )
        view = SongView.SongView( song )
        self.out = view.render()
        return True

class PositionGet( ActionBase.PlayerActionBase ):
    def do( self, param ):
        return

