# -*- coding: utf-8 -*-
"""
Use the lastfm most used tag as mp3 genre tag. Upate mp3 files automatically with this info.

Abstraction layer to the auto-generated UI_Form.py file. UI_Form.py is
generated out of the Qt designer created Maindialog.ui file with the 
command: 
pykdeuic4 -o Ui_Form.py Maindialog.ui

Additional GUI initializations are done here

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

from PyQt4.QtCore import SIGNAL

from Ui_Form import Ui_Form

#single threaded version
#from fileHandling.fileSystemHandler import fileSystemHandler
from fileHandling.fileSystemRunner import fileSystemRunner
  
from tag.GenreHandler import GenreHandler
from log.log import log

class Maindialog(Ui_Form):
    def setupUi(self, Form):
        Ui_Form.setupUi(self,Form)
        
        # do custom setup here
        self.connect( self.dryrunButton, SIGNAL('clicked()'), self.startDryRun) 
        
        
    def startDryRun(self):
        basedir = self.basedir.text()
        self.output.clear()
        print "Start dry run for dir: " + basedir
        genre = GenreHandler()
        #theLog = log( 'doPrint' )
        theLog = log( 'appendTextWidget' )
        theLog.setTextWidget(self.output)
        #theLog.addMessage('A log test message')

        # the single threaded version
#        handler = fileSystemHandler( genre.getGenre, theLog )
#        handler.getLibrary(basedir)

        runner = fileSystemRunner()
        runner.setBasedir(basedir)
        runner.setLog(theLog)
        runner.setCallback(genre.getGenre)
        runner.start()
        
        
        
        