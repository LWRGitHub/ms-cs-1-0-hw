def get_file_lines(filename):

    file_line = open(filename, 'r')
    lines_list = file_line.readlines()

    return lines_list

def lines_printed_backwards(lines_list):

    num_list = range(len(lines_list))

    lines_list.reverse()
    num_list.reverse()

    for num in num_list:
        print(f"{num_list[num]} {lines_list[num]}")


lines_printed_backwards(get_file_lines("poem.txt"))