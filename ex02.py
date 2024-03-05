'''Class Music 2'''

class Music:
    def __init__(self, name='', artist='', duration=0):
        self.name = name
        self.artist = artist
        self.duration = duration
    
music1 = Music(name='Under Pressure', artist='Queen & David Bowie', duration=248)
music2 = Music(name='The Tropper', artist='Iron Maiden', duration=245)
music3 = Music(name='Hotel California', artist='Eagles', duration=390)