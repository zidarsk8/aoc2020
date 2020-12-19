import logging
import re

import aoc4_data

fields = {
    "byr": "(Birth Year)",
    "iyr": "(Issue Year)",
    "eyr": "(Expiration Year)",
    "hgt": "(Height)",
    "hcl": "(Hair Color)",
    "ecl": "(Eye Color)",
    "pid": "(Passport ID)",
    "cid": "(Country ID)",
}


def check_date(value, min_, max_):
    try:
        return min_ <= int(value.strip()) <= max_
    except:
        return False


def check_height(value):
    return (value[3:] == "cm" and check_date(value[:3], 150, 193)) or (
        value[2:] == "in" and check_date(value[:2], 59, 76)
    )


def check_hair(value):
    rx = re.compile("#[0-9a-f]*")
    return not rx.sub("", value)


def check_pid(value):
    rx = re.compile("[0-9]*")
    return len(value) == 9 and not rx.sub("", value)


def check_passport(passport):
    passport = dict(p.split(":", 1) for p in passport.split())

    required = [field for field in fields if field != "cid"]

    return (
        all(field in passport for field in required)
        and check_date(passport["byr"], 1920, 2002)
        and check_date(passport["iyr"], 2010, 2020)
        and check_date(passport["eyr"], 2020, 2030)
        and check_height(passport["hgt"])
        and check_hair(passport["hcl"])
        and passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        and check_pid(passport["pid"])
    )


def test_aoc4():
    passports = (
        aoc4_data.data.strip().replace("\n\n", "|").replace("\n", " ").split("|")
    )
    valid = 0
    for passport in passports:
        valid += check_passport(passport)
    print(valid)
    assert False
