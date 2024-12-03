def first_problem():
    with open('inputs/input_day1_a.txt') as f:
    #with open('inputs/day1a_test.txt') as f:
        lines = f.readlines()
        r1, r2 = [], []
        for line in lines:
            x, y = map(int, line.strip().split())
            r1.append(x)
            r2.append(y)

        r1, r2 = sorted(r1), sorted(r2)
        total = sum([abs(x - y) for x, y in zip(r1, r2)])
    print(f"Part 1: {total}")

def second_problem():
    with open('inputs/input_day1_a.txt') as f:
        lines = f.readlines()
        similarity_score = dict()
        r1, r2 = [], []
        for line in lines:
            x, y = map(int, line.strip().split())
            r1.append(x)
            r2.append(y)
        for x in r1:
            similarity_score[x] = 0
        for y in r2:
            if y in similarity_score:
                similarity_score[y] += 1

        total = sum([x * similarity_score[x] for x in similarity_score])
    print(f"Part 2: {total}")


if __name__ == '__main__':
    first_problem()
    second_problem()