def giveMeTuples(*lists):
    commonIndex = 0
    listOfTuples = []
    listForATouple = []
    numberOfLists = len(lists)
    while True:
        for list in lists:
            for index in range(0,len(list)):
                if index == commonIndex:
                    listForATouple.append(list[index])
        commonIndex += 1
        listOfTuples.append(tuple(listForATouple))
        listForATouple.clear()
        if commonIndex == numberOfLists:
            break
    return listOfTuples
                


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = ["a", "b", "c"]

print(giveMeTuples(l1, l2, l3))