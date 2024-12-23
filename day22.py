from functools import lru_cache

def read_input():
    r = []
    with open("inputs/input_22.txt") as f:
        for line in f.readlines():
            r.append(int(line.strip()))
    return r

def one_step(sn):
    sn1 = sn*64
    sn ^= sn1
    sn %= 16777216
    sn1 = sn//32
    sn ^= sn1
    sn %= 16777216
    sn1 = sn*2048
    sn ^= sn1
    sn %= 16777216
    return sn

def part1():
    numbers = read_input()
    total = 0
    for number in numbers:
        x = number
        for i in range(2000):
            x = one_step(x)
        total += x
    return total
    
def get_prices_and_diffs():
    numbers = read_input()
    prices = []
    for number in numbers:
        x = number
        price_list = []
        for i in range(2000):
            price_list.append(x%10)
            x = one_step(x)
        price_list.append(x%10)
        prices.append(price_list)

    diffs = []
    diff_patterns = []
    for pl in prices:
        diff_list = [pl[i+1]-p for i, p in enumerate(pl[:-1])]
        diff_p_map = dict()
        for i, d in enumerate(diff_list[:-3]):
            key = get_key(diff_list[i:i+4])
            if key not in diff_p_map:
                diff_p_map[key] = i+4
        diff_patterns.append(diff_p_map)
        diffs.append(diff_list)

    return prices, diffs, diff_patterns

def calculate_for_pattern(prices, diff_patterns, pattern):
    total = 0
    key = get_key(pattern)
    for i, p in enumerate(prices):
        if key in diff_patterns[i]:
            index = diff_patterns[i][key]
            total += p[index]
    return total

def get_diff_pattern(key):
    diff_pattern = []
    while key > 0:
        diff = (key % 20) - 10
        diff_pattern.insert(0, diff)  # Insert at beginning to maintain order
        key //= 20
    return diff_pattern if diff_pattern else [0]  # Return [0] for key=0 case

def get_key(diff_pattern):
    x = 0
    for i, d in enumerate(diff_pattern):
        if i!=0:
            x *= 20
        x += (d+10)
    return x

def part2():
    prices, diffs, diff_patterns = get_prices_and_diffs()
    max_total, max_pattern = 0, []
    all_patterns = set([p for dfm in diff_patterns for p in dfm.keys()])
    for i, key in enumerate(all_patterns):
        diff_pattern = get_diff_pattern(key)
        if sum(diff_pattern) <0 or diff_pattern[-1]<0:
            continue
        total = calculate_for_pattern(prices, diff_patterns, diff_pattern)
        if total > max_total:
            max_total = total
            max_pattern = diff_pattern
    return max_total


if __name__ == "__main__":
    print(f"part 1 = {part1()}")
    print(f"part 2 = {part2()}") 