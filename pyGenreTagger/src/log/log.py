# -*- coding: utf-8 -*-
"""
Use the lastfm most used tag as mp3 genre tag. Upate mp3 files automatically with this info.

(c) webarok project
http://sourceforge.net/projects/webarok/
http://simirimia.triosolutions.at/

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

class log(object):
    def __init__(self, mode):
        if mode == 'doPrint':
            self.mode = 'doPrint'
        if mode == 'appendTextWidget':
            self.mode = 'appendTextWidget'
            
    def setTextWidget(self, widget):
        self.textWidget = widget        
            
    def addMessage(self, message ):
        if self.mode == 'doPrint':
            self.doPrint(message)
        if self.mode == 'appendTextWidget':
            self.appendTextWidget(message)
            
    def appendTextWidget(self, message):
        self.textWidget.append(message)
    
    def doPrint(self, message):
        print message