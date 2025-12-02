# https://adventofcode.com/2025/day/2

with open("input.txt", "r") as input:
    range_list = input.read().split(",")
    invalid_ids = 0
    for data in range_list:
        l, r = data.split("-")
        for val in range(int(l), int(r) + 1):
            val_str = str(val)
            if len(val_str) % 2 == 0:
                middle = len(val_str) / 2
                first_half = val_str[: int(middle)]
                second_half = val_str[int(middle) :]
                if first_half == second_half:
                    invalid_ids += val

    print(invalid_ids)
