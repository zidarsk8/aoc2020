import aoc5_data


def get_num(id_):
    return int(
        id_.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0"), 2
    )


def test_aoc5():
    print(aoc5_data.test_data)

    assert get_num("BFFFBBFRRR") == 567.0
    assert get_num("FFFBBBFRRR") == 119.0
    assert get_num("BBFFBBFRLL") == 820.0

    seats = sorted([get_num(line) for line in aoc5_data.data.splitlines()])
    for i, seat in enumerate(seats):
        print(i, seat, seat - i - 28)

    assert False
