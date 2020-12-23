data = """
Player 1:
28
3
35
27
19
40
14
15
17
22
45
47
26
13
32
38
43
24
29
5
31
48
49
41
25

Player 2:
34
12
2
50
16
1
44
11
36
6
10
42
20
8
46
9
37
4
7
18
23
39
30
33
21
""".strip()

test_data = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".strip()

test_infinite = """
Player 1:
43
19

Player 2:
2
29
14
""".strip()

from collections import deque
from typing import Deque


def parse(text):
    p1_text, p2_text = text.split("\n\n")
    p1 = deque([int(i) for i in p1_text.splitlines()[1:]])
    p2 = deque([int(i) for i in p2_text.splitlines()[1:]])
    return p1, p2


def test_parse():
    assert parse(test_data)[0] == deque([9, 2, 6, 3, 1])
    assert parse(test_data)[1] == deque([5, 8, 4, 7, 10])


def run_game(text):
    p1, p2 = parse(text)
    safety = 100000
    while p1 and p2 and safety:
        print("-------")
        print(p1)
        print(p2)
        p1_top = p1.popleft()
        p2_top = p2.popleft()
        if p1_top > p2_top:
            p1.append(p1_top)
            p1.append(p2_top)
        else:
            p2.append(p2_top)
            p2.append(p1_top)

        safety -= 1
    print("-------")
    print(p1)
    print(p2)
    return p1, p2


def test_game():
    p1_final, p2_final = run_game(test_data)
    assert p1_final == deque([])
    assert p2_final == deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])


def _prodsum(p1, p2):
    que = p1 or p2

    l = len(que)
    score = sum((l - i) * card for i, card in enumerate(que))
    return score


def prodsum(text):
    p1, p2 = run_game(text)
    score = _prodsum(p1, p2)
    return score


def test_part_1_prod_sum():
    score = prodsum(test_data)
    assert score == 306
    score = prodsum(data)
    assert score == 31781


def run_sub_game(p1, p2):
    safety = 200
    existing_sets = set()

    existing_sets.add((tuple(p1), tuple(p2)))
    while p1 and p2 and safety:
        print("-------")
        print(p1)
        print(p2)
        p1_top = p1.popleft()
        p2_top = p2.popleft()

        if p1_top <= len(p1) and p2_top <= len(p2):
            print("recurse")
            break

        if p1_top > p2_top:
            p1.append(p1_top)
            p1.append(p2_top)
        else:
            p2.append(p2_top)
            p2.append(p1_top)

        if (tuple(p1), tuple(p2)) in existing_sets:
            return p1, deque([])

        safety -= 1
    print("-------")
    print(p1)
    print(p2)
    return p1, p2


def part2(text):
    p1, p2 = parse(text)
    p1, p2 = run_sub_game(p1, p2)
    score = _prodsum(p1, p2)
    return score


def test_part2_infinite():
    p1, p2 = parse(test_infinite)
    p1, p2 = run_sub_game(p1, p2)
    assert p1
    assert not p2


def test_part2():
    score = part2(test_data)
    assert score == 291
