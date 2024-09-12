import bornyear

def checkBornYearForewer():
    result = False
    while result != True:
        if bornyear.checkBornYear():
            result = True
            return True   
        
#BornYear 1799
        
# if checkBornYearForewer():
#     print('Success')