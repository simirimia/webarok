# -*- coding: utf-8 -*-
"""
a wrapper around file system operations

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

import os

class fileSystemHandler(object):
    
    def __init__(self, callback):
        self.callback = callback
    
    """
    get all filenames in a tree structure like
    
    basedir (e.g. /home/$USER/Music)
      |--> Artist (dir)
        |--> Album (dir)
          |--> Track (file)
    """
    def getLibrary(self, basedir):
        for artist in os.listdir(basedir):
            if os.path.isdir(basedir + "/" + artist) and artist != "." and artist != "..":
                self.getArtist( basedir + "/" + artist )
            elif os.path.isfile( basedir + "/" + artist ):
                self.getTrack( basedir + "/" + artist )
        pass
    
    """
    get all filenames in a tree structure like
    
    basedir (dir)
      |--> Album (dir)
        |--> Track (file)
    """
    def getArtist(self, basedir):
        for album in os.listdir(basedir):
            if os.path.isdir(basedir + "/" + album) and album != "." and album != ".." :
                self.getAlbum( basedir + "/" + album )
            elif os.path.isfile( basedir + "/" + album ):
                self.getTrack( basedir + "/" + album )
        pass
    
    """
    get all filenames in a tree structure like
    
    basedir (dir)
      |--> Track (file)
    """
    def getAlbum(self, basedir):
        for track in os.listdir(basedir):
            self.getTrack( basedir + "/" + track )
        pass
    
    def getTrack(self, filename):
        if filename[0] == '.':
            # omit hidden files
            return
        if filename[-4:] != '.mp3':
            print "only mp3 files supported so far"
            return
        print str(self.callback( filename )) + "\t\t<--->\t\t" + filename  
        pass