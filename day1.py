listA = []
listB = []

# PART 1
result_one = 0

with open("./inputs/day1.txt", "r") as f:
    for line in f:
        values = line.replace("\n", "").split("   ")
        listA.append(int(values[0]))
        listB.append(int(values[1]))

listA.sort()
listB.sort()

for index, entry in enumerate(listA):
    result_one += abs((entry) - listB[index])

print(result_one)

# PART 2
result_two = 0

for entry in listA:
    counter = 0
    for value in listB:
        if entry == value:
            counter += 1

    if counter != 0:
        result_two += entry * counter

print(result_two)
