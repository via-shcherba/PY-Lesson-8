
def checkBornYear():
    bornYear = 1799
    inputYear = int(input('Введите год рождения: '))
    if inputYear == bornYear:
        return True
    else:
        return False
    
#BornYear 1799

# if checkBornYear():
#     print('Success')
# else:
#     print('Born Year is wrong')