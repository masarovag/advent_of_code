def sonar():
    from pathlib import Path
    data_folder = Path("tasks_2021/")
    file_to_open = data_folder / "data_1.txt"
    f = open(file_to_open)
    lines = f.readlines()

    suma = 0
    index = 0
    for i in lines:
        if index + 1 == len(lines):
            return suma

        if int(i.replace("\n", "")) < int(lines[index + 1].replace("\n", "")):
            suma += 1

        index = index + 1
    return suma
