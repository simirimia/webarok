#!/usr/bin/env python

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

import getopt, sys, os

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "ghm:b:", ["gui", "help", "mode=", "basedir="])
    except getopt.GetoptError, err:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
        
    mode = ''
    basedir = ''
    startGui = False
        
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-b", "--basedir"):
            basedir = a
        elif o in ("-m", "--mode"):
            mode = a
        elif o in ("-g", "--gui"):
            startGui = True
        else:
            assert False, "unhandled option"
            
    if startGui == True:
        from gui.App import run 
        run()
        sys.exit(0)
    
    if not ( mode=='dry' or mode=='update' ):
        print "No valid mode given"
        print
        usage()
        sys.exit(2)
    
    if not os.path.isdir( basedir ):
        print "No valid basedir given. Must be an existing directory"
        print
        usage()
        sys.exit(2)
    
    from fileHandling.fileSystemHandler import fileSystemHandler  
    from tag.GenreHandler import GenreHandler
    from log.log import log
    
    print "mode is: " + mode
    print "basedir is " + basedir 
    
    genre = GenreHandler()
    theLog = log( 'doPrint' )
    
    if mode=='update':
        handler = fileSystemHandler( genre.updateGenre, theLog )
    else:
        handler = fileSystemHandler( genre.getGenre, theLog )
    
    # Let's go!!!
    handler.getLibrary(basedir)
    
    print
    print "===================================================================================================="
    print "==================================   Genres used   ================================================="
    print "===================================================================================================="
    genres = genre.getGenres()
    for g in genres:
        print g
    
    # actually not really neccessary anymore
    #handler.getArtist( '/home/verena/Musik/Ash' )
    #handler.getTrack( '/home/verena/Musik/Green Day/American Idiot/11 Wake Me Up When September Ends.mp3' )
    
    
 
def usage():
    print "    tagger.py -m MODE -b BASEDIR"
    print "or  tagger.py -g [--gui] starts a simple KDE gui"
    print
    print "mode is either dry for a dryrun or update for really updating the files"
    print "use -m MODE or --mode=MODE"
    print "    -b BASEDIR or --basedir=BASEDIR"
    print
    print "BASEDIR must be an absolute path"
    print
    print "python-mutagen must be installed"
    print


if __name__ == "__main__":
    main()
