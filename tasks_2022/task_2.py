def count_score():
    from pathlib import Path
    data_folder = Path("tasks_2022/")
    file_to_open = data_folder / "data_2.txt"
    f = open(file_to_open)
    lines = f.readlines()

    print(lines)