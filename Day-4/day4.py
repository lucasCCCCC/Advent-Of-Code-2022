partA = 0
partB = 0

file = open("Day-4/input.txt", "r")

for line in file:
    curr = line.strip().split(",")
    firstRange = curr[0].split("-") 
    secondRange = curr[1].split("-") 

    if ((int(firstRange[0]) <= int(secondRange[0]) and int(firstRange[1]) >= int(secondRange[1])) or 
        (int(firstRange[0]) >= int(secondRange[0]) and int(firstRange[1]) <= int(secondRange[1]))):
        partA +=1

    if ((int(firstRange[0]) <= int(secondRange[0]) <= int(firstRange[1])) or 
        (int(secondRange[0]) <= int(firstRange[0]) <= int(secondRange[1]))):
        partB +=1

file.close()

print("Solution to part 1: ", partA)
print("Solution to part 2: ", partB)