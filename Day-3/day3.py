def getPriority(duplicateChar):
    if duplicateChar.isupper():
        return ord(duplicateChar) - ord("A") + 27
    elif duplicateChar.islower():
        return ord(duplicateChar) - ord("a") + 1

def part1():

    sum = 0

    file = open("Day-3/input.txt")

    for line in file:

        contents = line.strip()
        firstHalf  = contents[:len(contents)//2]
        secondHalf = contents[len(contents)//2:]

        firstHalfChars = set(firstHalf)

        for secondChar in secondHalf:
            if secondChar in firstHalfChars:
                sum += getPriority(secondChar)
                break

    file.close()

    return sum;

def part2():

    sum = 0

    with open("Day-3/input.txt", 'r') as infile:
        it = iter(infile)
        while True:
            linesList = []
            try:
                for i in range(3):
                    linesList.append(next(it).strip())
            except StopIteration:
                if len(linesList) == 0:
                    break
            commonChar = set.intersection(*map(set, linesList))
            sum += getPriority(list(commonChar)[0])

    return sum

print("Solution to part 1: ", part1())
print("Solution to part 2: ", part2())