import pygame

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

    #ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT.


    #ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT.
                           
    #First, clear the screen to white. Don't put any other drawing commeands
    #above this or they will be erased.
    screen.fill(white)

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

    for y_offset in range(0,100,10):
        pygame.draw.line(screen,green,[0,10+y_offset],[100,110+y_offset],5)
        pygame.draw.line(screen,green,[100,-10+y_offset],[0,-110+y_offset],5)
        pygame.draw.rect(screen,black,[20,20,250,100],2)
        pygame.draw.ellipse(screen,black,[20,20,250,100],2)
        pygame.draw.arc(screen,green,[100,100,250,200],  pi/2,    pi,2)
        pygame.draw.arc(screen,black,[100,100,250,200],     0,  pi/2,2)
        pygame.draw.arc(screen,red  ,[100,100,250,200],3*pi/2,  2*pi,2)
        pygame.draw.arc(screen,blue ,[100,100,250,200],    pi,3*pi/2,2)
        pygame.draw.polygon(screen,green,[[100,50],[400,20],[30,200]],5)
    #ALL CODE TO DRAW SHOULE GO ABOVE THIS COMMENT.

    #Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    #Limit to 20 frames per second.
    clock.tick(20)

#CLose the window and quit.
#If you forget this line, the program will hang.
#on exit if running from IDLE.
pygame.quit()
