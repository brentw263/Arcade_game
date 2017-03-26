import pygame
import random
#Define some colors.
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)
blue  = (   0,   0, 255)

pi = 3.14

pygame.init()

#Set the width and height of the screen.
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow Animation")

#Loop until the user clicks the close button.
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

# Star position
star_list = []

for i in range(50):
    x = random.randrange(0,700)
    y = random.randrange(0,700)
    star_list.append([x,y])

#--------Main Program Loop--------
while done == False:

    #Event processing starts here
    for event in pygame.event.get(): #User did something.                       
        if event.type == pygame.QUIT: #If user clicked close.
            done = True #FLag that we are done so we exit this loop.

    #Event processing ends here

                           
    #First, clear the screen to white. Drawing commands
    #above this will be ignored.
    screen.fill(black)

    #Select font to use. None is default.
    font = pygame.font.Font(None,25)

    #Render the text. "True" means anti-aliased text.
    #Black is the color. The variable black was defined
    #above as a list of [0,0,0]
    #Note: This line creates an image of the letters,
    #but does not put it on the screen yet.
    text = font.render("My text", True, black)

    #Put the image of the text on the screen at 250x250
    screen.blit(text, [250,250])

    # Process each star in the list
    for i in range ( len ( star_list ) ):

        # Draw the star
        pygame.draw.circle( screen, white, star_list[i], 2)

        # Move the star down one pixel
        star_list[i][1] += 1

        #If the star has moved off the bottom of the screen
        if star_list[i][1] > 700:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            star_list[i][1] = y
            # Give it a new position
            x = random.randrange(0,500)
            star_list[i][0] = x

    
    #End Drawing

    #Update the screen with what we've drawn.
    pygame.display.flip()

    #Limit to 20 frames per second.
    clock.tick(20)

pygame.quit()
