import logging
import re

import aoc7_data


def parse_quantity(text):
    if not text:
        return []

    def pars(item):
        n, bag = item.split(" ", 1)
        return int(n), bag

    return [pars(item) for item in text.replace(".", "").split(", ")]


def get_connections(text):

    connections = {}
    data = (
        text.strip()
        .replace("no other bags.", "")
        .replace(" bags", "")
        .replace(" bag", "")
        .splitlines()
    )

    for line in data:
        mapping, quantity = line.split(" contain ")
        connections[mapping] = parse_quantity(quantity)
    return connections


def reverse_connections(connections):
    t = [
        (bag, parent)
        for parent, items in connections.items()
        for n, bag in items
        if items
    ]
    rev = {bag: [] for bag, _ in t}

    for bag, parent in t:
        rev[bag].append(parent)
    return rev


def gather(rev, start):
    s = {start}
    visited = set()
    while s:
        item = s.pop()
        visited.add(item)

        for t in rev.get(item, []):
            s.add(t)

    visited.remove(start)
    return visited


def test_aoc7_test1():
    connections = get_connections(aoc7_data.test_data)
    print(connections)
    rev = reverse_connections(connections)
    print(rev)

    start = "shiny gold"
    print(gather(rev, start))
    print(len(gather(rev, start)))


def walk(connections, start):
    calculated = {bag: 1 for bag, children in connections.items() if not children}

    remaining = {bag: children for bag, children in connections.items() if children}

    while remaining:
        for bag, children in list(remaining.items()):
            if all(child in calculated for _, child in children):
                cnt = sum(cnt * calculated[child] for cnt, child in children) + 1
                calculated[bag] = cnt
                del remaining[bag]

    print(calculated[start] - 1)

    pass


def test_aoc7_test2():
    connections = get_connections(aoc7_data.test_data)

    start = "shiny gold"
    walk(connections, start)

    assert False


def test_aoc7_part2():
    connections = get_connections(aoc7_data.data)

    start = "shiny gold"
    walk(connections, start)

    assert False


def test_aoc7_part1():
    connections = get_connections(aoc7_data.data)
    rev = reverse_connections(connections)

    start = "shiny gold"
    assert len(gather(rev, start)) == 197
