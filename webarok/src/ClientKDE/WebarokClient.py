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

#!/usr/bin/env python                     

import sys

from PyKDE4.kdecore import *
from PyKDE4.kdeui import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class WebarokClient:
  def __init__( self ):
    self.window = KMainWindow()
    self.widget = QWidget()
    self.window.setCentralWidget( self.widget )

    layout = QVBoxLayout( self.widget )

    self.addressBar = QLineEdit( self.widget )
    layout.addWidget( self.addressBar )

    self.web = QWebView( self.widget )

    #url = QUrl( "http://google.at" )
    #url.setPort( 80 )
    url = QUrl( "http://192.168.1.10" )
    url.setPort( 8085 )

    self.web.load( url )
    layout.addWidget( self.web )
    self.window.show()

    QObject.connect( self.addressBar, SIGNAL( "returnPressed()" ), self.loadUrl )

  def loadUrl( self ):
    print "Loading " + self.addressBar.text()
    self.web.load( QUrl( self.addressBar.text() ) )

appName = "WebarokKdeClient"
catalog = ""
programName = ki18n( "WebarokKdeClient" )
version = "1.0"
description = ki18n( "A simple webbrowser to control Amarok with webarok" )
license = KAboutData.License_GPL
copyright = ki18n( "(c) 2009 Verena Ruff" )
text = ki18n( "none" )
homePage = "nope"
bugEmail = "nope"

aboutData = KAboutData ( appName, catalog, programName, version, description,
license, copyright, text, homePage, bugEmail )

KCmdLineArgs.init( sys.argv, aboutData )
app = KApplication()
c = WebarokClient()
sys.exit( app.exec_() )
