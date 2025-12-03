# https://adventofcode.com/2025/day/2

with open("input.txt", "r") as input:
    res = 0
    content = input.readlines()
    for number in content:
        l, r = 0, 0
        number = number.strip()
        max_num = max([int(num) for num in number])
        max_idx = number.index(str(max_num))
        if max_idx + 1 == len(number):
            r = max_num
            l = max([int(num) for num in number[:max_idx]])
            res += int(str(l) + str(r))
        else:
            second_max_list = number[max_idx + 1 :]
            second_max_num = max([int(num) for num in second_max_list])
            l = str(max_num)
            r = str(second_max_num)
            combined = int(l + r)
            res += combined

    print(res)
