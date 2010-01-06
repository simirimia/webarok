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

from pyk8055 import k8055
CARD_NUMBER = 3

from Backend.AmarokPlayer import AmarokPlayer

class Controller():
    
    def __init__(self):
        
        self.actions = {
                         1 : self.play,
                         2 : self.stop,
                         4 : self.pause
                        }
        
    
    def connect(self):
        self.k8055 = k8055(CARD_NUMBER)
    
    def disconnect(self):
        self.k8055.CloseDevice()
    
    def check(self):
        d =  self.k8055.ReadAllDigital()
        if d > 0 and d != self.lastResult:
            #self.resultLabel.setText( 'Last result: ' + d.__str__() )
            try:
                self.actions[d]()
            except Exception as e:
                print "unknown command issued: " + d.__str__()
                print e
        self.lastResult = d
        return -1
    
    def play(self):
        p = AmarokPlayer()
        p.play()
        #print "play"
   
    def stop(self):
        p = AmarokPlayer()
        p.stop()
        #print "stop"
   
    def pause(self):
        p = AmarokPlayer()
        p.pause()
        #print "pause"
