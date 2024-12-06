# PART 1
result_one = 0


def is_save(arr):
    distances = [arr[i] - arr[i + 1] for i in range(len(arr) - 1)]
    if all(abs(el) in [1, 2, 3] for el in distances):
        if all(el > 0 for el in distances) or all(el < 0 for el in distances):
            return True
    return False


with open("./inputs/day2.txt", "r") as f:
    for line in f:
        values = list(map(int, line.strip().split()))
        if is_save(values):
            result_one += 1

print(result_one)

# PART 2
result_two = 0


def is_save_with_one_out(arr):
    if is_save(arr):
        return True

    for i in range(len(arr)):
        arr_minus_one = arr[:i] + arr[i + 1 :]
        if is_save(arr_minus_one):
            return True

    return False


with open("./inputs/day2.txt", "r") as f:
    for line in f:
        values = list(map(int, line.strip().split()))
        if is_save_with_one_out(values):
            result_two += 1


print(result_two)
