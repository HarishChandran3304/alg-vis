white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,100,255)
orange = (255, 165, 0)
ended = False

def bubblesort(marks_info, colour):
    marks = list(marks_info.keys())
    number_of_items = len(colour)
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
    pygame.display.set_caption('Bubble sort')

    #USED TO DISPLAY TEXT ON THE SCREEN
    def display_message():
        global ended
        #TEXT MESSAGE
        txt = font.render('"SPACE" TO SORT', 1, white)
        #POSITION OF TEXT
        screen.blit(txt, (width//2-50, 20))
        txt = font.render('ALGORITHM USED: "BUBBLE SORT"', 1, white)
        screen.blit(txt, (width//2-150, 50))
        if ended == True:
            marks_in_order = marks
            marks_in_order.sort()
            txt = font.render(marks_info[marks_in_order[-1]]+ ' got '+ str(marks_in_order[-1]), 1, white)
            #POSITION OF TEXT
            screen.blit(txt, (width//2-50, 70))

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
            pygame.draw.line(screen, colour[i], (distance_of_each_bar * i, 100), (distance_of_each_bar * i, marks[i]*boundry_of_bars + 100), width_of_bar)

    #AFTER COMPARING TWO LINES THIS IS USED
    def refresh():
        display_bars()
        pygame.time.delay(2)
        pygame.display.update()

    def sort():
        global ended
        for i in range(len(marks)-1):
            for elem_marks in range(len(marks) - i - 1):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()

                #COLOUR CHANGES TO RED WHILE COMPARING
                colour[elem_marks] = colours[1]
                colour[elem_marks+1] = colours[1]
                pygame.time.delay(25)

                #IF THE ELEMENT ON THE LEFT ON THE LEFT IS GREATER IT GETS SWITCHED TO THE RIGHT
                if marks[elem_marks] > marks[elem_marks + 1]:
                    
                    #COLOUR CHANGES TO GREEN WHILE SWITCHING
                    colour[elem_marks] = colours[2]
                    colour[elem_marks+1] = colours[2]
                    #USING TEMPORARY VARIABLE WE STORE THE marks AND LATER SWITCH IT
                    temp_marks = marks[elem_marks]
                    marks[elem_marks] = marks[elem_marks + 1]
                    marks[elem_marks + 1] = temp_marks
                    refresh()

                #COLOURS SET TO ORANGE INDICATING THEY HAVE BEEN TRAVERSED THROUGH
                colour[elem_marks] = colours[0]
                colour[elem_marks+1] = colours[0]
        ended = True
        '''txt = font.render(marks_info[marks_in_order[0]]+ 'got'+ str(marks_in_order[0]), 1, white)
        #POSITION OF TEXT
        screen.blit(txt, (width//2-50, 20))'''
            
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

def mergesort(marks_info, colour):
    marks = list(marks_info.keys())
    number_of_items = len(colour)
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
    pygame.display.set_caption('Merge sort')

    #USED TO DISPLAY TEXT ON THE SCREEN
    def display_message():
        global ended
        #TEXT MESSAGE
        txt = font.render('"SPACE" TO SORT', 1, white)
        #POSITION OF TEXT
        screen.blit(txt, (width//2-50, 20))
        txt = font.render('ALGORITHM USED: "MERGE SORT"', 1, white)
        screen.blit(txt, (width//2-150, 50))
        if ended == True:
            marks_in_order = marks
            marks_in_order.sort()
            txt = font.render(marks_info[marks_in_order[-1]]+ ' got '+ str(marks_in_order[-1]), 1, white)
            #POSITION OF TEXT
            screen.blit(txt, (width//2-50, 70))

    colours =[orange, red, green, blue]

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
            pygame.draw.line(screen, colour[i], (distance_of_each_bar * i, 100), (distance_of_each_bar * i, marks[i]*boundry_of_bars + 100), width_of_bar)

    #AFTER COMPARING TWO LINES THIS IS USED
    def refresh():
        screen.fill(black)
        display_message()
        display_bars()
        pygame.time.delay(25)
        pygame.display.update()

    def merge(marks, x1, y1, x2, y2):
        i = x1
        j = x2
        temp =[]
        pygame.event.pump()
        #RED SIGNIFIES THAT THE TWO BARS ARE BEING COMPARED
        #GREEN SIGNIFIES THAT THE BAR HAS JUST BEEN MOVED TO TEMPORARY CORRECT POSITION (RECENT)
        #ORANGE SIGNIFIES THAT THE BAR IS IN CORRECT PLACE (FOR CURRENT ITERATION)
        while i<= y1 and j<= y2:
            colour[i]= colours[1]
            colour[j]= colours[1]
            refresh()
            if marks[i] < marks[j]:
                #IF THE marks IS SMALLER COMPARED TO NEXT THEN IT IS ADDED TO A VARIABLE CALLED TEMP
                #TEMP STANDS FOR TEMPORARY
                temp.append(marks[i])
                i+= 1

            else:
                #IF THE ONE ON THE RIGHT WAS RIGHT WAS SMALLER THEN IT GETS ADDED TO THE VARIABLE TEMP
                temp.append(marks[j])
                j+= 1

        while i<= y1:
            colour[i]= colours[1]
            refresh()
            temp.append(marks[i])
            i+= 1

        while j<= y2:
            colour[j]= colours[1]
            refresh()
            temp.append(marks[j])
            j+= 1

        j = 0

        for i in range(x1, y2 + 1):
            pygame.event.pump()
            marks[i]= temp[j]
            j+= 1
            colour[i]= colours[2]
            refresh()
            if y2-x1 == len(marks)-2:
                colour[i]= colours[3]
            else:
                colour[i]= colours[0]

    #ALGORITHIM FOR MERGE SORT
    def algorithm(marks, l, r):
        global ended
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()

        mid =(l + r)//2

        if l<r:
            algorithm(marks, l, mid)
            algorithm(marks, mid + 1, r)
            merge(marks, l, mid, mid + 1, r)
            
        ended = True
    
    def main():
        running = True 
        # Infinite loop to keep the window open
        while running:
            # background
            screen.fill(black)
            #GETS ALL EVENTS LIKE WHICH KEY IS PRESSED
            for event in pygame.event.get():

                # If we click Close button in window
                if event.type == pygame.QUIT:
                    running = False

                #IF A KEY IS PRESSED 
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        algorithm(marks, 1, len(marks)-1)
                    #IF ESC KEY IS PRESSED IT QUITS THE PROGRAM
                    elif event.key == K_ESCAPE:
                        running = False
            display_message()
            display_bars()
            pygame.display.update()
            
        pygame.quit()
    main()
