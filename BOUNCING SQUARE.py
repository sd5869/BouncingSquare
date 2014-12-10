import pygame
import random
# collision
def collision(score,rect_x,rect_y):
    score_sound = pygame.mixer.Sound("pop.ogg")
    miss_sound = pygame.mixer.Sound("miss.wav")
    pos = pygame.mouse.get_pos()
    xm = pos[0]
    ym = pos[1]
    if ((xm>=rect_x) and (ym>=rect_y )and (xm<=(rect_x+50)) and (ym<=(rect_y+50))):
        score+=5
        score_sound.play()
    else:
        score-=3
        miss_sound.play()
    return score
    #score display
def disp(screen,score):
            
            screen.fill(black)
            # Select the font to use, size, bold, italics
            font = pygame.font.SysFont('freesansbold.ttf', 70, True, False)
            # Render the text. "True" means anti-aliased text.
            # Note: This line creates an image of the letters,
            # but does not put it on the screen yet.
            text = font.render("SCORE:"+str(score),True,green)
            cx = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            cy = ( SCREEN_HEIGHT// 2) - (text.get_height() // 2)
            # Put the image of the text on the screen at 250x250
            screen.blit(text, [cx,cy]) 
            pygame.display.flip()
            clock = pygame.time.Clock()
            for i in range (1000):
                clock.tick(1000)
         #time calc       
def timel(frame_count):
    frame_rate = 20
    start_time = 60
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0 
    return total_seconds

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (  21,   0, 255)
yellow   = ( 255, 255,   0)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# -------- Collision Mode -----------

def colmode(screen):
        #---main program---
    pygame.init()   
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    #random colour
    x=[black,white,red,blue,yellow]
    # Starting position of the rectangle
    rect_x = 50
    rect_y = 50
    # data
    score  = 0
    ctr=0
    flag=0
    collide_sound = pygame.mixer.Sound("collision.wav")
    # Speed and direction of rectangle
    rect_change_x = 5
    rect_change_y = 5
    while done == False:
        #loop for event handleing
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                 done = True # Flag that we are done so we exit this loop           
                 disp(screen,score)
            if event.type==pygame.MOUSEBUTTONDOWN:
                score=collision(score,rect_x,rect_y)                
        # Set the screen background
        screen.fill(black)
        pygame.display.set_caption("BOUNCING SQUARE             Score:"+str(score)+ "       COLLISIONS:"+str(ctr))
        # Draw the rectangle
        i=random.randrange(5)
        j=random.randrange(5)
        pygame.draw.rect(screen, x[i], [rect_x, rect_y, 50, 50])
        pygame.draw.rect(screen, green, [rect_x + 10, rect_y + 10, 30, 30])      
        # Move the rectangle starting point        
        rect_x += rect_change_x
        rect_y += rect_change_y
        # Bounce the ball if needed
        if rect_y >SCREEN_HEIGHT-50 or rect_y < 0:
            rect_change_y = rect_change_y * -1
            ctr+=1
            collide_sound.play()
        if rect_x > SCREEN_WIDTH-50 or rect_x < 0:
            rect_change_x = rect_change_x * -1
            ctr+=1
            collide_sound.play()
        # Limit to 20 frames per second
        clock.tick(20)       
        if(ctr>=20):
                    pygame.display.set_caption("BOUNCING SQUARE             Score:"+str(score)+ "       COLLISIONS:"+str(ctr))
                    disp(screen,score)
                    done = True # Flag that we are done so we exit this loop
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        if(score!=0 and score>=100*flag ):
                rect_change_x +=2
                rect_change_y +=2
                score+=5
                flag+=1

          #---Time Mode---
def time_mode(screen):      
    pygame.init()
    collide_sound = pygame.mixer.Sound("collision.wav")
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    #random colour
    x=[black,white,red,blue,yellow]
    # Starting position of the rectangle
    rect_x = 50
    rect_y = 50
    # data
    score  = 0
    flag=0   
    time_left=0
    frame_count = 0
    # Speed and direction of rectangle
    rect_change_x = 5
    rect_change_y = 5
        # -------- Main Program Loop -----------
    while done == False:
        #loop for event handleing
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                 done = True # Flag that we are done so we exit this loop           
                 disp(screen,score)
            if event.type==pygame.MOUSEBUTTONDOWN:
                score=collision(score,rect_x,rect_y)                
        # Set the screen background
        screen.fill(black)
        pygame.display.set_caption("BOUNCING SQUARE             Score:"+str(score)+ "       TIME LEFT:"+str(time_left))
        # Draw the rectangle
        i=random.randrange(5)
        j=random.randrange(5)
        pygame.draw.rect(screen, x[i], [rect_x, rect_y, 50, 50])
        pygame.draw.rect(screen, green, [rect_x + 10, rect_y + 10, 30, 30])      
        # Move the rectangle starting point        
        rect_x += rect_change_x
        rect_y += rect_change_y
        # Bounce the ball if needed
        if rect_y >SCREEN_HEIGHT-50 or rect_y < 0:
            rect_change_y = rect_change_y * -1
            collide_sound.play()       
        if rect_x > SCREEN_WIDTH-50 or rect_x < 0:
            rect_change_x = rect_change_x * -1
            collide_sound.play()         
        # --- Timer going down ---
        time_left=timel(frame_count)
        frame_count += 1
        # Limit to 20 frames per second
        clock.tick(20)        
        if(time_left==0):
                    pygame.display.set_caption("BOUNCING SQUARE             Score:"+str(score)+ "       TIME LEFT:"+str(time_left))
                    disp(screen,score)
                    done = True # Flag that we  are using to exit loop
        # Go ahead and update the screen with what we've drawn.
        pygame.init()
        pygame.display.flip()
        if(score!=0 and score>=100*flag):
                rect_change_x +=2
                rect_change_y +=2
                score+=5
                flag+=1
        
#credits
def credit(screen):
    font = pygame.font.Font('freesansbold.ttf', 41)
    info_list=["This game has been created by ",
               "sd5869. All sprites used in this ",
               "game have been downloaded from ",
               "OpenGameArt.org.",
               "For any bugs or suggestions, ",
               "E-mail me at sd5869@gmail.com."]
    for i in range(len(info_list)):
        text=font.render(info_list[i],True,white)
        screen.blit(text, [10, (10+40*i)])

# how to play
def htp(screen):
    font = pygame.font.Font('freesansbold.ttf', 38)
    info_list=["You have to click on the Bouncing ",
               "Square.Beaware,only click on",
               "Square if you click outside it,you",
               "may end up scoring negative points.",
               "The game has two playing modes :",
               "1. Collision Mode: In this mode you",
               "have to score in limited collisions",
               " of Square with wall.",
               "2. Time Mode: In this mode you",
               "have to score in limited time."]
    for i in range(len(info_list)):
        text=font.render(info_list[i],True,white)
        screen.blit(text, [10, (10+40*i)])

# back button
def back(screen,a):
    tmp=0
    background_image = pygame.image.load("cover.png").convert()
    font = pygame.font.Font('freesansbold.ttf', 41)
    screen.blit(background_image, [0, 0])
    text=font.render("BACK", True, white)
    screen.blit(text, [580, 450])
    pos = pygame.mouse.get_pos()
    click_sound = pygame.mixer.Sound("mclick.ogg")
    xm = pos[0]
    ym = pos[1]
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            tmp=1
    if (tmp==1) and(xm>=580 and xm<=700 and ym>=450 and ym<=500):
            click_sound.play()
            return 0
    else:
            return a
                  
#chk func to keep track of mouse in menu
def chk_scr():
    click_sound = pygame.mixer.Sound("mclick.ogg") 
    pos = pygame.mouse.get_pos()
    xm = pos[0]
    ym = pos[1]
    if (xm>=248 and xm<=498 and ym>=191 and ym<=236):
        click_sound.play()
        return 1        
    elif(xm >=211 and xm<=491 and  ym>=241 and ym<=276):
        click_sound.play()
        return 2
    elif(xm>=238 and xm<=468 and ym>=291 and ym<=326) :
        click_sound.play()
        return 3
    elif(xm>=280 and xm<=420 and ym>=341 and ym<=376) :
        click_sound.play()
        return 4
    elif(xm>=306 and xm<=402 and ym>=391 and ym<=426) :
        return 11
    else:
        return 0    
# MENU text
def menu(screen):
    pygame.display.set_caption("BOUNCING SQUARE")
    font = pygame.font.Font('freesansbold.ttf', 41)
    background_image = pygame.image.load("cover.png").convert()
    screen.blit(background_image, [0, 0])
    text=font.render("Time Mode", True, white)
    cx = (700 // 2) - (text.get_width() // 2)
    cy = ( 500// 2) - (text.get_height() // 2)-50
    screen.blit(text, [cx, cy])
    text=font.render("Collision Mode", True, white)
    cx = (700 // 2) - (text.get_width() // 2)
    cy = ( 500// 2) - (text.get_height() // 2)
    screen.blit(text, [cx, cy])
    text=font.render("How To Play", True, white)
    cx = (700 // 2) - (text.get_width() // 2)
    cy = ( 500// 2) - (text.get_height() // 2)+50
    screen.blit(text, [cx, cy])
    text=font.render("Credits", True, white)
    cx = (700 // 2) - (text.get_width() // 2)
    cy = ( 500// 2) - (text.get_height() // 2)+100
    screen.blit(text, [cx, cy])
    text=font.render("Quit", True, white)
    cx = (700 // 2) - (text.get_width() // 2)
    cy = ( 500// 2) - (text.get_height() // 2)+150
    screen.blit(text, [cx, cy])
def  main():
        pygame.init()
        # Set the height and width of the screen
        size=[700,500]
        screen=pygame.display.set_mode(size)
        pygame.display.set_caption("BOUNCING SQUARE")
        #Loop until the user clicks the close button.
        done=False
        # Used to manage how fast the screen updates
        clock=pygame.time.Clock()
        # This is a font we use to draw text on the screen (size 36)
        font = pygame.font.Font('freesansbold.ttf', 56)
        display_instructions = True
        instruction_page = 0
        show=0
        # Set the screen background
        background_image = pygame.image.load("cover.png").convert()
        screen.blit(background_image, [0, 0])
        while not done :
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop
                if event.type==pygame.MOUSEBUTTONDOWN and instruction_page==0:
                        instruction_page=chk_scr()
                if instruction_page==11:
                            done=True                       
            # --- Game logic should go here
            if instruction_page==0:
                menu(screen)
            if instruction_page == 1:
                screen.fill(black) 
                time_mode(screen)
                instruction_page=0
                menu(screen)
                instruction_page =0
            if instruction_page == 2:
                screen.fill(black)
                colmode(screen)
                instruction_page=0
                menu(screen)
                instruction_page=0
            if instruction_page == 3:
                 instruction_page=back(screen,3)
                 htp(screen)     
            if instruction_page == 4:
                instruction_page=back(screen,4)
                credit(screen)        
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()         
            # --- Limit to 60 frames per second
            clock.tick(60)
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit()
if __name__ == "__main__":
    main()
