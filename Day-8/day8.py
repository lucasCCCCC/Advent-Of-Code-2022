matrix = []
lines = []
partA = 0
partB = 0

with open("Day-8/input.txt") as file:
    for line in file:
        matrix.append([int(num) for num in line.strip()])

for x, row in enumerate(matrix):
    for y, col in enumerate(row):
        score = 1
        visibleTree = False
        lines = [row[:y][::-1], row[y + 1 :], [r[y] for r in matrix[:x]][::-1], [r[y] for r in matrix[x + 1 :]],]

        for line in lines:
            for distance, j in enumerate(line, 1):
                if j >= col:
                    score *= distance
                    break
            else:
                visibleTree = True
                score *= max(1, len(line))

        partA += int(visibleTree)
        partB = max(partB, score)
        
print("Solution to part 1: ", partA)
print("Solution to part 2: ", partB)