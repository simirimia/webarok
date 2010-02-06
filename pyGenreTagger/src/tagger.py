# -*- coding: utf-8 -*-
"""
Use the lastfm most used tag as mp3 genre tag. Upate mp3 files automatically with this info.

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

from fileHandling.fileSystemHandler import fileSystemHandler  
from tag.GenreHandler import GenreHandler
    
    
#from mutagen.easyid3 import EasyID3
#print EasyID3.valid_keys.keys()
    
basedir = "/home/verena/Musik"
counter = 0

genre = GenreHandler()

handler = fileSystemHandler( genre.getGenre )
handler.getLibrary(basedir)

#handler = fileSystemHandler( genre.updateGenre )
#handler.getArtist( '/home/verena/Musik/Ash' )
                   
#handler.getTrack( "/home/verena/Musik/Patti Smith/Horses/07 Land_ Horses _ Land of a Thousand Dances _ La Mer (De) (1).mp3" )
                   
print "===================================================================================================="
genres = genre.getGenres()
for g in genres:
    print g








                                                   

