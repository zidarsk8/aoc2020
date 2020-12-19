import aoc9_data


def is_sum(data, sum_):
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            if data[i] + data[j] == sum_:
                return True
    return False


def find_broken(data, preamble):
    for i in range(preamble, len(data)):
        valid = is_sum(data[i - preamble : i], data[i])
        # print(i, data[i], data[i - preamble : i], valid)
        if not valid:
            return data[i]
    pass


def find_range(data, broken):
    for last_index, item in enumerate(data):
        for first_index in range(last_index - 2, -1, -1):
            s = sum(data[first_index:last_index])
            if s == broken:
                return data[first_index:last_index]
            if s > broken:
                break


def test_aoc9_part1_test():
    data = list(map(int, aoc9_data.test_data.splitlines()))
    assert find_broken(data, 5) == 127


def test_aoc9_part1():
    data = list(map(int, aoc9_data.data.splitlines()))
    print(find_broken(data, 25))


def test_aoc9_part2_test():
    data = list(map(int, aoc9_data.test_data.splitlines()))
    broken = find_broken(data, 5)
    r = find_range(data, broken)
    print(min(r) + max(r))


def test_aoc9_part2():
    data = list(map(int, aoc9_data.data.splitlines()))
    broken = find_broken(data, 25)
    r = find_range(data, broken)
    print(min(r) + max(r))


def get_leaderboard():
    import requests

    cookies = {
        "session": "53616c7465645f5f38ebdef428b7e6061b4208d01f491317418b2c00bd1ce591259b7cac79ff31660af57ae7f26925e6",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://adventofcode.com/2020/leaderboard/private",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers",
    }

    response = requests.get(
        "https://adventofcode.com/2020/leaderboard/private/view/119027",
        headers=headers,
        cookies=cookies,
    )
    return response


def test_aoc():

    response = get_leaderboard()
    print(
        response.text.replace(
            """<span class="privboard-star-locked">*</span>""", ""
        ).replace("""[X]</a></div>""", "[X]</a></div>\n")
    )
    

    assert False
