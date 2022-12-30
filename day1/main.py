with open("./data.txt") as data_file:
    lines = data_file.readlines()
    data = [entry.strip() for entry in lines]

    currentCal = 0
    mostCal = 0
    topCals = []
    for entry in data:
        if entry != "":
            currentCal = currentCal + int(entry)
        elif entry == '':
            topCals.append(currentCal)
            if currentCal > mostCal:
                mostCal = currentCal
                print(f"MostCal Now {mostCal}")
            currentCal = 0
    topCals.sort(reverse=True)
    print(f"Currentcal: {currentCal}\nMostCal: {mostCal}")
    print(f"{sum(topCals[:3])}")