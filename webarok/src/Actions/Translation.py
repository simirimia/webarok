"""
Retrive translation

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
from Actions import ActionBase
import ConfigParser
from json import JSONEncoder

class Translation( ActionBase.ActionBase ):
    def do( self, param ):
        lang = self.config.language

        config = ConfigParser.RawConfigParser()
        filename = 'lang/' + lang + '.ini'
        config.readfp(open(filename))

        translation = {
                       'trans_artist' : config.get( 'webarok', 'artist' ),
                       'trans_album' : config.get( 'webarok', 'album' ),
                       'trans_duration' : config.get( 'webarok', 'duration' ), 
                       'trans_main' : config.get( 'webarok', 'main' ),
                       'trans_playlist' : config.get( 'webarok', 'playlist' ),
                       'trans_lyrics' : config.get( 'webarok', 'lyrics' ),
                       'trans_track' : config.get( 'webarok', 'track' ),
                       'trans_search' : config.get( 'webarok', 'search' ),
                       'trans_status' : config.get( 'webarok', 'status' ),
                       'trans_loading' : config.get( 'webarok', 'loading' ),
                       'trans_settings' : config.get( 'webarok', 'settings' ),
                       'trans_opt_autorefresh' : config.get( 'webarok', 'opt_autorefresh' ),
                       'trans_autorefresh_volume' : config.get( 'webarok', 'autorefresh_volume' ),
                       'trans_autorefresh_progress' : config.get( 'webarok', 'autorefresh_progress' ),
                       'trans_autorefresh_status' : config.get( 'webarok', 'autorefresh_status' ),
                       'trans_autorefresh_playlist' : config.get( 'webarok', 'autorefresh_playlist' ),
                       'trans_about' : config.get( 'webarok', 'about' ),
                       'trans_the_playlist' : config.get( 'webarok', 'the_playlist' ),
                       'trans_no_result' : config.get( 'webarok', 'no_result' ),
                       'trans_search_with_mysql' : config.get( 'webarok', 'search_with_mysql' ),
                       'trans_artists' : config.get( 'webarok', 'artists' ),
                       'trans_tracks' : config.get( 'webarok', 'tracks' ),
                       'trans_all' : config.get( 'webarok', 'all' ),
                       'trans_search_button' : config.get( 'webarok', 'trans_search_button' ),
                       'trans_no_lyrics' : config.get( 'webarok', 'trans_no_lyrics' ),
                       'trans_refresh_data_button' : config.get( 'webarok', 'refresh_data_button' )
                       }
        
        encoder = JSONEncoder()

        self.out = encoder.encode( translation )
        return
    



