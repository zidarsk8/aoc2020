def rotate(cups, left):
    return cups[left:] + cups[:left]


def find_destination(current: str, cups: str):
    candidate = int(current) - 1
    while str(candidate) not in cups and candidate > 0:
        candidate -= 1

    return str(candidate) if candidate else max(cups)


def crab(cups: str, moves):

    current_pos = 0
    destination = 0
    for i in range(moves):
        pick_up = cups[1:4]
        destination = find_destination(cups[0], cups[4:])
        destination_pos = cups.find(destination)

        pass

    pass


def test_find_destination():
    assert find_destination("3", "25467") == "2"
    assert find_destination("2", "54673") == "7"
    assert find_destination("5", "32891") == "3"
    assert find_destination("8", "72546") == "7"
    assert find_destination("4", "32581") == "3"
    assert find_destination("1", "92584") == "9"


def test_rotate():
    assert rotate("389125467", 1) == "891254673"
    assert rotate("389125467", 2) == "912546738"
    assert rotate("389125467", 4) == "254673891"


def test_part1():
    assert crab("389125467", 10) == 92658374
    assert crab("389125467", 100) == 67384529
    assert crab("459672813", 100) == 0
