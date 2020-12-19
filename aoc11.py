import aoc11_data
import copy


def load_data(text_data):
    lines = text_data.splitlines()
    l = len(lines[0])

    grid = [[" "] + list(l) + [" "] for l in lines]
    return [list(" " * (l + 2))] + grid + [list(" " * (l + 2))]


def to_str(grid):
    return "\n".join("".join(row) for row in grid)


def print_grid(grid):
    print()
    print(to_str(grid))
    print()


def tick(grid):
    new_grid = copy.deepcopy(grid)
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item in ".* ":
                continue
            if item == "L":
                count_occupied = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if grid[y + dy][x + dx] == "#":
                            count_occupied += 1
                if not count_occupied:
                    new_grid[y][x] = "#"
            if item == "#":
                count_occupied = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if grid[y + dy][x + dx] == "#":
                            count_occupied += 1
                if count_occupied > 4:
                    new_grid[y][x] = "L"

    return new_grid


def count(grid):
    count_occupied = 0
    for row in grid:
        for item in row:
            if item == "#":
                count_occupied += 1
    return count_occupied


def test_aoc11():
    grid = load_data(aoc11_data.test_data)
    print_grid(grid)
    old_grid = [[]]
    while to_str(grid) != to_str(old_grid):
        old_grid = grid
        grid = tick(grid)

    print_grid(grid)
    print(count(grid))


def tick2(grid):
    new_grid = copy.deepcopy(grid)
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item in ".* ":
                continue
            if item == "L":
                count_occupied = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        m = 1
                        while grid[y + dy * m][x + dx * m] == ".":
                            m += 1
                        if grid[y + dy * m][x + dx * m] == "#":
                            count_occupied += 1
                if not count_occupied:
                    new_grid[y][x] = "#"
            if item == "#":
                count_occupied = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        m = 1
                        while grid[y + dy * m][x + dx * m] == ".":
                            m += 1
                        if grid[y + dy * m][x + dx * m] == "#":
                            count_occupied += 1
                if count_occupied > 5:
                    new_grid[y][x] = "L"

    return new_grid


def test_aoc11_part2():
    grid = load_data(aoc11_data.data)
    print_grid(grid)
    old_grid = [[]]
    while to_str(grid) != to_str(old_grid):
        old_grid = grid
        grid = tick2(grid)

    print_grid(grid)
    print(count(grid))

    assert False
