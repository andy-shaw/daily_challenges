'''
Andy Shaw
7/1/2014

Spit out weight on other planets
'''

import math
import sys

class Planet(object):
    '''Planet'''
    def __init__(self, name, radius, density, G=0.0000000000667):
        '''Need name, radius(meters), and density'''
        self.name = name
        self.r = float(radius)
        self.density = float(density)
        self.G = G

    def weight(self, mass):
        return self.G * ((self.mass() * mass) / math.pow(self.r,2))

    def mass(self):
        return self.volume() * self.density

    def volume(self):
        return 4.0/3.0 * math.pi * math.pow(self.r, 3.0)

    def toString(self):
        return '\t'.join((self.name, str(self.r), str(self.density)))

if __name__ == '__main__':
    #read in planet info
    planets = {}
    for line in open('gravity_input.txt', 'r').readlines():
        stats = line.strip().split(',')
        planets[stats[0]] = Planet(stats[0], stats[1], stats[2])

    lens = []
    for p in planets.keys():
        lens.append(len(p))
    max_len = max(lens)

    mass = int(sys.argv[1])
    for planet in planets.values():
        print (planet.name + ':').ljust(max_len+1), planet.weight(mass)