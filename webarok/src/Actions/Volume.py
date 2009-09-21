"""
Volume related actions

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

from Backend import Player
from Actions import ActionBase

from Theme_default import VolumeView

class VolumeGet( ActionBase.PlayerActionBase ):
    def do( self, param ):
        v = ActionBase.PlayerActionBase.player.volumeGet()

        view = VolumeView.VolumeView( v )
        self.out = view.render()
        return

class VolumeUp( ActionBase.PlayerActionBase ):
    def do( self, param ):
        v = ActionBase.PlayerActionBase.player.volumeGet()
        v.up()
        ActionBase.PlayerActionBase.player.volumeSet( v )
        return

class VolumeDown( ActionBase.PlayerActionBase ):
    def do( self, param ):
        v = ActionBase.PlayerActionBase.player.volumeGet()
        v.down()
        ActionBase.PlayerActionBase.player.volumeSet( v )
        return
