from json import JSONEncoder

class VolumeView( object ):

    def __init__( self, volume ):
        self.volume = volume

    def render( self ):
        encoder = JSONEncoder()
        return encoder.encode( self.volume.getDictionary() )
