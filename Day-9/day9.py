def evalMove(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    ddx, ddy = tail

    if (abs(dx) == 2) and (abs(dy) == 2):
        tail[0] += dx//2
        tail[1] += dy//2
    else:
        if abs(dx) == 2:
            tail[0] += dx//2
            tail[1] = head[1]
        elif abs(dy) == 2:
            tail[1] += dy//2
            tail[0] = head[0]

    new_x, new_y = tail
    return ((new_x != ddx) or (new_y != ddy))

def solveInput(rope, steps):
    visited = set()
    tail = rope[-1]
    head = rope[0]
    visited.add(str(tail))

    for step in steps:
        dir, dst = step.split()

        for _ in range(int(dst)):
            if dir == 'U':
                head[1] += 1
            elif dir == 'D':
                head[1] -= 1
            elif dir == 'R':
                head[0] += 1
            else:
                head[0] -= 1

            motion = True

            for n in range(1, len(rope)):
                if motion:
                    motion = evalMove(rope[n-1], rope[n])

            if motion:
                visited.add(str(rope[-1]))

    return len(visited)

file = open("Day-9/input.txt", "r")
steps = [line.strip() for line in file.readlines()]
file.close()

ropeOne = [[0, 0], [0, 0]]
ropeTwo = [[0, 0] for _ in range(10)]

print("Solution to part 1: ", solveInput(ropeOne, steps))
print("Solution to part 2: ", solveInput(ropeTwo, steps))