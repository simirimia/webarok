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

from threading import Thread
from fileSystemHandler import fileSystemHandler

class fileSystemRunner( Thread  ):
    
    def __init__(self):
        Thread.__init__(self)
        self.callback = None
        self.log = None
        self.basedir = ''
    
    def setCallback(self, callback):
        self.callback = callback
    
    def setLog(self,log):
        self.log = log
        
    def setBasedir(self,basedir):
        self.basedir = basedir
    
    def run(self):
        handler = fileSystemHandler(self.callback, self.log)
        handler.getLibrary(self.basedir)