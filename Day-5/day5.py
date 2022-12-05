import string
import copy

def parseFile(cargo):
    cargoList = [[] for i in range(int(cargo[-1].strip()[-1]))]

    for line in cargo:
        for c in range(len(line)):
            if line[c] in string.ascii_uppercase:
                cargoList[c//4].append(line[c])

    return cargoList

file = open("Day-5/input.txt", "r")

cargo, cargoSteps = file.read().strip().split("\n\n")
cargo = parseFile(cargo.split("\n"))

copyOne = copy.deepcopy(cargo)
copyTwo = copy.deepcopy(cargo)

for cargoStep in cargoSteps.split("\n"):
    step = cargoStep.strip().split(" ")

    amountToMove = int(step[1])
    originalCrate = int(step[3])
    targetCrate = int(step[5])

    for i in range(amountToMove):
        elemToMove = copyOne[originalCrate - 1].pop(0)
        copyOne[targetCrate - 1].insert(0, elemToMove)

    for i in reversed(range(amountToMove)):
        elemToMove = copyTwo[originalCrate - 1].pop(i)
        copyTwo[targetCrate - 1].insert(0, elemToMove)

file.close()

partA = ""
partB = ""

for stack1, stack2 in zip(copyOne, copyTwo):
    partA += stack1[0]
    partB += stack2[0]

print("Solution to part 1: ", partA)
print("Solution to part 2: ", partB)