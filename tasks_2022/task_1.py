def elves_calories():
    with open('data_1.txt') as f:
        lines = f.readlines()

    active_sum = 0
    my_list = []
    lines.append("")

    for i in lines:
        a = i.replace("\n", "")
        if a == "":
            my_list.append(active_sum)
            active_sum = 0
        else:
            active_sum += int(a)

    elf_sum = sum(sorted(my_list)[-3:])
    return elf_sum
