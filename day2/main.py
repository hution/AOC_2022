win = 6
draw = 3
loss = 0
idealScore = 0
scissors_Z = 3
rock_X = 1 
paper_Y = 2

with open('./day2/data.txt') as data_file:
    lines = data_file.readlines()
    data = [entry.strip().split(' ') for entry in lines]
    #print(f"{data}")

    for count, entry in enumerate(data):
        #print(count, entry)
        for i in range(0,1):
            match entry[i]:
                case "A": # Rock Case
                    if entry[i+1] == "Y": #Must Draw - Rock
                        idealScore += draw + rock_X
                    elif entry[i+1] =="X": #Must Lose - Scissors
                        idealScore += loss + scissors_Z
                    else: # Must Win - Paper
                        idealScore += win + paper_Y
                case "B": #Paper Case
                    if entry[i+1] == "Y":#Must Draw - Paper
                        #Draw State
                        idealScore += draw + paper_Y
                    elif entry[i+1] =="X": # Must Lose - Rock
                        #Loss state
                        idealScore += loss + rock_X
                    else: # Must Win - Scissors
                        idealScore += win + scissors_Z
                case "C": # Scissor Case
                    if entry[i+1] == "Y": #Must Draw - Scissors
                        idealScore += draw + scissors_Z
                    elif entry[i+1] =="X": #Must Lose - Paper
                        idealScore += loss + paper_Y
                    else: # Must Win - rock
                        idealScore += win + rock_X
        print(f"Round {count+1} score is {idealScore}")

    print(f"Ideal Score: {idealScore}")    


#A is rock 
#B is paper
#C is scissors
#X is rock - 1 point
#Y is paper - 2 points
#Z is scissors - 3 points
