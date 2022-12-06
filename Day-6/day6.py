file = open("Day-6/input.txt", "r")

dataStream = file.readline().strip()

def messageDetection(size, data):
    left = 0
    right = size

    while (right < len(data) + 1):

        curr = data[left:right]

        if len(curr) == len(set(curr)):
            break;

        left += 1
        right += 1

    return right

print("Solution to part 1: ", messageDetection(4, dataStream))
print("Solution to part 2: ", messageDetection(14, dataStream))
