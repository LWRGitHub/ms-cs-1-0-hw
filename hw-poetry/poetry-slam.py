def get_file_lines(filename):
    """ gets file & puts it in a list """
    file_line = open(filename, 'r')
    lines_list = file_line.readlines()

    return lines_list

def lines_printed_backwards(lines_list):
    """ prints lines backwards with line number """
    num_list = range(len(lines_list))
    num_list = list(num_list)

    for num in reversed(num_list):
        print(f"{num_list[num]} {lines_list[num]}")

def lines_printed_random():

def lines_printed_custom(lines_list):
    """ every other letter is capital """
    for line in lines_list:
        string = ''

        num_list = range(len(line))
        num_list = list(num_list)
        for i in num_list:
            if line[i] != ' ' and i % 2 == 0:
                string += line[i].upper()
            else:
                string += line[i]
        print(string)


poem_list = get_file_lines("poem.txt")

lines_printed_backwards(poem_list)

print(lines_printed_random(poem_list))