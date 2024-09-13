import bornyearforewer
import bornday

if bornyearforewer.checkBornYearForewer():
    result = False
    while result != True:
        if bornday.checkBornDay():
            result = True
            print('Правильно!')

#BornYear 1799
#BornDay 6 June