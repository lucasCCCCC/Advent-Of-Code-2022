gameOutcomeScores1 = {
    "X - A": 4, 
    "Y - B": 5, 
    "Z - C": 6, 
    "X - B": 1, 
    "X - C": 7, 
    "Y - A": 8, 
    "Y - C": 2, 
    "Z - A": 3, 
    "Z - B": 9
}

gameOutcomeScores2 = {
    "X - A": 3, 
    "Y - B": 5, 
    "Z - C": 7, 
    "X - B": 1, 
    "X - C": 2, 
    "Y - A": 4, 
    "Y - C": 6, 
    "Z - A": 8, 
    "Z - B": 9
}

scorePartA = 0
scorePartB = 0
file = open("Day-2/test.txt", "r")

for line in file:
    curr = line.split(" ")
    play = curr[1].strip() + " - " + curr[0].strip()
    scorePartA += gameOutcomeScores1.get(play)
    scorePartB += gameOutcomeScores2.get(play)

file.close()

print("Solution to part 1: ", scorePartA) 
print("Solution to part 2: ", scorePartB)