'''

Student Name: Mugdha Chakma
Student ID  : 22122847

Version History:
    - 14/10/24 - original version released

'''

import matplotlib.pyplot as plt
import numpy as np
from canopy import House, Tree, Sky, Land, Cat, Dog, Sun, Water


# initalize frame width and height
XMAX = 1000
YMAX = 500
    
def main():

    step_count = 30 # timestamp count variable 
    # cat and dog are two animals
    
    c1 = Cat([100,100])
    c2 = Cat([180,100])
    c1.set_time_mature(int(step_count / 2)) # at half stage change state and double the size
    c2.set_time_mature(int(step_count / 2)) # at half stage change state and double the size
    
    d1 = Dog([120,95])
    d2 = Dog([80,150])
    d1.set_time_mature(int(step_count / 2)) # at half stage change state and double the size
    d2.set_time_mature(int(step_count / 2)) # at half stage change state and double the size

    cats = [c1, c2]
    dogs = [d1, d2]

    land_boudary = int(YMAX / 2) # sky and land meets at half the frame

    sky_colors = ["#87CEEB", "#2e86c1","#1b4f72"] # list of colors to change with the position of sun
    sky = Sky(sky_colors[0], (land_boudary, XMAX)) 

    land_colors = ['#48c9b0', '#17a589', "#0b5345"] # list of land colors to change with the position of sun
    land = Land(land_colors[0], (0, land_boudary))
    sun = Sun([int(XMAX / 2), 400], "#FFCC33", 1000)
    

    house1 = House([200, 250], '#edbb99', 4000)

    # init tree width and height
    tree_width = 20 
    tree_height = 150
    tree1 = Tree ([50, 180], "#78281f", [tree_width, tree_height])
    tree2 = Tree ([650, 140], "#78281f", [tree_width, tree_height])
    tree3 = Tree ([800, 160], "#78281f", [tree_width, tree_height])

    water = Water([850, XMAX], [land_boudary - 20, 100], "#79b7eb")
    
    plt.title("Simulation with Houses, Trees, Roads and characters")  # title of the plot

    
    pets_in_yard = True # variable to control position of the pets. outside the fence after half steps

    for i in range(step_count):
        print("\n ### TIMESTEP ",i, "###")
        

        if sun.get_pos()[1] > land_boudary + 20:
            # condition to check if the sun is at top
            # set the sky and land colors and pet position
            sky.set_colour(sky_colors[0])
            land.set_colour(land_colors[0])
            if not pets_in_yard:
                for c in cats:
                    c.set_pos_in_yard()
                
                for d in dogs:
                    d.set_pos_in_yard()
            pets_in_yard = True
        elif sun.get_pos()[1] <= land_boudary - 60:
            # condition to check if its night
            # reset the sun position to be morning and change sky and land color
            sun.reset_pos()
            sky.set_colour(sky_colors[0])
            land.set_colour(land_colors[0])
        elif sun.get_pos()[1] <= land_boudary - 20:
            # condition to check if its evening
            # change sky and land color
            sky.set_colour(sky_colors[2])
            land.set_colour(land_colors[2])
        else:
            # condition to check if its morning
            # change sky and land color
            sky.set_colour(sky_colors[1])
            land.set_colour(land_colors[1])
            if pets_in_yard:
                for c in cats:
                    c.set_pos_in_field()
                
                for d in dogs:
                    d.set_pos_in_field()
            pets_in_yard = False

        # plot sun, sky and land
        plt.fill_between([0, XMAX], sky.get_size()[0], sky.get_size()[1], color=sky.get_colour()) # plot sky
        plt.scatter(sun.get_pos()[0], sun.get_pos()[1], c= sun.get_colour(), s=sun.get_size()) # plot sun
        plt.fill_between([0, XMAX], land.get_size()[0], land.get_size()[1], color=land.get_colour()) # plot land
        plt.fill_between(water.posX, water.posY[0], water.posY[1], color = water.get_colour()) # plot water
        

        # plot road and road lines
        road_boundary = 70 # road Y axis boundary in the frame
        plt.fill_between([0, XMAX], 30, road_boundary, color='#707b7c') # plot road
        plt.plot([0, XMAX], [50, 50], color='yellow', linestyle='--', linewidth=2) # plot road lines

        # plot house and fences
        plt.scatter(house1.get_coord()[0], house1.get_coord()[1], c=house1.get_colour(), s=house1.get_size(), marker="s")
        roofx_coords = [100, 300, 200]  # x-coordinates of the triangle roof vertices
        roofy_coords = [300, 300, 400]  # y-coordinates of the triangle roof vertices
        plt.fill(roofx_coords, roofy_coords, color='#78281f') # fill the roof with color 

        plt.fill_between([310, 320], 90, 250, color='#212f3d') # fence right
        plt.fill_between([10, 20], 90, 250, color='#212f3d') # fence left


        # tree1 with leaves
        plt.fill_between([tree1.get_coord()[0], tree1.get_coord()[0] + tree_width], tree1.get_coord()[1], tree1.get_coord()[1] + tree_height, color=tree1.get_colour())
        plt.fill_between([tree1.get_coord()[0] - 20, tree1.get_coord()[0] + tree_width + 20], tree1.get_coord()[1] + tree_height - 20, tree1.get_coord()[1] + tree_height + 20, color="#145a32")

        # tree2 with leaves
        plt.fill_between([tree2.get_coord()[0], tree2.get_coord()[0] + tree_width], tree2.get_coord()[1], tree2.get_coord()[1] + tree_height, color=tree2.get_colour())
        plt.fill_between([tree2.get_coord()[0] - 20, tree2.get_coord()[0] + tree_width + 20], tree2.get_coord()[1] + tree_height - 20, tree2.get_coord()[1] + tree_height + 20, color="#145a32")

        # tree3 with leaves
        plt.fill_between([tree3.get_coord()[0], tree3.get_coord()[0] + tree_width], tree3.get_coord()[1], tree3.get_coord()[1] + tree_height, color=tree3.get_colour())
        plt.fill_between([tree3.get_coord()[0] - 20, tree3.get_coord()[0] + tree_width + 20], tree3.get_coord()[1] + tree_height - 20, tree3.get_coord()[1] + tree_height + 20, color="#145a32")

        cxvalues = []
        cyvalues = []
        csizes = []
        
        # cats step change
        for c in cats:
            c.stepChange(0, XMAX, land_boudary, road_boundary)
            cxvalues.append(c.pos[0])
            cyvalues.append(c.pos[1])
            csizes.append(c.get_size())

        dxvalues = []
        dyvalues = []
        dsizes = []


        # dogs step change
        for d in dogs:
            d.stepChange(0, XMAX, land_boudary, road_boundary)
            dxvalues.append(d.pos[0])
            dyvalues.append(d.pos[1])
            dsizes.append(d.get_size())

        # plot the pets
        plt.scatter(cxvalues, cyvalues, csizes, color="orange")  
        plt.scatter(dxvalues, dyvalues, s=dsizes, color="#ba4a00")  

        # sun goes down at each iteration
        sunX, sunY = sun.get_pos()
        sun.set_pos([sunX, sunY - 15]) 
        
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        
        plt.pause(1)
        plt.clf()
    
if __name__ == "__main__":
    main()
