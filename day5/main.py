
c1 =[]
c2 = []
c3 = []

with open('./testdata.txt') as data_file:
    lines = data_file.readlines()
    data = [entry.strip() for entry in lines]

    #print(f"{lines}\n")

    for index, value in enumerate(data):
        print(value)
        if value.find9:
            print(value.index("1   2   3"))