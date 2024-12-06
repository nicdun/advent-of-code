# PART 1
def get_next_mul(i):
    xy = ["", ""]
    p = 0
    plus = 0
    separator = ","
    result = 0
    for index in range(len(i)):
        val = i[index]
        plus = index
        if val.isdigit():
            xy[p] += val
        elif val == separator and len(xy[0]) == 0:
            break
        elif val == separator:
            if p == 1:
                break
            p = 1
        elif val == ")" and len(xy[1]) == 0:
            break
        elif val == ")" and len(xy[1]) > 0:
            result = int(xy[0]) * int(xy[1])
            break
        else:
            break
    i = i[plus:]
    return i, result


result_one = 0
with open("./inputs/day3.txt", "r") as f:
    i = f.read().strip()
    while True:
        search_string = "mul("
        search_string_length = len("mul(")
        a = i.find(search_string)
        i = i[(a + search_string_length) :]

        if a == -1:
            break

        result = get_next_mul(i)
        i = result[0]
        result_one += result[1]


print(result_one)

# PART 2
result_two = 0
with open("./inputs/day3.txt", "r") as f:
    i = f.read().strip()

    while True:
        mul_string = "mul("
        mul = i.find("mul(")
        dont = i.find("don't()")
        do = i.find("do()")

        if dont < mul and dont < do:
            i = i[do:]
        elif dont == do == mul == -1:
            break
        else:
            i = i[mul:]

        x = 0
        y = 0
        z = ["", ""]
        p = 0
        j = 4
        separator = ","

        while True:
            if i[j].isdigit():
                z[p] += i[j]
                j += 1
            elif i[j] == separator and p == 0:
                p = 1
                j += 1
            elif i[j] == ")" and p == 1:
                x = int(z[0])
                y = int(z[1])
                j += 1
                break
            else:
                break

        i = i[j:]
        result_two += x * y

print(result_two)
