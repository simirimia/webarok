"""
Base  class for mysql control

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
from Configuration import Configuration

class MyMySql( object ):

    def __init__( self ) :
        #print "init MyMySql class"
        self.initialized = False
        try:
            import MySQLdb
            self.config = Configuration.Configuration()
            if (self.config.useCollection != True):
                return
            self.db = MySQLdb.connect(self.config.mySqlOpts['host'], self.config.mySqlOpts['user'], self.config.mySqlOpts['pass'], self.config.mySqlOpts['db'])
            self.db.apilevel = "2.0"
            self.db.threadsafety = 2
            self.db.paramstyle = "format" 
            self.cursor = self.db.cursor()
        except:
            self.initialized = False
        return
    
    def isInitialized( self ):
        return self.initialized


