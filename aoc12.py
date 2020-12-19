import aoc12_data
from typing import List, Tuple

Directions = List[Tuple[str, int]]


def drive(directions: Directions):
    current_dir = 90
    direction_map = {
        0: "N",
        90: "E",
        180: "S",
        270: "W",
    }
    current_pos = [0, 0]
    moves = {"E": (0, 1), "W": (0, -1), "N": (1, 0), "S": (-1, 0)}
    for direction, steps in directions:
        if direction == "F":
            current_pos[0] += moves[direction_map[current_dir]][0] * steps
            current_pos[1] += moves[direction_map[current_dir]][1] * steps
        elif direction in "NSEW":
            current_pos[0] += moves[direction][0] * steps
            current_pos[1] += moves[direction][1] * steps
        if direction in "R":
            current_dir = (current_dir + steps) % 360
        if direction in "L":
            current_dir = (current_dir - steps) % 360

    return sum(map(abs, current_pos))


def test_part1():
    directions: Directions = [
        (line[0], int(line[1:])) for line in aoc12_data.data.splitlines()
    ]

    print(drive(directions))

    assert False


def drive2(directions: Directions):
    waypoint = [1, 10]
    current_dir = 0
    direction_map = {
        0: "N",
        90: "E",
        180: "S",
        270: "W",
    }
    current_pos = [0, 0]
    print(directions)
    moves = {"E": (0, 1), "W": (0, -1), "N": (1, 0), "S": (-1, 0)}
    for direction, steps in directions:
        if direction == "F":
            if current_dir == 0:
                current_pos[0] += steps * waypoint[0]
                current_pos[1] += steps * waypoint[1]
            if current_dir == 90:
                current_pos[0] += steps * -waypoint[1]
                current_pos[1] += steps * waypoint[0]
            if current_dir == 180:
                current_pos[0] += steps * -waypoint[0]
                current_pos[1] += steps * -waypoint[1]
            if current_dir == 270:
                current_pos[0] += steps * waypoint[1]
                current_pos[1] += steps * -waypoint[0]

        elif direction in "NSEW":
            waypoint[0] += moves[direction][0] * steps
            waypoint[1] += moves[direction][1] * steps

        if direction in "R":
            if steps == 90:
                waypoint = [-waypoint[1], waypoint[0]]
            elif steps == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif steps == 270:
                waypoint = [waypoint[1], -waypoint[0]]
        if direction in "L":
            steps = (360 - steps) % 360
            if steps == 90:
                waypoint = [-waypoint[1], waypoint[0]]
            elif steps == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif steps == 270:
                waypoint = [waypoint[1], -waypoint[0]]

        print()
        print(waypoint)
        print(current_pos)
        print(current_dir)

    return sum(map(abs, current_pos))


def test_part2_1():
    directions: Directions = [
        (line[0], int(line[1:])) for line in aoc12_data.test_data.splitlines()
    ]

    print(drive2(directions))

    assert False


def test_part2():
    directions: Directions = [
        (line[0], int(line[1:])) for line in aoc12_data.data.splitlines()
    ]

    print(drive2(directions))

    assert False
