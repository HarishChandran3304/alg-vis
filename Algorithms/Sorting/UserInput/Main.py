choice = input('Enter choice (p, c or m) ').lower()

from csv import *

from pygame import PixelArray
from SortingAlgs import *
from sys import exit

temp = []
with open('StudentMarks.csv', 'r') as file:
    reader_object = reader(file)
    for row in reader_object:
        temp.append(row)
    content = []
    for x in temp:
        if x != []:
            content.append(x)
            number_of_items = len(content)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,100,255)
orange = (255, 165, 0)

names = [x[0] for x in content]
phy_marks = [int(x[1]) for x in content]
chem_marks = [int(x[2]) for x in content]
math_marks = [int(x[3]) for x in content]

phy_colour = [white]*number_of_items
chem_colour = [white]*number_of_items
math_colour = [white]*number_of_items

# while True:
if choice == 'p':physicsfunc(phy_marks, phy_colour)
elif choice == 'c':chemfunc(chem_marks, chem_colour)
elif choice == 'm': mathfunc(math_marks, math_colour)
elif choice == 'exit':exit()
    # else: print('Invalid input')


'''    if __name__ == '__main__':
        main()'''