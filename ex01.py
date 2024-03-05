
'''Create a class called Music with the attributes'''

class Music:
    name = ''
    artist = ''
    duration = ''

music1 = Music()
music1.name = 'Bohemian Rhapsody'
music1.artist = 'Queen'
music1.duration = 355

music2 = Music()
music2.name = 'Imagine'
music2.artist = 'John Lennon'
music2.duration = 183

music3 = Music()
music3.name = 'Shape of You'
music3.artist = 'Ed Sheeran'
music3.duration = 234

print(f'Music: {music1.name} - Artist: {music1.artist} - {music1.duration} seconds')
print(f'Music: {music2.name} - Artist: {music2.artist} - {music2.duration} seconds')
print(f'Music: {music3.name} - Artist: {music3.artist} - {music3.duration} seconds')
    