test_data = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".strip()

from lark import Lark
import aoc19_data


def test_part1():
    text = test_data
    text = aoc19_data.text

    text = (
        text.replace("1", "a1")
        .replace("2", "a2")
        .replace("3", "a3")
        .replace("4", "a4")
        .replace("5", "a5")
        .replace("6", "a6")
        .replace("7", "a7")
        .replace("8", "a8")
        .replace("9", "a9")
        .replace("0", "a0")
    )
    print(text)
    grammar, lines = text.split("\n\n")
    parser = Lark(grammar, start="a0")
    counter = 0
    for line in lines.splitlines():
        try:
            parser.parse(line)
            counter += 1
        except Exception as e:
            print(e)
    assert counter == 156


def test_part1():
    text = test_data
    text = aoc19_data.text

    text = (
        text.replace("1", "a1")
        .replace("2", "a2")
        .replace("3", "a3")
        .replace("4", "a4")
        .replace("5", "a5")
        .replace("6", "a6")
        .replace("7", "a7")
        .replace("8", "a8")
        .replace("9", "a9")
        .replace("0", "a0")
    )

    grammar, lines = text.split("\n\n")

    grammar = "\n".join(
        "a8: a4a2 | a4a2 a8" if line.startswith("a8:") else line
        for line in grammar.splitlines()
    )
    grammar = "\n".join(
        "a1a1: a4a2 a3a1 | a4a2 a1a1 a3a1" if line.startswith("a1a1:") else line
        for line in grammar.splitlines()
    )
    print(grammar)

    parser = Lark(grammar, start="a0")
    counter = 0
    for line in lines.splitlines():
        try:
            parser.parse(line)
            counter += 1
        except Exception as e:
            pass

    assert counter == 363
