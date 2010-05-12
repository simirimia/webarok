"""
Contral amarok player via dbus

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

from Backend.BaseDbusPlayer import BaseDbusPlayer

# VLC needs to be started with "vlc --control dbus" explicitly
# otherwise the DBUS server is not started
 
class VlcPlayer( BaseDbusPlayer ):

    def __init__( self ):
        print "initializing Backend/VlcPlayer"
        BaseDbusPlayer.__init__( self, "org.mpris.vlc" )
        return

    def unpause( self ):
        # VLC need another pause to unpause
        BaseDbusPlayer.pause(self)

