from collections import defaultdict

partA = 0
partB = 0

fileContent = open("Day-7/input.txt").read().splitlines()

commands = map(str.split, fileContent)
paths = []
directories = defaultdict(int)

for command in commands:
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                paths.pop()
            else:
                paths.append(command[2])
    elif command[0] != "dir":
        for i in range(len(paths)):
            directories[tuple(paths[:i+1])] += int(command[0])

partA = sum(size for size in directories.values() if size <= 100000)

minSizeToDelete = 30000000 - (70000000 - directories[("/",)])

partB = min(size for size in directories.values() if size >= minSizeToDelete)

print("Solution to part 1: ", partA)
print("Solution to part 2: ", partB)
