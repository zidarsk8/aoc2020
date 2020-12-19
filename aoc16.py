#

import aoc16_data


def parse_rules(text: str):
    rules = {}
    for line in text.splitlines():
        name, ranges = line.split(": ")
        range1_txt, range2_txt = ranges.split(" or ")
        range1 = [int(i) for i in range1_txt.split("-")]
        range2 = [int(i) for i in range2_txt.split("-")]
        valid = set(range(range1[0], range1[1] + 1)) | set(
            range(range2[0], range2[1] + 1)
        )
        rules[name] = (range1, range2, valid)

    return rules


def parse_ticket(text: str):
    return [int(i) for i in text.splitlines()[1].split(",")]


def parse_nearby(text: str):
    nearby_tickets = []
    for line in text.splitlines()[1:]:
        nearby_tickets.append([int(i) for i in line.split(",")])
    return nearby_tickets


def parse(text):
    rules_text, ticket_text, nearby_text = text.split("\n\n")
    rules = parse_rules(rules_text)
    ticket = parse_ticket(ticket_text)
    nearby = parse_nearby(nearby_text)

    return rules, ticket, nearby


def get_valid_numbers(rules):
    valid = set()
    for range1, range2, _ in rules.values():
        valid |= set(range(range1[0], range1[1] + 1))
        valid |= set(range(range2[0], range2[1] + 1))
    return valid


def validate_tickets(rules, tickets):
    valid = get_valid_numbers(rules)
    invalid = []
    for ticket in tickets:
        for value in ticket:
            if value not in valid:
                invalid.append(value)

    return invalid


def part1(text):
    rules, ticket, nearby = parse(text)

    invalid = validate_tickets(rules, nearby)
    return sum(invalid)


def test_part1():

    assert part1(aoc16_data.test) == 71
    assert part1(aoc16_data.data) == 21081


def part2(text):
    rules, my_ticket, tickets = parse(text)

    invalid = set(validate_tickets(rules, tickets))
    filtered_tickets = [
        ticket for ticket in tickets if not set(ticket).intersection(invalid)
    ]

    possible = [set(rules.keys()) for _ in my_ticket]

    for ticket in filtered_tickets:
        for i, number in enumerate(ticket):

            for rule_name, ranges in rules.items():
                if (
                    number not in ranges[2]
                    and rule_name in possible[i]
                    and len(possible) > 1
                ):
                    possible[i].remove(rule_name)
                    if len(possible[i]) == 1:
                        only = possible[i].pop()
                        [p.remove(only) for p in possible if only in p]
                        possible[i] = {only}

    for _ in range(len(possible)):
        for i in range(len(possible)):
            if len(possible[i]) == 1:
                only = possible[i].pop()
                [p.remove(only) for p in possible if only in p]
                possible[i] = {only}

    return {name.pop(): number for name, number in zip(possible, my_ticket)}


def test_part2():
    # assert part2(aoc16_data.test2) == {"class": 12, "row": 11, "seat": 13}
    p = part2(aoc16_data.data)
    for k, v in p.items():
        print(k, v)

    product = (
        p["departure location"]
        * p["departure station"]
        * p["departure platform"]
        * p["departure track"]
        * p["departure date"]
        * p["departure time"]
    )

    assert product == 0
