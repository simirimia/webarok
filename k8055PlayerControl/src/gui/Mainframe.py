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

from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QLabel

from PyKDE4.kdeui import KVBox, KHBox, KPushButton

from lib.Controller import Controller 

class MainFrame(KVBox):
    def __init__(self, parent=None):
        KVBox.__init__(self, parent)
        self.help  = QLabel ("k8055 test controller", self)
        self.layout ().setAlignment (self.help, Qt.AlignHCenter)
        self.statusLabel  = QLabel ("NOT running", self)
        self.layout ().setAlignment (self.statusLabel, Qt.AlignHCenter)
        self.resultLabel = QLabel("0", self)
        self.layout().setAlignment(self.resultLabel, Qt.AlignHCenter)
        
        hBox1 = KHBox (self)
        hBox1.setSpacing (10)
        hBox1.setMargin (40)

        startButton = KPushButton( "start", hBox1 )
        stopButton = KPushButton( "stop", hBox1 )
        
        self.connect( startButton, SIGNAL('clicked()'), self.startListening)
        self.connect( stopButton, SIGNAL('clicked()'), self.stopListening)        

        self.timer = 0
        
        self.lastResult = 0

    def startListening(self):
        self.statusLabel.setText( "Listening...." )
        self.controller = Controller()
        self.controller.connect()
        self.timer = self.startTimer(300)
    
    def stopListening(self):
        self.statusLabel.setText( "Stopped!" )
        self.killTimer(self.timer)
        self.controller.disconnect()
    
    def timerEvent (self, event):
        d = self.controller.check()
        if (d>0):
            self.resultLabel.setText( 'Last result: ' + d.__str__() )
