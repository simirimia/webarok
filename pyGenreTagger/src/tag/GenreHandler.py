# -*- coding: utf-8 -*-
"""
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


from mutagen.easyid3 import EasyID3
from string import upper

from webservice.Webclient import Webclient

class GenreHandler(object):
    
    tagBlacklist = [ 
                    # years
                    '00s','10s','20s','30s','40s','50s','60s','70s','80s','90s',
                    '1970', '1971','1972','1973','1974','1975','1976','1977','1978','1979',
                    '1980', '1981','1982','1983','1984','1985','1986','1987','1988','1989', 
                    '1990', '1991','1992','1993','1994','1995','1996','1997','1998','1999',
                    '2000','2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                    '2010',  
                    '90s metal', '80s heavy metal', '90s heavy metal', '80s hard rock', '80s rock','90s hard rock',
                    '21st century', '90s guitar music',
                    
                    # social tags
                    'albums i own', 'seen_live', 'seen live', 'favorites', 'favourite songs', 'song i have seen live', 
                    'all time faves', 'live', 'cds i own', 'once i was twenteen', 'favorite albums', 'favorite',
                    'all about me','favourite','i love it',
                    
                    # tags which are too general
                    'rock', 'xmas','rnr','pop',
                    
                    # moods
                    'sad', 'evening', 'melancholic','mutmacher','lalala','funny', 'gute laune', 'relax','evil',
                    'emo', 'schoenwedder', 'fun', 'freude', 'cheer me up', 'makes me sing', 'drinking music',
                    'moody', 'mellow', 'melancholy','herzzerreissend','angry','chillout','sanftmut',
                    
                    # cities / countries 
                    'deutsch','german','deutschrock', 'deutschpunk', 'deutscher punk rock', 'french rock', 'french',
                    'francophone', 'irish', 'irish punk', 'new york','german indie','berlin','british','german band',
                    'best of german',

                    # band/artist names
                    'die aerzte', 'die beste band der welt', 'dieaerzte', 'germacn punk', 'arzte gut', 'beste band der welt',
                    'bela b', 'thedoctors', 'favorite sleater-kinney songs','l7', 'nick cave', 'punk patti',
                    'elementofcrime-mittelpunktderwelt','katiejane garside','flap: daisy chainsaw',
                    
                    
                    # tags I personally dislike
                    'acoustic', 'instrumental', 'underrated', 'damn', 'metalcore', 'experimental', 'grindcore',
                    'pop punk', 'nwv', 'unplugged','le meilleur du rock francais', 'ls','grrlie', 'rage', 'riot',
                    'emusic', 'hardcore', 'vocal', 'xtc', 'remix', 'indie pop', 'singer-songwriter', 'classic rock',
                    
                    
                    # other non-genre tags
                    'kult', 'cover', 'outros', '2nd psuedoname derived from this', 'chuck berry cover', 'richard berry cover', 'under a minute',
                    'under two minutes', 'henryatlast', 'female fronted metal', 'female vocalists', 'nirvana cover', 'awesome covers',
                    'qwerot','blah', 'rolling stones cover','die wahren perlen deutschsprachiger popmusik',
                    'songs die so gut sind das ich meiner oma ihr klein haeuschen zwar nicht verkaufen aber zumindest dafuer beleihen wuerde',
                    'strange', 'gut', 'nonsense', 'coversong', 'das beste', '003', 'covers', 'leapsandbounds cdcollection', 
                    'dead kennedys cover', 'marvelous guitar','tribute', 'essentials', 'spring', 'beach songs', 'chick rock','thanks night ranger',
                    'political', 'joseph and jeny jam', 'whatever you exhale i breathe in in the end', 'painful truths', 'fuck you',
                    'beautiful', 'soundtracks and sunsets', 'screaming', 'i will not shout i will not scream', 'power songsssss',
                    'music that some cunt might like', 'the office girls', 'great albums', 'funky favs', 'gone kissin', 'sexy bitches',
                    'punk rock grrrl', 'zabij', 'butter', 'prda', 'crap', 'feminist', 'genius', 'queer', 'female voice', 'horrible album',
                    'star wars', 'energetic','gran turismo','jamiekicsarchive','kevin little', 'red', 'listen', 'indie rock favs',
                    'songs that i sing along to but i always forget the words so i say duh duh while trying to sound like i do know the words and no one is falling for it but they keep quiet because they are embarassed for me',
                    'fave songs ever','too short to exist as a track otherwise','cool','the songs that saved your life','prebrutalno :cerek:',
                    'apocalyptic folk', 'female vocals','haunting','bee gees cover','nice','good one','bitchrock','acclaimed music top 3000',
                    'stairway to hell','the pitchfork 500','texte sind ne eins','egomanie','mid','mia die aussicht','altundgut',
                    'swfav','nemetsfrass','moon','sex','slow','flap','groovy','derartig ratsam','gegen die widrigkeiten des lebens',
                    'in farbe','dudelsack','mariechentanz','ich scheiss auf deutsche texte',
                    'folk-rock','genre: goa','german indie rock','god','hysterical','immer wieder gerne','masterpiece','night','organ',
                    'psychoalgie','slordig','soundtrack','sprechgesang','super','trip-scape','uk','upbeat','wtf','wwwsinnfreichfavorit',
                    'z3po like this','waka rock song','60s revival','aleyster crowley','altparty','american','american guitar sound',
                    'angels voices','clawfinger','comique','cover song','creepy','drums','english','favorite indie','favourites',
                    'feat alison goldfrapp','female','female vocalist','fuck you bitch',
                    'german lyrics','good remix','great lyrics','guitar','guitar hero','hole-1991-pretty on the inside','hybrid theory ep',
                    'i could fuck to this','idle','kick ass','lady - cool','lieblingslieder','loud driving music','mitsingen',
                    'morning','my albums','piano','play it again sam','pop-punk','punk metal','rocking out','satan','schrammel',
                    'sexy','shock shock horror horror shock shock horror','songtitles containing the f-word','sorry','southside 2008',
                    'straight edge','synthpop','tanz metal','tiop asin okss','waka rock song','my garage is a mess','suedwind cd 1',
                    'only the top songs-no global artist-tags please','no future girls','girls in the garage','ma pierd in piesa asta',
                    'obv radical','eerie','chick-rock','songs under two minutes','meine heimatlieder','gute laune gitarren pop',
                    'world music','love it like le kittins on a stick','fantasterific','anyzio rocha','youth crew',
                    'get going','es ist egal','hot songs','songs i absolutely love','nielslive','intoxicated','gaensehaut',
                    'california seixas','heart major','artist to check out','naive','thisdrums''songs about love','vvussel'
                    ]
    
    tagMapping = {
                    'spoken word'               : 'speech', 
                    'punk rock'                 : 'punk',
                    'hardcore punk'             : 'punk',
                    'punk tracks'               : 'punk',
                    'pnk'                       : 'punk',
                    'punk-rock'                 : 'punk',
                    'p4nk7'                     : 'punk',
                    'gothic metal'              : 'gothic',
                    'gothic rock'               : 'gothic',
                    'indie rock'                : 'indie',
                    'prog'                      : 'progressive',
                    'progressive rock'          : 'progressive',
                    'alternative rock'          : 'alternative',
                    'riot girl'                 : 'riot grrrl',
                    'riot grrl'                 : 'riot grrrl',
                    'lovesongs'                 : 'ballad',
                    'love'                      : 'ballad',
                    'experimental industrial'   : 'industrial',
                    'electronics'               : 'electronic',
                    'electroclash'              : 'electronic',
                    'electropop'                : 'electronic',
                    'indie alternative hamburg' : 'hamburger schule',
                    'hamburg'                   : 'hamburger schule',
                    'alternativ'                : 'alternative',
                    'electro'                   : 'electronic',
                    'electronica'               : 'electronic',
                    'chanson francaise'         : 'chanson', 
                    'german chanson'            : 'chanson',
                    'experimental metal'        : 'metal',
                    'mittelalter'               : 'medieval',
                    'nu metal'                  : 'nu-metal',
                    'numetal'                   : 'nu-metal',
                    'industrial metal'          : 'industrial',
                    'heavy metal'               : 'metal',
                    'heavy-metal'               : 'metal',
                    'alternative metal'         : 'metal',
                    'alternative poprock'       : 'alternative', 
                    'garage rock'               : 'garage',
                    'post punk'                 : 'post-punk',
                    'medieval rock'             : 'medieval',
                    'ndh'                       : 'neue deutsche haerte',       
                   }
                  
    tagsUsed = []
    
    def __init__(self):
        self.mp3 = None
        self.client = Webclient()
        self.tagBlacklist = set(self.tagBlacklist)
    
    ''' filename with full path '''    
    def updateGenre(self, filename):
        genre = self.getGenre(filename)
        self.mp3['genre'] = unicode(genre)
        print "Saving.."
        self.mp3.save()
        return genre
        
    ''' filename with full path '''
    def getGenre(self, filename):
        tags = self.getTagsByArtistAndTitle(filename)
        genre = self.resolveTagsToGenre(tags)
        
        if genre == None:
            #print "Getting genre from album"
            tags = self.getTagsByArtistAndAlbum(filename)
            genre = self.resolveTagsToGenre(tags)
        
        if genre == None:
            #print "Getting genre from artist"
            tags = self.getTagsByArtist(filename)
            genre = self.resolveTagsToGenre(tags)
        
        genre = unicode(genre).capitalize()
        self.tagsUsed.append(genre)
    
    def getTagsByArtist(self, filename):
        self.getMp3(filename)
        if self.mp3 == None:
            return None
        artist =self.mp3['artist'][0].encode('utf-8')
        dom = self.client.getTrackInfoByArtist(artist)
        if dom == None:
            print "No response for file: " + filename
            #exit();
            return None
        return dom.getElementsByTagName('tag')   
    
    def getTagsByArtistAndAlbum(self, filename):
        self.getMp3(filename)
        if self.mp3 == None:
            return None
        artist =self.mp3['artist'][0].encode('utf-8')
        try:
            album = self.mp3['album'][0].encode('utf-8')
        except:
            album = ''
            
        dom = self.client.getTrackInfoByArtistAndAlbum(artist, album)
        if dom == None:
            print "No response for file: " + filename
            #exit();
            return None
        return dom.getElementsByTagName('tag')    
        
    def getTagsByArtistAndTitle(self, filename):
        self.getMp3(filename)
        if self.mp3 == None:
            return None
        artist =self.mp3['artist'][0].encode('utf-8')
        title = self.mp3['title'][0].encode('utf-8')
        dom = self.client.getTrackInfoByArtistAndTitle(artist, title)
        if dom == None:
            print "No response for file: " + filename
            #exit();
            return None
        return dom.getElementsByTagName('tag')    
        
    def resolveTagsToGenre(self,tags):
        if self.mp3 == None:
            return None
        if tags == None:
            return None
        
        artist =self.mp3['artist'][0].encode('utf-8')
        title = self.mp3['title'][0].encode('utf-8')
        
        try:
            album = self.mp3['album'][0].encode('utf-8')
        except:
            album = ''
        
        #try to get a useful genre
        for tag in tags:
            tagname =  tag.getElementsByTagName('name')[0].firstChild.data
            
            if ( upper(tagname) == upper(artist) ): 
                #print "artist found as tagname"
                continue
            if ( upper(tagname) == upper(album) ): 
                #print "album found as tagname"
                continue
            if ( upper(tagname) == upper(title) ): 
                #print "title found as tagname"
                continue
            if ( tagname in self.tagBlacklist ):
                #print "tag should be ignored"
                continue
            if ( self.tagMapping.has_key( tagname ) ):
                #print "Tag should be mapped to: " + self.tagMapping.get( tagname )
                return self.tagMapping.get( tagname )
        
            if tagname == None:
                print self.client.getLastData()
                exit();
        
            # none of the above rules applied, so take the current tagname as genre
            return tagname

        #print "No tags found"
        #print self.client.getLastData()
        return None
    
    def getMp3(self, filename):
        try:
            self.mp3 = EasyID3( filename )
        except:
            self.mp3 = None
            pass
    
    def getGenres(self):
        return set(self.tagsUsed)