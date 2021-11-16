from pygame.draw import line


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,100,255)
orange = (255, 165, 0)

def physicsfunc(phy_marks, phy_colour):
    number_of_items = len(phy_colour)
    #IMPORTING PYGAME
    import pygame
    import random

    #MAKES IT EASY TO TRACK KEYS PRESSED
    from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        K_SPACE,
        K_r
    )

    #**********************************************************************************************************************************#
    pygame.font.init()

    #OTHER VARIABLES
    # Window size
    width = number_of_items*100
    length = 750
    #DEFINING FONTS TO DISPLAY TEXT
    font = pygame.font.SysFont('times new roman', 20)

    #DISPLAYING WINDOW
    screen = pygame.display.set_mode((width, length))
    pygame.display.set_caption('Physics marks sort')

    #USED TO DISPLAY TEXT ON THE SCREEN
    def display_message():
        #TEXT MESSAGE
        txt = font.render('"SPACE" TO SORT', 1, white)
        #POSITION OF TEXT
        screen.blit(txt, (width//2-50, 20))
        txt = font.render('ALGORITHM USED: "BUBBLE SORT"', 1, white)
        screen.blit(txt, (width//2-150, 50))

    colours = [orange, red, green, blue]

    #FUNCTION TO DISPLAY THE BARS ON THE SCREEN
    def display_bars(number_of_items=number_of_items):
        screen.fill(black)
        display_message()
        #DETERMINES THE WIDTH OF EACH BAR
        width_of_bar =(width-100)//100
        #GIVES UNIFORM DISTANCE OF 900 / 50 UNITS BEHIND EACH BAR, 900 WAS CHOSEN BECAUSE IT IS THE LENGTH OF THE SCREEN
        distance_of_each_bar = 900 / 50
        #DETERMINES THE LENTH TILL WHERE THE BAR WILL REACH
        boundry_of_bars = 500 / 100
        # Drawing the array values as lines
        for i in range(number_of_items):
            pygame.draw.line(screen, phy_colour[i], (distance_of_each_bar * i, 100), (distance_of_each_bar * i, phy_marks[i]*boundry_of_bars + 100), width_of_bar)

    #AFTER COMPARING TWO LINES THIS IS USED
    def refresh():
        display_bars()
        pygame.time.delay(2)
        pygame.display.update()

    def sort():
        for i in range(len(phy_marks)-1):
            for elem_height in range(len(phy_marks) - i - 1):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()

                #COLOUR CHANGES TO RED WHILE COMPARING
                phy_colour[elem_height] = colours[1]
                phy_colour[elem_height+1] = colours[1]
                pygame.time.delay(25)

                #IF THE ELEMENT ON THE LEFT ON THE LEFT IS GREATER IT GETS SWITCHED TO THE RIGHT
                if phy_marks[elem_height] > phy_marks[elem_height + 1]:
                    
                    #COLOUR CHANGES TO GREEN WHILE SWITCHING
                    phy_colour[elem_height] = colours[2]
                    phy_colour[elem_height+1] = colours[2]
                    #USING TEMPORARY VARIABLE WE STORE THE HEIGHT AND LATER SWITCH IT
                    temp_height = phy_marks[elem_height]
                    phy_marks[elem_height] = phy_marks[elem_height + 1]
                    phy_marks[elem_height + 1] = temp_height
                    refresh()

                #COLOURS SET TO ORANGE INDICATING THEY HAVE BEEN TRAVERSED THROUGH
                phy_colour[elem_height] = colours[0]
                phy_colour[elem_height+1] = colours[0]

        for i in range(len(phy_marks)):
            phy_colour[i] = colours[-1]
            
    def main():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # elif 
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        sort()
                
                    elif event.key == K_ESCAPE:
                        running = False

            display_bars()
            pygame.display.update()

        pygame.quit()
    main()

def chemfunc(chem_marks, chem_colour):

    number_of_items = len(chem_colour)
    #IMPORTING PYGAME
    import pygame

    #MAKES IT EASY TO TRACK KEYS PRESSED
    from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        K_SPACE,
        K_r
    )

    #**********************************************************************************************************************************#
    pygame.font.init()

    #OTHER VARIABLES
    # Window size
    width = number_of_items*100
    length = 750
    #DEFINING FONTS TO DISPLAY TEXT
    font = pygame.font.SysFont('times new roman', 20)

    #DISPLAYING WINDOW
    screen = pygame.display.set_mode((width, length))
    pygame.display.set_caption('CHem marks sort')

    #USED TO DISPLAY TEXT ON THE SCREEN
    def display_message():
        #TEXT MESSAGE
        txt = font.render('"SPACE" TO SORT', 1, white)
        #POSITION OF TEXT
        screen.blit(txt, (width//2-50, 20))
        txt = font.render('ALGORITHM USED: "BUBBLE SORT"', 1, white)
        screen.blit(txt, (width//2-150, 50))

    colours = [orange, red, green, blue]

    #FUNCTION TO DISPLAY THE BARS ON THE SCREEN
    def display_bars(number_of_items=number_of_items):
        screen.fill(black)
        display_message()
        #DETERMINES THE WIDTH OF EACH BAR
        width_of_bar =(width-100)//100
        #GIVES UNIFORM DISTANCE OF 900 / 50 UNITS BEHIND EACH BAR, 900 WAS CHOSEN BECAUSE IT IS THE LENGTH OF THE SCREEN
        distance_of_each_bar = 900 / 50
        #DETERMINES THE LENTH TILL WHERE THE BAR WILL REACH
        boundry_of_bars = 500 / 100
        # Drawing the array values as lines
        for i in range(number_of_items):
            pygame.draw.line(screen, chem_colour[i], (distance_of_each_bar * i, 100), (distance_of_each_bar * i, chem_marks[i]*boundry_of_bars + 100), width_of_bar)

    #AFTER COMPARING TWO LINES THIS IS USED
    def refresh():
        display_bars()
        pygame.time.delay(2)
        pygame.display.update()

    def sort():
        for i in range(len(chem_marks)-1):
            for elem_height in range(len(chem_marks) - i - 1):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()

                #COLOUR CHANGES TO RED WHILE COMPARING
                chem_colour[elem_height] = colours[1]
                chem_colour[elem_height+1] = colours[1]
                pygame.time.delay(25)

                #IF THE ELEMENT ON THE LEFT ON THE LEFT IS GREATER IT GETS SWITCHED TO THE RIGHT
                if chem_marks[elem_height] > chem_marks[elem_height + 1]:
                    
                    #COLOUR CHANGES TO GREEN WHILE SWITCHING
                    chem_colour[elem_height] = colours[2]
                    chem_colour[elem_height+1] = colours[2]
                    #USING TEMPORARY VARIABLE WE STORE THE HEIGHT AND LATER SWITCH IT
                    temp_height = chem_marks[elem_height]
                    chem_marks[elem_height] = chem_marks[elem_height + 1]
                    chem_marks[elem_height + 1] = temp_height
                    refresh()

                #COLOURS SET TO ORANGE INDICATING THEY HAVE BEEN TRAVERSED THROUGH
                chem_colour[elem_height] = colours[0]
                chem_colour[elem_height+1] = colours[0]

        for i in range(len(chem_marks)):
            chem_colour[i] = colours[-1]
            
    def main():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        sort()
                
                    elif event.key == K_ESCAPE:
                        running = False

            display_bars()
            pygame.display.update()

        pygame.quit()
    main()

def mathfunc(math_marks, math_colour):
    number_of_items = len(math_colour)
    #IMPORTING PYGAME
    import pygame
    #MAKES IT EASY TO TRACK KEYS PRESSED
    from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        K_SPACE,
        K_r
    )

    #**********************************************************************************************************************************#
    pygame.font.init()

    #OTHER VARIABLES
    # Window size
    width = number_of_items*100
    length = 700
    #DEFINING FONTS TO DISPLAY TEXT
    font = pygame.font.SysFont('times new roman', 20)

    #DISPLAYING WINDOW
    screen = pygame.display.set_mode((width, length))
    pygame.display.set_caption('Math marks sort')

    #USED TO DISPLAY TEXT ON THE SCREEN
    def display_message():
        #TEXT MESSAGE
        txt = font.render('"SPACE" TO SORT', 1, white)
        #POSITION OF TEXT
        screen.blit(txt, (width//2-50, 20))
        txt = font.render('ALGORITHM USED: "BUBBLE SORT"', 1, white)
        screen.blit(txt, (width//2-150, 50))

    colours = [orange, red, green, blue]

    #FUNCTION TO DISPLAY THE BARS ON THE SCREEN
    def display_bars(number_of_items=number_of_items):
        screen.fill(black)
        display_message()
        #DETERMINES THE WIDTH OF EACH BAR
        width_of_bar =(width-100)//100
        #GIVES UNIFORM DISTANCE OF 900 / 50 UNITS BEHIND EACH BAR, 900 WAS CHOSEN BECAUSE IT IS THE LENGTH OF THE SCREEN
        distance_of_each_bar = 900 / 50
        #DETERMINES THE LENTH TILL WHERE THE BAR WILL REACH
        boundry_of_bars = 500 / 100
        # Drawing the array values as lines
        for i in range(number_of_items):
            pygame.draw.line(screen, math_colour[i], (distance_of_each_bar * i, 100), (distance_of_each_bar * i, math_marks[i]*boundry_of_bars + 100), width_of_bar)

    #AFTER COMPARING TWO LINES THIS IS USED
    def refresh():
        display_bars()
        pygame.time.delay(2)
        pygame.display.update()

    def sort():
        for i in range(len(math_marks)-1):
            for elem_height in range(len(math_marks) - i - 1):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()

                #COLOUR CHANGES TO RED WHILE COMPARING
                math_colour[elem_height] = colours[1]
                math_colour[elem_height+1] = colours[1]
                pygame.time.delay(25)

                #IF THE ELEMENT ON THE LEFT ON THE LEFT IS GREATER IT GETS SWITCHED TO THE RIGHT
                if math_marks[elem_height] > math_marks[elem_height + 1]:
                    
                    #COLOUR CHANGES TO GREEN WHILE SWITCHING
                    math_colour[elem_height] = colours[2]
                    math_colour[elem_height+1] = colours[2]
                    #USING TEMPORARY VARIABLE WE STORE THE HEIGHT AND LATER SWITCH IT
                    temp_height = math_marks[elem_height]
                    math_marks[elem_height] = math_marks[elem_height + 1]
                    math_marks[elem_height + 1] = temp_height
                    refresh()

                #COLOURS SET TO ORANGE INDICATING THEY HAVE BEEN TRAVERSED THROUGH
                math_colour[elem_height] = colours[0]
                math_colour[elem_height+1] = colours[0]

        for i in range(len(math_marks)):
            math_colour[i] = colours[-1]
            
    def main():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        sort()
                
                    elif event.key == K_ESCAPE:
                        running = False

            display_bars()
            pygame.display.update()

        pygame.quit()
    main()
