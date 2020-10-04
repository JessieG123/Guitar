import collections
import math
import random

class GuitarString:
    def __init__(self, frequency):
        #define p
        self.p=math.ceil(44100/frequency)
        #make a wavetable
        self.data=collections.deque()
        for i in range(self.p):
            self.data.append(0.0)
    def pluck(self):
        #clear wavetable
        self.data.clear()
        #fill with white noise from -0.5 to 0.5
        for i in range(self.p):
            self.data.append(random.uniform(-0.5, 0.5))
        return self.data
    def tick(self):
        y=0.996*(0.5*(self.data[0]+self.data[1]))
        self.data.popleft()
        self.data.append(y)
        return y 
