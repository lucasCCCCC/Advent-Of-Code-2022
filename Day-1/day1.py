file = open("Day-1/input.txt", "r")

elveCalories = file.read().strip().split("\n\n")

calories = []

for calorie in elveCalories:
    items = calorie.split("\n")
    items = [eval(item) for item in items]
    calories.append(sum(items))

file.close()

calories = sorted(calories, reverse = True)
top3Calories = calories[0] + calories[1] + calories[2]

print("Solution to part 1: ", max(calories)) 
print("Solution to part 2: ", top3Calories)
