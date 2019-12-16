# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
 

while True:
    speed = input('How fast do you want the labyrinth to move? [Answer (seconds): 1, 3, 5, 10] >>>')
    if speed == '1':
        speed = 60
        break
    if speed == '3':
        speed = 180
        break
    if speed == '5':
        speed = 300
        break
    if speed == '10':
        speed = 600
        break
    else:
        print()
        print('Please enter 1, 3, 5 or 10')
       
while True:
    speed = input('How fast do you want the labyrinth to move? [Answer (seconds): 1, 3, 5, 10] >>>')
    if speed == '1':
        speed = 60
        break
    if speed == '3':
        speed = 180
        break
    if speed == '5':
        speed = 300
        break
    if speed == '10':
        speed = 600
        break
    else:
        print()
        print('Please enter 1, 3, 5 or 10')


       
       
class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """
 
    # Set speed vector
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([6, 6])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Room(object):
    """ Base class for all rooms. """
 
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
##################################################################################################################
##################################################################################################################
##################################################################################################################
import random

le =20
we = 20
class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = []
       

        for i in range(900 ):
            walls.append([random.randint(20,970),random.randint(20,570),le,we,BLUE])
       
       

        walls = walls+[[0, 0, 1000, 60, RED], [0, 0, 30, 600, RED], [970, 0, 30, 1000, RED],[0, 570, 1000, 30, RED]]

       
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 

 
 
def main():
    """ Main Program """
 
    # Call this function so the Pygame library can initialize itself
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([1000, 600])
 
    # Set the title of the window
    pygame.display.set_caption('Quantum Maze Runner')
   
 
    # Create the player paddle object
    player = Player(0,0)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
   
   
 
    rooms = []
 
    room = Room1()
    rooms.append(room)
 
 
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    clock = pygame.time.Clock()
 
    done = False
   
    changecount = 0
   
   
   
    while not done:
       
        if changecount % speed ==0:
            rooms = []
 
            room = Room1()
            rooms.append(room)
 
 
            current_room_no = 0
            current_room = rooms[current_room_no]
 
        clock = pygame.time.Clock()
 
        # --- Event Processing ---
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-2.5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(2.5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -2.5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 2.5)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(2.5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-2.5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 2.5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -2.5)
                   
 
        # --- Game Logic ---
 
        player.move(current_room.wall_list)
 

 
        # --- Drawing ---
        screen.fill(BLACK)
 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)
       
        changecount +=1
 
    pygame.quit()
 
if __name__ == "__main__":
    main()
