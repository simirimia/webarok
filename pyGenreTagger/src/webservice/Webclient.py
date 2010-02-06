# -*- coding: utf-8 -*-
"""
a wrapper around openanything.py

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

from webservice.openanything import fetch

import xml.dom.minidom
from string import replace

class Webclient( object ):
    
    def __init__(self):
        self.user_agent = "PyGenreTagger"
        self.lastData = ''
        
    def getTrackInfoByArtistAndTitle(self, artist, title):
        url = 'ws.audioscrobbler.com/2.0/?method=track.getinfo&api_key=3ade68a8e97b8b2d689cb15369499193&artist=' + artist + '&track=' + title
        url = replace( url, ' ', '+' )
        url = 'http://' + url
        return self.fetchDataDom(url)    
    
    def getTrackInfoByArtistAndAlbum(self, artist, album):
        url = 'ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=3ade68a8e97b8b2d689cb15369499193&artist=' + artist + '&album=' + album
        url = replace( url, ' ', '+' )
        url = 'http://' + url
        return self.fetchDataDom(url) 
    
    def getTrackInfoByArtist(self, artist):
        url = 'ws.audioscrobbler.com/2.0/?method=artist.getinfo&api_key=3ade68a8e97b8b2d689cb15369499193&artist=' + artist 
        url = replace( url, ' ', '+' )
        url = 'http://' + url
        return self.fetchDataDom(url)
        
    def fetch(self, url):
        try:
            return fetch( url, None, None, self.user_agent )
        except:
            return None
    
    def fetchDataDom(self, url):
        try:
            response = self.fetch(url)
            self.lastData = response['data']
            return xml.dom.minidom.parseString(response['data'])
        except:
            #print str(e)
            print "No data found"
            print response
            return None
        
    def getLastData(self):
        return self.lastData
        
    
