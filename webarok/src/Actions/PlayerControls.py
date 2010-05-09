"""
contral the player

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


class Next( ActionBase.PlayerActionBase ):
    def do( self, param ):
        if ActionBase.PlayerActionBase.player.isInitialized() == False:
            return False
        ActionBase.PlayerActionBase.player.next()
        return True

class Pause( ActionBase.PlayerActionBase ):
    def do( self, param ):
        if ActionBase.PlayerActionBase.player.isInitialized() == False:
            return False
        ActionBase.PlayerActionBase.player.pause()
        return True


class Play( ActionBase.PlayerActionBase ):
    def do( self, param ):
        if ActionBase.PlayerActionBase.player.isInitialized() == False:
            return False
        ActionBase.PlayerActionBase.player.play()
        return True

class Previous( ActionBase.PlayerActionBase ):
    def do( self, param ):
        if ActionBase.PlayerActionBase.player.isInitialized() == False:
            return False
        ActionBase.PlayerActionBase.player.previous()
        return True

class Stop( ActionBase.PlayerActionBase ):
    def do( self, param ):
        if ActionBase.PlayerActionBase.player.isInitialized() == False:
            return False        
        ActionBase.PlayerActionBase.player.stop()
        return True

class Seek( ActionBase.PlayerActionBase ):
    def do( self, param ):
        if ActionBase.PlayerActionBase.player.isInitialized() == False:
            return False
        song = ActionBase.PlayerActionBase.player.getCurrentSong()
        
        time = song.getDictionary()["mtime"]        
        #print "DEBUG: "+str(time)
        positionToGo = time * float(param)/100.0
        if positionToGo<0:
          positionToGo = 0
        if positionToGo>time-1:
          positionToGo = time-1 
        #print "DEBUG: "+str(int(positionToGo))
        ActionBase.PlayerActionBase.player.seek( int(positionToGo) )
        return True
