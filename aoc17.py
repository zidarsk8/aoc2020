#
from typing import Tuple, DefaultDict

import itertools

from collections import defaultdict

test_data = """
.#.
..#
###
""".strip()


data = """
..##.#.#
.#####..
#.....##
##.##.#.
..#...#.
.#..##..
.#...#.#
#..##.##
""".strip()


def count_neighbors2(grid, point):
    count = 0
    for dw in range(-1, 2):
        for dz in range(-1, 2):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == dy == dz == dw == 0:
                        continue
                    if (
                        grid[
                            (point[0] - dx, point[1] - dy, point[2] - dz, point[3] - dw)
                        ]
                        == "#"
                    ):
                        count += 1
    return count


def count_neighbors(grid, point):
    count = 0
    for dz in range(-1, 2):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == dz == 0:
                    continue
                if grid[(point[0] - dx, point[1] - dy, point[2] - dz)] == "#":
                    count += 1
    return count


def print_grid2(grid, size=5, shift=2):
    for dw in range(-size, size):
        for dz in range(-size, size):
            print("z = ", dz)
            print("w = ", dw)
            for dx in range(-size, size):
                for dy in range(-size, size):
                    print(grid[(dx + shift, dy + shift, dz, dw)], end="")
                print()
            print()
    print("---------------------------------------------------")


def print_grid(grid, size=5, shift=2):
    for dz in range(-size, size):
        print("z = ", dz)
        for dx in range(-size, size):
            for dy in range(-size, size):
                print(grid[(dx + shift, dy + shift, dz)], end="")
            print()
        print()
    print("---------------------------------------------------")


def get_bounding(grid):
    max_x = max(x for x, y, z in grid.keys())
    max_y = max(y for x, y, z in grid.keys())
    max_z = max(z for x, y, z in grid.keys())
    min_x = min(x for x, y, z in grid.keys())
    min_y = min(y for x, y, z in grid.keys())
    min_z = min(z for x, y, z in grid.keys())
    return min_x, max_x, min_y, max_y, min_z, max_z


def get_bounding2(grid):
    max_x = max(x for x, y, z, w in grid.keys())
    max_y = max(y for x, y, z, w in grid.keys())
    max_z = max(z for x, y, z, w in grid.keys())
    max_w = max(w for x, y, z, w in grid.keys())
    min_x = min(x for x, y, z, w in grid.keys())
    min_y = min(y for x, y, z, w in grid.keys())
    min_z = min(z for x, y, z, w in grid.keys())
    min_w = min(w for x, y, z, w in grid.keys())
    return min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w


def tick(grid: DefaultDict[Tuple[int, int, int], str]):
    new_grid = grid.copy()
    min_x, max_x, min_y, max_y, min_z, max_z = get_bounding(grid)
    for z in range(min_z - 1, max_z + 2):
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                count = count_neighbors(grid, [x, y, z])
                if grid[(x, y, z)] == "#" and count not in (2, 3):
                    new_grid[(x, y, z)] = "."
                if grid[(x, y, z)] == "." and count == 3:
                    new_grid[(x, y, z)] = "#"

    return new_grid


def part1(text: str):
    grid = defaultdict(lambda: ".")
    for y, line in enumerate(text.splitlines()):
        for x, char in enumerate(line):
            grid[(x, y, 0)] = char

    grid = tick(grid)
    grid = tick(grid)

    grid = tick(grid)
    grid = tick(grid)

    grid = tick(grid)
    grid = tick(grid)

    return sum(value == "#" for value in grid.values())


def test_part1():
    assert part1(test_data) == 112
    assert part1(data) == 213


def tick2(grid: DefaultDict[Tuple[int, int, int], str]):
    new_grid = grid.copy()
    min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w = get_bounding2(grid)
    for w in range(min_w - 1, max_w + 2):
        for z in range(min_z - 1, max_z + 2):
            for x in range(min_x - 1, max_x + 2):
                for y in range(min_y - 1, max_y + 2):
                    count = count_neighbors2(grid, [x, y, z, w])
                    if grid[(x, y, z, w)] == "#" and count not in (2, 3):
                        new_grid[(x, y, z, w)] = "."
                    if grid[(x, y, z, w)] == "." and count == 3:
                        new_grid[(x, y, z, w)] = "#"

    return new_grid


def part2(text: str):
    grid = defaultdict(lambda: ".")
    for y, line in enumerate(text.splitlines()):
        for x, char in enumerate(line):
            grid[(x, y, 0, 0)] = char

    grid = tick2(grid)
    print_grid2(grid)
    grid = tick2(grid)

    grid = tick2(grid)
    grid = tick2(grid)

    grid = tick2(grid)
    grid = tick2(grid)

    return sum(value == "#" for value in grid.values())


def test_part2():
    assert part2(test_data) == 848
    assert part2(data) == 1624
