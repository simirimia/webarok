# -*- coding: utf-8 -*-
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

from os import curdir

from Configuration import Configuration
from Actions import Factory

class DispatcherBase( object ):
    def __init__( self ):
        self.path = ""
        self.out = ""
        self.status = 0
        self.config = ""
        return

    def dispatch( self ):
        return

    def reset( self ):
        self.path = ""
        self.out = ""
        self.status = ""
        return

### END DispatcherBase ###

class Dispatcher( DispatcherBase ):

    def __init__( self ):
        self.config = Configuration.Configuration()
        return

    def dispatch( self ):
        #print "Dispatching: " + self.path

        if self.path.startswith( "/action/" ):
            d = DynamicDispatcher()
        elif self.path.startswith( "/index" ) or self.path == "" or self.path == "/":
            d = MainDispatcher()
        else:
            d = StaticDispatcher()
            pass

        d.config = self.config
        d.path = self.path
        d.dispatch()
        self.out = d.out
        self.status = d.status
        d.reset()
        return

### END Dispatcher ###

class StaticDispatcher( DispatcherBase ):

    def dispatch( self ):
        try:
            if self.path.startswith( "/js/" )  :
                filename = curdir + "/static/" + self.path
            else:
                filename = curdir + "/static/" + self.path
            #print "static dispatcher: " + filename

            f = open( filename )
            self.out = f.read()
            f.close()
            self.status = 200
            return
        except IOError:
            print "NOT FOUND: " + filename
            self.out = ""
            self.status = 404
            return

### END StaticDispatcher ###

class MainDispatcher( StaticDispatcher ):

    def dispatch( self ):
        print "main dispatcher"
        theme_pos = self.path.find( "theme=" )
        if theme_pos > 0:
            #print "Theme found at: " + theme_pos.__str__()
            theme = self.path[theme_pos + 6:]
            #print "New theme: " + theme
            self.config.staticTheme = theme
        self.path = self.config.staticTheme + "/index.html"
        StaticDispatcher.dispatch( self )

### END MainDispatcher ####

class DynamicDispatcher( DispatcherBase ):

    def __init__( self ):
        DispatcherBase.__init__( self )
        self.action = ""
        self.factory = Factory.Factory()
        return

    def dispatch( self ):

        t = self.path.rsplit( "/" )


        if t[0] == "action":
            base = 0
        elif t[1] == "action":
            base = 1
        else:
            print "ERROR: Action not found 1"
            return

        self.action = t[base + 1]

        if self.action == "":
            print "ERROR: Action not found 2"
            return

        action = self.factory.get( self.action )

        #t[base+2] is the optional (optional in URL, not in constructor) parameter for an action
        if len( t ) < ( base + 3 ):
            t.append( "" )


        try:
            action.do( t[base + 2] )
            self.out = action.out
            self.status = 200
        except:
            self.status = 500
        return

