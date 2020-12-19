import logging
import re

import aoc6_data


def test_aoc4_part1():
    groups = [group.replace("\n", "") for group in aoc6_data.data.strip().split("\n\n")]
    print(sum(list(map(len, (map(set, groups))))))

    assert False


def test_aoc4():
    groups = [
        list(map(set, group.splitlines()))
        for group in aoc6_data.data.strip().split("\n\n")
    ]

    print(groups)
    counts = 0
    for group in groups:
        answers: set = group[0]
        for person in group:
            answers.intersection_update(person)
        counts += len(answers)
    print(counts)

    assert False
