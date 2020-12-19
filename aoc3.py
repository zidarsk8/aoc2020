import aoc3_data


grid = aoc3_data.test_data.strip().splitlines()
grid = aoc3_data.data.strip().splitlines()


def get_pos(x, y):
    x_len = len(grid[0])
    if y >= len(grid):
        return None
    return grid[y][x % x_len]


for y in range(10):
    for x in range(20):
        print(get_pos(x, y), end="")
    print()


def count_trees(y, x):
    slope = (y, x)

    pos = 0, 0
    trees = 0
    while get_pos(*pos):
        if get_pos(*pos) == "#":
            trees += 1
        pos = tuple(sum(i) for i in zip(slope, pos))

    return trees


print(count_trees(1, 1))
print(count_trees(3, 1))
print(count_trees(5, 1))
print(count_trees(7, 1))
print(count_trees(1, 2))


print(
    count_trees(1, 1)
    * count_trees(3, 1)
    * count_trees(5, 1)
    * count_trees(7, 1)
    * count_trees(1, 2)
)
