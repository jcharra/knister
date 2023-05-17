import random


class Knister:
    def __init__(self):
        self.field = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

    def roll(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def show(self):
        for row in self.field:
            print(" ".join(f"{n:3}" for n in row))

    @staticmethod
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

    def evaluate(self):
        total = 0
        for idx, row in enumerate(self.field):
            val = self.eval_group(row)
            total += val

        for i in range(5):
            val = self.eval_group([row[i] for row in self.field])
            # print(f"Col {i} has eval {val}")
            total += val

        diag1 = self.eval_group([self.field[i][i] for i in range(5)])
        diag2 = self.eval_group([self.field[i][4-i] for i in range(5)])

        total += diag1 * 2
        total += diag2 * 2

        return total


if __name__ == "__main__":
    k = Knister()
    rolls = 0
    while rolls < 25:
        num = k.roll()

        k.show()
        print("Eval:", k.evaluate())
        print("ROLL:", num)

        while True:
            inp = input("Where? ")
            try:
                row, col = int(inp[0]), int(inp[1])
                if k.field[row][col] == 0:
                    k.field[row][col] = num
                    break
                else:
                    print("Nope - occupied!")
            except:
                pass

        rolls += 1

    print("Endstand:")
    k.show()
    print("PUNKTE:", k.evaluate())
