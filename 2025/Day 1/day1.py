# https://adventofcode.com/2025/day/1

with open("input.txt", "r") as input:
    start = 50
    res = 0
    for data in input:

        if data[0] == "R":
            start += int(data[1:])
        else:
            start -= int(data[1:])

        if start == 0 or start % 100 == 0:
            res += 1
    print(res)
