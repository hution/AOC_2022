
#https://adventofcode.com/2022/day/3#part2
priorities = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
sumPri = 0
index = 0

def findPriority(value):
    return priorities.index(value) + 1

def findMatch(a,b):
    matches = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                matches.append((i,j,b[j]))
    return matches

with open('./data.txt') as data_file:
    lines = data_file.readlines()
    data = [entry.strip() for entry in lines]

    #for x in range(0,len(data),3):
    #for index, value in enumerate(data):
        #divideAt = len(entry) / 2
    while index < len(data)-2:
        bagOne = data[index]
        bagTwo = data[index+1]
        bagThree = data[index+2]

        index +=3
        print(index)

        print(f"Bag One has: {bagOne}\nBag Two has: {bagTwo}\nBag Three has: {bagThree}")

        matchTwoResult = findMatch(bagOne,bagTwo)
        matchThreeResult = matchTwoResult[0][2] in bagThree
        if matchTwoResult:
            print(f"Double match found: {matchTwoResult}")
        if matchThreeResult == True:
            print(f"Three match. Found '{matchTwoResult[0][2]}'")
            sumPri += findPriority(matchTwoResult[0][2])
            print(f"SumPri is: {sumPri}")
        else:
            print("No triple match")
        
    print(f"Sum of the priority is {sumPri}")

