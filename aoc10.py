import aoc10_data
import math


def arrangements(data):

    groups = []
    current_group = 0
    for i, d in enumerate(data):
        skip1 = 0 < i < len(data) - 1 and d - data[i - 1] == 1 and data[i + 1] - d == 1
        print(f"{d:>3}   {skip1}")
        if skip1:
            current_group += 1
        else:
            if current_group != 0:
                groups.append(current_group)
            current_group = 0
    print(groups)

    options = {1:2, 2:4, 3:7}

    powers = [options[g] for g in groups if g != 0]
    print(math.prod(powers))


def test_aoc10():
    data = list(sorted(list(map(int, aoc10_data.data.splitlines()))))
    data.insert(0, 0)
    data.append(max(data) + 3)
    diffs = {1: 0, 2: 0, 3: 0}
    for index, d in enumerate(data[:-1]):
        diffs[data[index + 1] - d] += 1
    print(data)
    print(diffs)

    assert diffs[1] * diffs[3] == 1998
    assert False


def test_part2_2():
    data = list(sorted(list(map(int, aoc10_data.data2.splitlines()))))
    data.insert(0, 0)
    data.append(max(data) + 3)
    arrangements(data)

    assert False


def test_part2():
    data = list(sorted(list(map(int, aoc10_data.data.splitlines()))))
    data.insert(0, 0)
    data.append(max(data) + 3)
    arrangements(data)

    assert False
