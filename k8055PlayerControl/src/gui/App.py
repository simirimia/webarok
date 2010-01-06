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

from PyKDE4.kdecore import KCmdLineArgs, KAboutData, ki18n
from PyKDE4.kdeui import KApplication, KMainWindow

from PyQt4.QtCore import SIGNAL

import sys
 
from gui.Mainframe import MainFrame
 
class MainWin (KMainWindow):
    def __init__ (self, *args):
        KMainWindow.__init__ (self)
        self.resize(300, 200)
        self.setCentralWidget (MainFrame(self))  
 
def run():
    appName     = "k8055 player control"
    catalog     = ""
    programName = ki18n ("k8055 player control") 
    version     = "0.1"
    description = ki18n ("control various music/video players with the velleman K8055 USB interface board")
    license     = KAboutData.License_GPL
    copyright   = ki18n ("(c) 2010 webarok project")
    text        = ki18n ("")
    homePage    = "http://sourceforge.net/projects/webarok/"
    bugEmail    = "simirimia@sourceforge.net"

    aboutData   = KAboutData (appName, catalog, programName, version, description,
                              license, copyright, text, homePage, bugEmail)

    aboutData.addAuthor (ki18n ("simirimia"), ki18n ("original concept"))
    
    KCmdLineArgs.init (sys.argv, aboutData)
    
    app = KApplication ()
    mainWindow = MainWin (None, "k8055 player control")
    mainWindow.show()
    app.connect (app, SIGNAL ("lastWindowClosed ()"), app.quit)
    app.exec_ ()