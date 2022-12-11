def count_score():
    from pathlib import Path
    data_folder = Path("tasks_2022/")
    file_to_open = data_folder / "data_2.txt"
    f = open(file_to_open)
    lines = f.readlines()
    score = 0

    for i in lines:
        values = to_int_list(i)
        score += calculate_line_score(values[0], values[1])

    return score


def calculate_line_score(opponent, me):
    if opponent == me:
        return 3 + me
    elif (opponent == 1 and me == 2) or (opponent == 2 and me == 3) or (opponent == 3 and me == 1):
        return 6 + me
    else:
        return me


def convert_string_to_int(character):
    if character == "A" or character == "X":
        return 1
    elif character == "B" or character == "Y":
        return 2
    else:
        return 3


def to_int_list(value):
    string_list = value.replace("\n", "").split(" ")
    opponent = convert_string_to_int(string_list[0])
    me = convert_string_to_int(string_list[1])
    return [opponent, me]
