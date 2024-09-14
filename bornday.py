from bornyear import checkBornYear

def checkBornDay():
    bornDay = '6 Июня'
    inputDay = input('Введите день рождения: ')
    if inputDay == bornDay:
        return True
    else:
        return False
    
#BornDay 6 June

# if checkBornYear():
#     if checkBornDay():
#         print('Success')
#     else:
#         print('Born Day is wrong')
# else:
#     print('Born Year is wrong')