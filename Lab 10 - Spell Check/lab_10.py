import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    my_file = open("dictionary.txt")
    dictionary_list = []

    for line in my_file:
        line = line.strip()

        dictionary_list.append(line)

    my_file.close()

    print("---linear search---")

    my_file = open("AliceInWonderLand200.txt")
    line_number = 1

    for line in my_file:
        line = line.strip()
        word_list = split_line(line)

        for word in word_list:
            found = False
            word_upper = word.upper()
            for dict in dictionary_list:
                if dict == word_upper:
                    found = True
                    break;

            if not found:
                print("Line", line_number, "possible misspelled word:", word)

        line_number += 1

    my_file.close()

    print("---Binary Search---")
    my_file = open("AliceInWonderLand200.txt")
    line_number = 1

    for line in my_file:
        line = line.strip()
        word_list = split_line(line)

        for word in word_list:
            found = False
            word_upper = word.upper()
            start = 0
            end = len(dictionary_list) - 1

            while start <= end and not found:
                middle = (end + start) // 2
                key = dictionary_list[middle]

                if key < word_upper:
                    start = middle + 1
                elif key > word_upper:
                    end = middle - 1
                else:
                    found = True
                    break

            if not found:
                print("Line", line_number, "possible misspelled word:", word)

        line_number += 1

    my_file.close()

main()
