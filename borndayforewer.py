from bornday import checkBornDay
from bornyearforewer import checkBornYearForewer

if checkBornYearForewer():
    result = False
    while result != True:
        if checkBornDay():
            result = True
            print('Правильно!')

#BornYear 1799
#BornDay 6 Июня