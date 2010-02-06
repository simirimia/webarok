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

from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

from Maindialog import Maindialog


import sys
global app
class MainWin(kdeui.KMainWindow, Maindialog):
    def __init__ (self, *args):
        kdeui.KMainWindow.__init__ (self)
        rootWidget = QtGui.QWidget(self)
        self.setupUi(rootWidget)
        self.resize(640, 480)
        self.setCentralWidget(rootWidget)
            
def run():   
    appName     = "genreTagger"
    catalog     = ""
    programName = kdecore.ki18n("genre tagger")
    version     = "0.1"
    description = kdecore.ki18n("Use the lastfm most used tag as mp3 genre tag. Upate mp3 files automatically with this info.")
    license     = kdecore.KAboutData.License_GPL
    copyright   = kdecore.ki18n("(c) 2010 webarok project")
    text        = kdecore.ki18n("")
    homePage    = "http://sourceforge.net/projects/webarok/"
    bugEmail    = "simirimia@sourceforge.net"

    aboutData   = kdecore.KAboutData(appName, catalog, programName, version, description,
                              license, copyright, text, homePage, bugEmail)

    # command line option -g was given to start the gui
    # but for the KDE app -g is an unknown option
    # found no way to register -g as valid option
    # at the KApplication
    
    # try to define some comand line options
#    options = kdecore.KCmdLineOptions()
#    options.add('g')
#    options.add('-g')
#    kdecore.KCmdLineArgs.addCmdLineOptions( options )

    #braindead workaround
    args = sys.argv
    newArgs = []
    for a in args:
        if a!='-g' and a!='-b' and a!='-m':
            newArgs.append(a)

    #kdecore.KCmdLineArgs.init(sys.argv, aboutData)
    kdecore.KCmdLineArgs.init(newArgs, aboutData)
    
    app = kdeui.KApplication()
    mainWindow = MainWin(None, "main window")
    mainWindow.show()
    app.connect (app, QtCore.SIGNAL ("lastWindowClosed ()"), app.quit)
    app.exec_ ()
    
if __name__ == '__main__':
    run()