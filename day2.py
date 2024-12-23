
def first_part():
    with open('inputs/input_day2.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            levels = list(map(int, line.strip().split()))
            diff = [levels[i+1]-x for i, x in enumerate(levels[:-1])]
            total += all([1<=x<=3 for x in diff]) or all([1<=-x<=3 for x in diff])
    print(f"Part 1: {total}")

def valid_increasing(levels):
    slack = 1
    x = levels[0]
    for i, _ in enumerate(levels[:-1]):
        if levels[i+1]-x<1 or levels[i+1] - x>3:
            if slack>0:
                slack -= 1
            else:
                return False
        else:
            x = levels[i+1] 
    return True

def second_part():
    with open('inputs/input_day2.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            levels = list(map(int, line.strip().split()))
            if valid_increasing(levels) or valid_increasing(levels[::-1]):
                total += 1
            elif valid_increasing([-l for l in levels]) or valid_increasing([-l for l in levels[::-1]]):
                total += 1
    print(f"Part 2: {total}")

if __name__ == '__main__':
    first_part()
    second_part()