# -*- coding: utf-8 -*-
import MediaObjects
from json import JSONEncoder

class SongView( object ):

    def  __init__( self, song ):
        self.song = song

    def render( self ):
        encoder = JSONEncoder()
        return encoder.encode( self.song.getDictionary() )


    def renderHtml( self ):
        html = ""

        html += "<div class=""art"">"
        html += " <img width=""150px"" height=""150px"" src='/action/Art/" + self.song.albumart_remote_file + "'>"
        html += "</div>"

        html += " <div class = ""song""> "
        html += " <div class = ""description"" > Title: </div> "
        html += " <div class = ""value"" > " + self.song.title + " </div> "
        html += " <div class = ""description"" > Artist: </div > "
        html += " <div class = ""value"" > " + self.song.artist + " </div> "
        html += " <div class = ""description"" > Album: </div > "
        html += " <div class = ""value"" > " + self.song.album + " </div> "
        html += " <div class = ""description"" > Duration: </div> "
        html += " <div class = ""value"" > " + self.song.time.__str__() + " </div> "
        html += " </div> "

        return html
