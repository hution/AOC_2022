c1, c2, c3, c4 = "","","",""
uniqueCount = 0

testVars = []

with open('./testdata.txt') as data_file:
    lines = data_file.readlines()
    data = [entry.strip() for entry in lines]
    textData = data[0]

    for index, value in enumerate(textData):
        print(f"Index is: {index} and Value is: {value}")
        if index < 4:
            match index:
                case 0:
                    c1 = value
                    testVars.append(value)
                case 1:
                    c2 = value
                    testVars.append(value)
                case 2:
                    c3 = value
                    testVars.append(value)
                case 3:
                    c4 = value
                    testVars.append(value)
        elif value in testVars:
            print("Not unique")
            print(f"{testVars}")
            testVars.append(value)
            testVars.pop(0)
            print(f"{testVars}")
        else:
            if uniqueCount == 3:
                print(f"Unique set found at {index-1}")
                break
            else:
                uniqueCount += 1
                
