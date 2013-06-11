import pygame

#Define some colors.
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)

pygame.init()

#Set the width and height of the screen.
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Scuda Bang!")

#Loop until the user clicks the close button.
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#--------Main Program Loop--------
while done == False:

    #ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): #User did something.                       
        if event.type == pygame.QUIT: #If user clicked close.
            done = True #FLag that we are done so we exit this loop.

    #ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


    #ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT.

    #ALL GAME LOGIC SHOULD GO ABOYVE THIS COMMENT.


    #ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT.
                           
    #First, clear the screen to white. Don't put any other drawing commeands
    #above this or they will be erased.
    screen.fill(white)

    for y_offset in range(0,100,10):
        pygame.draw.line(screen,green,[0,10+y_offset],[100,110+y_offset],5)
        
    #ALL CODE TO DRAW SHOULE GO ABOVE THIS COMMENT.

    #Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    #Limit to 20 frames per second.
    clock.tick(20)

#CLose the window and quit.
#If you forget this line, the program will hang.
#on exit if running from IDLE.
pygame.quit()
