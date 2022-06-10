def main(inp):
    out = []

    for row in inp:
        filtered_row = []
        for i in range(len(row)):
            if (row[i] is not None):
                filtered_row.append(row[i])
        if (len(filtered_row)):
            out.append(filtered_row)

    for row in out:
        a = row[0].split(" ")
        row[0] = '{} {}'.format(a[2], a[0])
        if (row[1] == "Да"):
            row[1] = "Выполнено"
        else:
            row[1] = "Не выполнено"
        row[2] = "+7({}){}-{}-{}".format(row[2][2:-7],
                                         row[2][-7:-4],
                                         row[2][-4:-2],
                                         row[2][-2::])
        date = row[3].split("-")
        row[3] = '{}-{}-{}'.format(date[0], date[1], date[2][-2::])
    return out
