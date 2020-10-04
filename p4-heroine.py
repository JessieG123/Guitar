import stddraw
import stdaudio
from picture import Picture
from guitarstring import GuitarString
#same class from problem 3

#client test file from the assignment basically

def frequency(keys_array, key):
    for i in range(len(keys_array)):
        if str(key)==keys_array[i]:
            return i
    return None

def string(i):
    note=((2**(1/12))**i)*110.00
    return note

keys_array=["q", "2", "w", "e", "4", "r", "5", "t", "y", "7", "u", "8", "i", "9", "o", "p", "-", "[", "=", "z", "x", "d", "c", "f", "v", "g", "b", "n", "j", "m", "k", ",", ".", ";", "/", "'", " "]

key_note=GuitarString(110.00)

guitar_string_array=[]
# show a nice background picture

p = Picture("cpsc231-guitar.png")

stddraw.picture(p)
stddraw.show(0.0)
escape = False

for i in range(len(keys_array)):
    note=string(i)
    key_note=GuitarString(note)
    guitar_string_array.append(key_note)

while not escape:
# check for and process events
    stddraw._checkForEvents()
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == chr(27):
            escape = True
        i=frequency(keys_array, key)
        if i!=None:
            guitar_string_array[i].pluck()
# simulate and play strings
    y=0
    for i in range(len(guitar_string_array)):
        y += guitar_string_array[i].tick()
    stdaudio.playSample(y)
