import random

#Q1
def get_file_lines(filename):
    """ gets file & puts it in a list """
    file_line = open(filename, 'r')
    lines_list = file_line.readlines()

    return lines_list

#Q2
def lines_printed_backwards(lines_list):
    """ prints lines backwards with line number """
    num_list = range(len(lines_list))
    num_list = list(num_list)

    for num in reversed(num_list):
        print(f"{num_list[num]} {lines_list[num]}")

#Q3
def lines_printed_random(lines_list):
    """ prints random lines """
    num_list = range(len(lines_list))
    num_list = list(num_list)

    for i in num_list:
        num = random.randrange(10)
        print(lines_list[num])
  
#Q4
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

#S1
def stretch_write_file(lines_list):
    file_name = f"{input('Please enter a file name for the file: ')}.txt"
    f = open(file_name, "w")

    for line in lines_list: 
        f.write(line)
    print('file created!')

#S3
# def stretch_read_poem_from_input():
#     file_name = f"{input('Please enter a file name for the file: ')}.txt"
#     f = open(file_name, "w")

#     poem = input("Type you poem here: ")
#     f.write(poem)

#     file_line = open(file_name, 'r')
#     lines_list = file_line.readlines()
#     return lines_list

#S2
def stretch_menu():
    poem_list = get_file_lines("poem.txt")

    answer = input('Enter "backwards", "random", "write poem to file" or "custom" to see the poem printed in that way. Or type "done" to exit: ')

    while answer != "done":
        
        if answer == "backwards":
            lines_printed_backwards(poem_list)
            answer = input('Enter "backwards", "random", "write poem to file" or "custom" to see the poem printed in that way. Or type "done" to exit: ')
        elif answer == "random":
            print(lines_printed_random(poem_list))
            answer = input('Enter "backwards", "random", "write poem to file" or "custom" to see the poem printed in that way. Or type "done" to exit: ')
        elif answer == "custom":
            print(lines_printed_custom(poem_list))
            answer = input('Enter "backwards", "random", "write poem to file" or "custom" to see the poem printed in that way. Or type "done" to exit: ')
        elif answer == "write poem to file":
            stretch_write_file(poem_list)
            answer = input('Enter "backwards", "random", "write poem to file" or "custom" to see the poem printed in that way. Or type "done" to exit: ')
        #S3 
        # elif answer == "input peom":
        #     poem_list = stretch_read_poem_from_input()
        #     answer = input('Enter "backwards", "random", "write poem to file" or "custom" to see the poem printed in that way. Or type "done" to exit: ')
        else:
            answer = input('Enter "backwards", "random", "write poem to file" or "custom" to see the poem printed in that way. Or type "done" to exit: ')
    

stretch_menu()