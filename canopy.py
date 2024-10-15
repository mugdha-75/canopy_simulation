'''

Student Name: Mugdha Chakma
Student ID  : 22122847

Version History:
    - 14/10/24 - original version released

'''

import random
import numpy as np
import matplotlib.pyplot as plt

class Tree():

    def __init__(self, pos, colour, size):
        self.pos = pos
        self.colour_code = colour
        self.size = size     

    def get_coord(self):
        return self.pos

    def get_size(self):
        return self.size

    def get_colour(self):
        return self.colour_code

    def set_size(self, size):
        self.size = size

    def set_colour(self, colour):
        self.colour_code = colour  

    def __str__(self):
        return f"Tree: {self.pos}"


class House:
    def __init__(self, pos, colour, size):
        self.pos = pos
        self.colour_code = colour
        self.size = size   

    def get_coord(self):
        return self.pos

    def get_coord(self):
        return self.pos

    def get_size(self):
        return self.size

    def get_colour(self):
        return self.colour_code
    


class Sky:
    def __init__(self, colour, size):
        self.colour_code = colour
        self.size = size

    def get_size(self):
        return self.size 
    

    def get_colour(self):
        return self.colour_code
    

    def set_colour(self, code):
        self.colour_code = code


class Land:
    def __init__(self, colour, size):
        self.colour_code = colour
        self.size = size

    def get_size(self):
        return self.size 
    

    def get_colour(self):
        return self.colour_code
    

    def set_colour(self, code):
        self.colour_code = code

class Water:
    def __init__(self, posX, posY, colour):
        self.colour_code = colour
        self.posX = posX
        self.posY = posY
    

    def get_colour(self):
        return self.colour_code
    

    def set_colour(self, code):
        self.colour_code = code


class Sun:
    def __init__(self, pos, colour, size):
        self.colour_code = colour
        self.size = size
        self.pos = pos
        self.initpos = pos

    
    def get_pos(self):
        return self.pos
    
    def reset_pos(self):
        self.pos = self.initpos
    
    def set_pos(self, pos):
        self.pos = pos 

    def get_size(self):
        return self.size 
    

    def get_colour(self):
        return self.colour_code
    

    def set_colour(self, code):
        self.colour_code = code


class Cat():

    time2mature = 4
    states = ["kitten","mature"]
    
    def __init__(self, pos, size=25, age=1):
        self.pos = pos
        self.size = size
        self.initpos = pos
        self.age = age
        self.state = self.states[0]
        
    def __str__(self):
        return self.state + " @ " + str(self.pos)
    
    def set_time_mature(self, age):
        self.time2mature = age
    
    def set_pos_in_field(self):
        self.pos = [300 + self.initpos[0], self.initpos[1]]

    def set_pos_in_yard(self):
        self.pos = [self.initpos[0], self.initpos[1]]
    
    def stepChange(self, XMIN, XMAX, land_boudary, road_boundary):
        xmov = random.choice([10, 0, -10])
        ymov = random.choice([10, 0, -10])

        # condition to check if the animal is moving out of frame in X axis
        while self.pos[0] + xmov <= XMIN or self.pos[0] + xmov >= XMAX:
            xmov = random.choice([-10, 10])
        
        # condition to check if the animal is moving out of boundary (sky and road)
        while self.pos[1] + ymov >= land_boudary or self.pos[1] + ymov <= road_boundary:
            ymov = random.choice([-10, 10])
        
        self.age += 1
        if self.state == self.states[0] and self.age > self.time2mature:
            self.state = self.states[1]
            self.size = self.size * 2

        self.pos[0] += xmov
        self.pos[1] += ymov
    
    def get_size(self):
        return self.size
                        

class Dog():

    time2mature = 4
    states = ["puppy","mature"]

    def __init__(self, pos, size = 50, age =1):
        self.pos = pos
        self.size = size
        self.initpos = pos
        self.age = age
        self.state = self.states[0]
        
        
    def __str__(self):
        return self.state + " @ " + str(self.pos)
    
    def set_pos_in_field(self):
        self.pos = [300 + self.initpos[0], self.initpos[1]]

    def set_time_mature(self, age):
        self.time2mature = age
    
    def stepChange(self, XMIN, XMAX, land_boudary, road_boundary):

        # choose a random step in the surrounding 
        xmov = random.choice([10, 0, -10])
        ymov = random.choice([10, 0, -10])

        # condition to check if the animal is moving out of frame in X axis
        while self.pos[0] + xmov <= XMIN or self.pos[0] + xmov >= XMAX:
            xmov = random.choice([-10, 10])
        
        # condition to check if the animal is moving out of boundary (sky and road)
        while self.pos[1] + ymov >= land_boudary or self.pos[1] + ymov <= road_boundary:
            ymov = random.choice([-10, 10])
        
        self.age += 1
        if self.state == self.states[0] and self.age > self.time2mature:
            self.state = self.states[1]
            self.size = self.size * 2

        self.pos[0] += xmov
        self.pos[1] += ymov
    
    def set_pos_in_yard(self):
        self.pos = [self.initpos[0], self.initpos[1]]

    def get_size(self):
        return self.size