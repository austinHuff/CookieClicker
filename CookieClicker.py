import pygame
import inputbox
import time

pygame.init()

# get highscores & save into dict
try:
    highscores = dict()
    with open('highscores.txt','r') as t:
        s = t.readlines()
    for i in s:
        L = i.split(' ')
        if L != ["\n"] and L != [""]:
            highscores[str(L[0])] = [int(L[1]),int(L[2]),int(str(L[3])[0:-1])]
except FileNotFoundError:
    # file not found, create blank highscores.txt file
    with open('highscores.txt','w') as t:
        t.write("")
# constants and global vars
display_width = 500
display_height = 500
C_WIDTH = 200
C_HEIGHT = 200
clickrate = 1
secondrate = 0
eaten = 0
cookieImg = pygame.image.load(r'C:\Users\Austin\Desktop\paint_images\cookieT.png')

# colors
black = (0,0,0)
white = (255,255,255)
grey = (200,200,200)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

# fonts
smallText = pygame.font.Font('freesansbold.ttf',15)
mediumText = pygame.font.Font('freesansbold.ttf',35)
largeText = pygame.font.Font('freesansbold.ttf',50)

# window and clock
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Cookie Clicker')
clock = pygame.time.Clock()

def boost_1():
    print('boost1')

def boost_2():
    print('boost2')

def boost_3():
    print('boost3')

def game_help():
    # displays game help message
    top = 100
    inc = 25
    count = 0
    bool_Help = True
    while bool_Help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("HELP MENU", largeText)
        TextRect.center = ((display_width/2),(75))
        gameDisplay.blit(TextSurf, TextRect)
        count = 1
        
        TextSurf, TextRect = text_objects("Click on the cookie to increase your score", smallText)
        TextRect.center = ((display_width/2),(top+count*inc))
        gameDisplay.blit(TextSurf, TextRect)
        count = 2
        
        name = max(highscores)
        if name.endswith('s'):
            msg = "Try to beat " + str(name) + "' highscore of " + str(highscores[max(highscores)][0])
        else:
            msg = "Try to beat " + str(name) + "'s highscore of " + str(highscores[max(highscores)][0])
        TextSurf, TextRect = text_objects(msg, smallText)
        TextRect.center = ((display_width/2),(top+count*inc))
        gameDisplay.blit(TextSurf, TextRect)
        count = 3
            
        TextSurf, TextRect = text_objects("You can buy boosts (currently in development).", smallText)
        TextRect.center = ((display_width/2),(top+count*inc))
        gameDisplay.blit(TextSurf, TextRect)
        count = 4
        
        TextSurf, TextRect = text_objects("BOOST1: (what is does)", smallText)
        TextRect.center = ((display_width/2),(top+count*inc))
        gameDisplay.blit(TextSurf, TextRect)
        count = 5
        
        TextSurf, TextRect = text_objects("BOOST2: (what it does)", smallText)
        TextRect.center = ((display_width/2),(top+count*inc))
        gameDisplay.blit(TextSurf, TextRect)
        count = 6
        
        TextSurf, TextRect = text_objects("BOOST3: (what it does)", smallText)
        TextRect.center = ((display_width/2),(top+count*inc))
        gameDisplay.blit(TextSurf, TextRect)
        count = 7
        
        button("Play",200,400,100,50,blue,bright_blue,game_loop)
        pygame.display.update()
        #time.sleep(3)
        #game_loop()
        clock.tick(15)

def cookie(x,y):
    gameDisplay.blit(cookieImg, (x,y))

