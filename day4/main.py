#https://adventofcode.com/2022/day/4#part2
overlapCount = 0
alreadyChecked = False


def problemOne():
    print(f"Comparing: {compareOne[0]}-{compareOne[1]} and {compareTwo[0]}-{compareTwo[1]}")
    if int(compareOne[0]) >= int(compareTwo[0]) and int(compareOne[1]) <= int(compareTwo[1]):
        overlapCount +=1
        alreadyChecked = True
        print(f"Overlap Count Check 1: {overlapCount}")
    if int(compareTwo[0]) >= int(compareOne[0]) and int(compareTwo[1]) <= int(compareOne[1]) and alreadyChecked == False:
        overlapCount +=1
        print(f"Overlap Count Check 2: {overlapCount}")
    alreadyChecked = False


with open('./data.txt') as data_file:
    lines = data_file.readlines()
    data = [entry.strip().split(',') for entry in lines]

    #print(f"{data}")
    for entry in data:
        compareOne = entry[0].split('-')
        listOne = list(range(int(compareOne[0]),int(compareOne[1])+1))
        compareTwo = entry[1].split('-')
        listTwo = list(range(int(compareTwo[0]),int(compareTwo[1])+1))
        print(f"Comparing:\n{listOne}\n{listTwo}")
        for x in listOne:
            if (x in listTwo):
                print("Match Found")
                overlapCount+=1
                break
        #print(f"First number: {compareOne}\nSecond number: {compareTwo}")
        #print(f"Comparing: {entry[0][0]} and {entry[1][0]}")
    print(f"Overlap Count: {overlapCount}")            