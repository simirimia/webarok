"""
The current status (player, stopped, paused) 

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

from Actions.ActionBase import PlayerActionBase
from json import JSONEncoder

class PlayerStatus( PlayerActionBase ):
    def do( self, param ):
        status = PlayerActionBase.player.getStatus()
        encoder = JSONEncoder()
        if status == False:
            return False
        self.out = encoder.encode( status.getDictionary() )
        return True
