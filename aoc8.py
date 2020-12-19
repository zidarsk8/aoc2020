from typing import Dict, Set

import aoc8_data


class PC:
    def __init__(self, verbose=False):
        self.pc: int = 0
        self.reg1: int = 0
        self.ram: Dict = {}
        self.verbose: bool = verbose
        self.instructions: List[Tuple[str, int]] = []
        self.exit: bool = False
        self.error: int = 0
        self.visited: Set[int] = set()

    def reset(self):
        self.pc = 0
        self.reg1 = 0
        self.ram = {}
        # self.instructions = []
        self.exit = False
        self.visited = set()

    def parse_instructions(self, data):
        parsed = [line.split() for line in data.splitlines()]
        self.instructions = [(instruction, int(param)) for instruction, param in parsed]

        if self.verbose:
            self.print_state()

    def print_state(self):
        print("---")
        print(f" pc  = {self.pc}")
        print(f" reg1 = {self.reg1}")
        for index, c in enumerate(self.instructions):
            current = "*" if self.pc == index else " "
            print(f"{index:>5}    {current}  {c}")
        print("---")

    def check_loop(self):
        if self.pc in self.visited:
            return True
        self.visited.add(self.pc)
        return False

    def nop(self, param):
        self.pc += 1

    def acc(self, param):
        self.reg1 += param
        self.pc += 1

    def jmp(self, param):
        self.pc += param

    def run_command(self):
        if self.verbose:
            self.print_state()
        if self.check_loop():
            print("Doom!")
            self.error = 1
            self.exit = True
            return

        if self.pc == len(self.instructions):
            print("Happy Ending")
            self.error = 0
            self.exit = True
            return

        command, param = self.instructions[self.pc]
        if self.verbose:
            print(f"{self.pc:>5}    {self.reg1:>5}  -  {command}   {param:>5}")

        method = getattr(self, command, None)
        if not method:
            self.exit = True
            return

        method(param)

    def run_program(self, data):
        max_commands = 100000
        print()
        print(self.instructions)
        for _ in range(max_commands):
            self.run_command()

            if self.exit:
                break

        print(self.reg1)

    def _swap(self, index):
        swap = {"jmp": "nop", "nop": "jmp"}

        self.instructions[index] = (
            swap[self.instructions[index][0]],
            self.instructions[index][1],
        )

    def debug_program(self, data):
        self.parse_instructions(data)
        original_instructions = self.instructions

        self.parse_instructions(data)
        print(self.instructions)
        print()

        for i in range(len(self.instructions)):
            if self.instructions[i][0] in ("nop", "jmp"):
                self._swap(i)
                self.reset()
                self.run_program(data)
                self._swap(i)
                if not self.error:
                    break


def test_aoc8_part1_test():
    data = aoc8_data.test_data
    pc = PC()
    pc.run_program(data)


def test_aoc8_part1():
    data = aoc8_data.data
    pc = PC()
    pc.run_program(data)


def test_aoc8_part2_test():
    data = aoc8_data.test_data
    pc = PC()
    pc.debug_program(data)

    assert False


def test_aoc8_part2():
    data = aoc8_data.data
    pc = PC()
    pc.debug_program(data)

    assert False
