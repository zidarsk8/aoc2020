test_data = """
939
7,13,x,x,59,x,31,19
""".strip()

data = """
1001612
19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,821,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,463,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23
""".strip()


def test_aoc13_p1t():
    time, schedule = test_data.splitlines()
    time = int(time)
    schedule = [int(bus) for bus in schedule.split(",") if bus != "x"]
    print(time)
    print(schedule)

    departures = []
    for bus in schedule:
        departure = (bus - (time % bus)) if time % bus else 0
        departures.append((departure, bus))

    departures.sort()

    print(departures[0])
    print(departures[0][0] * departures[0][1])

    assert departures[0][0] * departures[0][1] == 295


def test_aoc13_p1():
    time, schedule = data.splitlines()
    time = int(time)
    schedule = [int(bus) for bus in schedule.split(",") if bus != "x"]
    print(time)
    print(schedule)

    departures = []
    for bus in schedule:
        departure = (bus - (time % bus)) if time % bus else 0
        departures.append((departure, bus))

    departures.sort()

    print(departures[0])
    print(departures[0][0] * departures[0][1])

    assert departures[0][0] * departures[0][1] == 6568


def find_common(offset, a, b):
    print()
    print(offset, a, b)
    for i in range(2000):
        print(
            f"a = {a},  n = {offset + a * i}  remainder {(offset + a * i) % b}"
        )
        if (offset + a * i) % b == b - 1:
            return offset + a * i + 1, a * b


def test_find_common():

    assert find_common(0, 3, 7) == (7, 21)

    assert find_common(0, 7, 3) == (15, 21)

    assert find_common(7, 21, 13) == (260, 21 * 13)

    assert find_common(7, 21, 1) == (8, 21)


def get_timestamp(departures):
    print("-" * 100)
    print(departures)

    schedule = [1 if bus == "x" else int(bus) for bus in departures.split(",")]

    offset = 0
    a = schedule[0]

    for b in schedule[1:]:
        offset, a = find_common(offset, a, b)

    return offset - len(schedule) + 1


def test_part2():

    assert get_timestamp("3,7,13") == 258
    assert get_timestamp("3,7,13") == 258
    assert get_timestamp("17,x,13") == 102

    assert get_timestamp(test_data.splitlines()[1]) == 1068781

    assert get_timestamp("17,x,13,19") == 3417
    assert get_timestamp("67,7,59,61") == 754018
    assert get_timestamp("67,x,7,59,61") == 779210
    assert get_timestamp("67,7,x,59,61") == 1261476
    assert get_timestamp("1789,37,47,1889") == 1202161486

    assert get_timestamp(data.splitlines()[1]) == 554865447501099