def text_objects(text,font):
    textSurface = font.render(text,True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x < mouse[0] < x+w and y < mouse[1] < y+h:
        # mouse within boundaries of box
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        print(click)
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONUP or mouse[0] == 1: #MOUSEBUTTONUP - When any mouse button down
                print('up or down')
                action()
            
    else:
        # mouse not within boundaries of box
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    #put text on box
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = text_objects(msg,smallText)
    textRect.center = ((x+(w/2)), y+(h/2))
    gameDisplay.blit(textSurf, textRect)

def click_eat():
    global eaten
    global clickrate
    eaten += clickrate

def cookies_eaten(count):
    # displaying the number of cookies eaten
    font = pygame.font.SysFont(None,25)
    text = font.render("Cookies eaten: " + str(int(count)), True, black)
    gameDisplay.blit(text,(5,5))

def click_rate(rate):
    # displaying the cookies eaten per click 
    font = pygame.font.SysFont(None,25)
    text = font.render("Cookies per click: " + str(rate), True, black)
    gameDisplay.blit(text,(5,20))

def idle_rate(rate):
    # displaying the cookies eaten per sec idle
    font = pygame.font.SysFont(None,25)
    text = font.render("Cookies per sec: " + str(rate), True, black)
    gameDisplay.blit(text,(5,35))
    
def load_save():
    # load a saved game from dict
    global name
    global eaten
    global clickrate
    global secondrate
    
    try:
        eaten = highscores[name][0]
        clickrate = highscores[name][1]
        secondrate = highscores[name][2]
        print("i got the keys")
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("GAME LOADED", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(3)
        game_loop()
    except KeyError:
        print("no key")
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("NO SAVED GAME", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(3)
        game_intro()

def save_message():
    # displays game saved message
    gameDisplay.fill(white)
    TextSurf, TextRect = text_objects("GAME SAVED", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    game_intro()

def save_game():
    # save a game by putting vals into dict
    global name
    global eaten
    global clickrate 
    global secondrate
    print("saving")
    highscores[name] = [0,0,0]
    highscores[name][0] = int(eaten)
    highscores[name][1] = int(clickrate)
    highscores[name][2] = int(secondrate)

    save_message()
 
def quitgame():
    # save dict into textfile & kill
    print('quitting')
    with open('highscores.txt','w') as f:
        for i in highscores:
            f.write(str(i) + " " + str(highscores[i][0]) + " " + str(highscores[i][1]) + " " + str(highscores[i][2]) + '\n')
    pygame.quit()
    quit()

def game_intro():
    # pregame menu
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("Cookie Clicker", largeText)
        TextRect.center = ((display_width/2),(100))
        gameDisplay.blit(TextSurf, TextRect)
        cookie(((display_width-C_WIDTH)/2),((display_height-C_HEIGHT)/2))
        # buttons
        button("GO!",50,400,100,50,green,bright_green,game_loop)
        button("Load",200,400,100,50,blue,bright_blue,load_save)
        button("QUIT",350,400,100,50,red,bright_red,quitgame)
        # words
        TextSurf, TextRect = text_objects("Welcome " + name, mediumText)
        TextRect.center = ((display_width/2),(150))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)
        
def game_loop():
    global eaten
    
    print('game loop')
    #funtionality of the game
    cookiex = (display_width-C_WIDTH)/2
    cookiey = (display_height-C_HEIGHT)/2
    clockrate = 1000
    game_exit = False
    while not game_exit:

        # event checking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        
        # display items
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("Cookie Clicker", largeText)
        TextRect.center = ((display_width/2),(100))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects(name, smallText)
        TextRect.center = ((display_width/2),(130))
        gameDisplay.blit(TextSurf, TextRect)

        # action buttons
        button("SAVE",200,430,100,50,blue,bright_blue,save_game)
        button("HELP",50,430,100,50,green,bright_green,game_help)
        button("QUIT",350,430,100,50,red,bright_red,quitgame)
        # boost buttons
        button("BOOST1",50,350,100,50,green,bright_green,boost_1)
        button("BOOST2",200,350,100,50,blue,bright_blue,boost_2)
        button("BOOST3",350,350,100,50,red,bright_red,boost_3)
        # hidden button to see if cookie is clicked
        button("",cookiex+24,cookiey+30,C_WIDTH-48,C_HEIGHT-60, white, blue, click_eat)

        cookie(cookiex,cookiey)
        TextSurf, TextRect = text_objects("Boosts:", smallText)
        TextRect.center = ((display_width/2),(340))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Actions:", smallText)
        TextRect.center = ((display_width/2),(415))
        gameDisplay.blit(TextSurf, TextRect)

        #eaten = eaten + (secondrate/clockrate)
        eaten += secondrate/17 # this 17 is just an eyeball -- find a better way to add the rate every second
        cookies_eaten(eaten)
        click_rate(clickrate)
        idle_rate(secondrate)
        #print(eaten)
        pygame.display.update()
        clock.tick(clockrate) # number inside can be num clicks allowed per second?


name = 'asdf'#inputbox.ask(gameDisplay, 'Enter Username')
game_intro() #comment out to go straight into game loop
game_loop()
