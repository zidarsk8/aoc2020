#


def play_game(starting_text: str, steps=2020):
    numbers = [int(n) for n in starting_text.split(",")]
    indexes = {n: [i, i] for i, n in enumerate(numbers)}

    for turn in range(len(numbers), steps):
        last_n = numbers[turn - 1]
        previous_occurance = indexes[last_n][-2]
        current_number = turn - 1 - previous_occurance
        if current_number not in indexes:
            indexes[current_number] = [turn, turn]
        else:
            indexes[current_number].append(turn)
        numbers.append(current_number)

    return current_number


def testaoc1():
    assert play_game("0,3,6", 9) == 4
    assert play_game("0,3,6") == 436

    assert play_game("1,3,2") == 1
    assert play_game("2,1,3") == 10
    assert play_game("1,2,3") == 27
    assert play_game("2,3,1") == 78
    assert play_game("3,2,1") == 438
    assert play_game("3,1,2") == 1836
    assert play_game("1,0,18,10,19,6") == 441


def test2():
    assert play_game("0,3,6", 30000000) == 175594
    assert play_game("1,0,18,10,19,6", 30000000) == 441
