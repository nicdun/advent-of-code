# PART 1
with open("./inputs/day4.txt", "r") as f:
    s = ""
    a = []
    w = [""] * 8
    result = 0

    for line in f:
        a.append(line.strip())

    # create padding to not run into array out of bounce
    # on each side 3 characters due to 'MAS'
    s = "Z" * (len(a[0]) + 2 * 3)
    for i in range(len(a)):
        a[i] = "ZZZ" + a[i] + "ZZZ"

    for i in range(3):
        a.insert(0, s)
        a.append(s)

    # processing through each row y and each column x
    # go through 'XMAS' in clock direction
    for y in range(len(a)):
        for x in range(len(a[y])):
            if a[y][x] == "X":
                w[0] = a[y][x : x + 4]
                w[1] = a[y][x] + a[y + 1][x + 1] + a[y + 2][x + 2] + a[y + 3][x + 3]
                w[2] = a[y][x] + a[y + 1][x] + a[y + 2][x] + a[y + 3][x]
                w[3] = a[y][x] + a[y + 1][x - 1] + a[y + 2][x - 2] + a[y + 3][x - 3]
                w[4] = a[y][x] + a[y][x - 1] + a[y][x - 2] + a[y][x - 3]
                w[5] = a[y][x] + a[y - 1][x - 1] + a[y - 2][x - 2] + a[y - 3][x - 3]
                w[6] = a[y][x] + a[y - 1][x] + a[y - 2][x] + a[y - 3][x]
                w[7] = a[y][x] + a[y - 1][x + 1] + a[y - 2][x + 2] + a[y - 3][x + 3]
                result += w.count("XMAS")

    print(result)

# PART 2
with open("./inputs/day4.txt", "r") as f:
    s = ""
    a = []
    w = []
    # S.S - M.M - M.S - S.M
    # .A. - .A. - .A. - .A.
    # M.M - S.S - M.S - S.M
    options = ["AMMSS", "ASSMM", "ASMMS", "AMSSM"]
    result = 0

    for line in f:
        a.append(line.strip())

    # create padding to not run into array out of bounce
    # on each side 1 characters due to X structure of 'MAS'
    s = "Z" * (len(a[0]) + 2)
    for i in range(len(a)):
        a[i] = "Z" + a[i] + "Z"

    a.insert(0, s)
    a.append(s)

    # processing through each row y and each column x
    # check each X values for possible 'MAS' options
    for y in range(len(a)):
        for x in range(len(a[y])):
            if a[y][x] == "A":
                w = (
                    a[y][x]
                    + a[y + 1][x + 1]
                    + a[y + 1][x - 1]
                    + a[y - 1][x - 1]
                    + a[y - 1][x + 1]
                )
                print(w)
                result += options.count(w)

    print(result)
