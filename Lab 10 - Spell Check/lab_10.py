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
                print("possible misspelling: ", word, " at line ", line_number)
        #    if uppercase_word in dictionary_list:
        #        print("{word}")
        #    else:
        #        print("Not found in dictionary")

        line_number += 1

    my_file.close()

    print("---Binary Search---")
    my_file = open("AliceInWonderLand200.txt")
    line_number = 1
    start = 0
    end = len(dictionary_list) - 1
    found = False

    while start <= end and not found:
        middle = (end + start) // 2

        if dictionary_list[middle] < word:
            end = middle + 1
        elif dictionary_list[middle] > word:
            start = middle - 1
        else:
            found = True

    if not found:
        print("possible misspelling: ", word, "at line", line_number)
    my_file.close()

main()

#  while start <= end:
#     mid = (start + end) // 2
#     mid_word = dictionary_list[mid]

#    if mid_word == word:
#        found = True
#    elif mid_word < word:
#         start = mid + 1
#     else:
#         end = mid - 1