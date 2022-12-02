def main1():
    f = open("input.txt", "r");
    count = 0
    currCalories = 0
    maxCalories = 0
    
    while True:
        line = f.readline()

        line = line if len(line) == 1 else line.strip()

        if not line:
            maxCalories = compareCalories(maxCalories,currCalories)
            break

        if line == '\n':
            maxCalories = compareCalories(maxCalories,currCalories)
            currCalories = 0
        else:
         currCalories += int(line)    

    print(maxCalories)        


def main2():
    f = open("input.txt", "r");
    scores = []
    total = 0
    currCalories = 0

    while True:

        line = f.readline()
        line = line if len(line) == 1 else line.strip()

        if not line:
            scores.append(currCalories)
            break

        if line == '\n':
            scores.append(currCalories)
            currCalories = 0
        else:
         currCalories += int(line)  

    highScores = sorted(scores,reverse=True)[:3]

    for i in highScores:
        total += int(i)

    print(total)
    

if __name__ == "__main__":
    #main1() #Part 1
    main2() #Part 2

def compareCalories(max, current):
    return(current if int(current) > int(max) else max) 


