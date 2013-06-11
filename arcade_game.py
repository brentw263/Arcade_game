import pygame

pi = 3.141592653

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My awesome game!)

#Loop until the user clicks the close button.
done = False

#Used to manage how fast the screen updates
clock = pygame.time.clock()

#--------Main Program Loop--------
while done = False:

    #ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): #User did something.                       
        if event.type == pygame.QUIT: #If user clicked close.
            done = True #FLag that we are done so we exit this loop.

    #ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


    #ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT.

    #ALL GAME LOGIC SHOULD GO ABOYVE THIS COMMENT.


    #ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT.

    #ALL CODE TO DRAW SHOULE GO ABOVE THIS COMMENT.

    #Limit to 20 frames per second.
    clock.tick(20)
