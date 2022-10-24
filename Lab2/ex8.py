def divisionWithASCII(divisor, list, flag):
    listOfLists = []
    for string in list:
        miniList = []
        for character in string:
            if (ord(character) % divisor == 0) and (flag == True):
                miniList.append(character)
            elif (ord(character) % divisor != 0) and (flag == False):
                miniList.append(character)
        listOfLists.append(miniList)
    return listOfLists


print(divisionWithASCII(2, ["test", "hello", "lab002"], False))