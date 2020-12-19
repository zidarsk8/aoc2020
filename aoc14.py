from typing import List, Dict
import aoc14_data


def parse_single(text: str):

    lines: List[str] = text.splitlines()

    mask_text = lines[0].replace("mask = ", "")
    and_mask = int(mask_text.replace("X", "1"), 2)
    or_mask = int(mask_text.replace("X", "0"), 2)
    float_mask = int(mask_text.replace("1", "0").replace("X", "1"), 2)

    commands = [
        tuple(map(int, line.replace("mem[", "").split("] = "))) for line in lines[1:]
    ]

    return and_mask, or_mask, float_mask, commands


def parse(text: str):

    parts = text[7:].split("mask = ")
    groups = []
    for part in parts:
        groups.append(parse_single(part))
    return groups


def run_commands(groups):
    ram = {}
    for and_mask, or_mask, float_mask, commands in groups:
        for addr, value in commands:
            ram[addr] = (value & and_mask) | or_mask
    return ram


def print_ram(ram: Dict[int, int]):
    for loc, value in sorted(ram.items()):
        print(f"{loc:>5} : {bin(value):>38}   {value:>5}")


def test_1():
    groups = parse(aoc14_data.test_data2)

    ram = run_commands(groups)
    print_ram(ram)
    print(sum(ram.values()))


def test_part1():
    groups = parse(aoc14_data.data)

    ram = run_commands(groups)
    print(sum(ram.values()))


def generate_floating(float_mask):
    # print(f"{bin(float_mask):>38}")
    if float_mask == 0:
        return [0]
    if float_mask == 1:
        return [0, 1]
    children = generate_floating(int(bin(float_mask)[3:], 2))
    return [2 ** (len(bin(float_mask)) - 3) + n for n in children] + children


def decoder2(groups):
    ram = {}
    for and_mask, or_mask, float_masks, commands in groups:
        for addr, value in commands:
            for float_mask in generate_floating(float_masks):
                address = (addr & ((2 ** 40 - 1) & ~float_masks)) | or_mask | float_mask

                print(f"{bin(address)[2:]:>38}")

                ram[address] = value
    return ram


def test_generate_floating():

    for i in sorted(generate_floating(22)):
        print(f"{bin(i)[2:]:>38}")
    assert sorted(generate_floating(22)) == [0, 2, 4, 6, 16, 18, 20, 22]


def test_part2():
    groups = parse(aoc14_data.data)
    ram = decoder2(groups)

    print(sum(ram.values()))

    assert False
