import bornyear

def checkBornDay():
    bornDay = '6 June'
    inputDay = input('Enter born day: ')
    if inputDay == bornDay:
        return True
    else:
        return False
    
#BornDay 6 June

# if bornyear.checkBornYear():
#     if checkBornDay():
#         print('Success')
#     else:
#         print('Born Day is wrong')
# else:
#     print('Born Year is wrong')