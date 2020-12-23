#
from typing import List

import aoc20_data


class Tile:
    def __init__(self, text: str):
        lines = text.splitlines()
        self.id: int = int(lines[0].split()[1][:-1])
        self.tile = lines[1:]



class Canvas:
    def __init__(self, text: str):
        self.tiles: List[Tile] = [Tile(tile_text) for tile_text in text.split("\n\n")]
        pass


def test_part1():
    canvas = Canvas(aoc20_data.test_data)
    assert False
