import random


def roll():
    return random.randint(1, 6) + random.randint(1, 6)


def show(field):
    for row in field:
        print(" ".join(f"{n:3}" for n in row))


def eval_group(values):
    if 0 in values:
        return 0

    counts = [values.count(n) for n in range(2, 13)]
    if 5 in counts:
        return 10
    elif 4 in counts:
        return 6
    elif 3 in counts:
        if 2 in counts:
            # Full house
            return 8
        else:
            # three
            return 3
    elif 2 in counts:
        return 3 if counts.count(2) > 1 else 1
    else:
        nums = sorted(values)
        if nums == list(range(nums[0], nums[0] + 5)):
            if 7 in nums:
                return 10
            else:
                return 12
        else:
            return 0


def evaluate(field):
    total = 0
    for idx, row in enumerate(field):
        val = eval_group(row)
        # print(f"Row {idx} has eval {val}")
        total += val

    for i in range(5):
        val = eval_group([row[i] for row in field])
        # print(f"Col {i} has eval {val}")
        total += val

    diag1 = eval_group([field[i][i] for i in range(5)])
    diag2 = eval_group([field[i][4-i] for i in range(5)])

    print("Diag 1:", diag1)
    print("Diag 2:", diag2)

    total += diag1 * 2
    total += diag2 * 2

    return total


def create_field():
    return [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]


if __name__ == "__main__":
    field = create_field()
    rolls = 0
    while rolls < 25:
        num = roll()

        show(field)
        print("Eval:", evaluate(field))
        print("ROLL:", num)

        while True:
            inp = input("Where? ")
            try:
                row, col = int(inp[0]), int(inp[1])
                if field[row][col] == 0:
                    field[row][col] = num
                    break
                else:
                    print("Nope - occupied!")
            except:
                pass

        rolls += 1
