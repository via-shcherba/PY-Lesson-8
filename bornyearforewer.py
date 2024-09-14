from bornday import checkBornYear

def checkBornYearForewer():
    result = False
    while result != True:
        if checkBornYear():
            result = True
            return True   
        
#BornYear 1799
        
# if checkBornYearForewer():
#    print('Success')