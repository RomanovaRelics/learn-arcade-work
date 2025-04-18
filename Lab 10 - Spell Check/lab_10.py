###import regular expression for pattern matching in text
import re

###This function takes in a line of text and returns
### a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def read_in_file(file_name):
    """ Read in lines from a file """

    ### Open the file for reading, and store a pointer to it in the new
    ### variable "file"
    my_file = open(file_name)

    ### Create an empty list to store our names
    line_list = []

    ### Loop through each line in the file like a list
    for line in my_file:
        ### Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        ### Add the name to the list
        line_list.append(line)

    my_file.close()

    #print( "There are", len(line_list), "lines in the file.")

    return line_list

#def linear_search(word, dictionary):

    # Start at the beginning of the list
    #current_position_in_dictionary = 0

    #found = False

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the word
    #while current_position_in_dictionary < len(dictionary) and dictionary[current_position_in_dictionary] != word:
        # Advance to the next word in the dictionary
        #current_position_in_dictionary += 1

    #if current_position_in_dictionary < len(dictionary):
        #print("The word is at position", current_position_in_dictionary)
        #return True
    #else:
        #print("The word was not in the list.")
        #return False

def binary_search(word, dictionary):
    lower_bound = 0
    upper_bound = len(dictionary) - 1
    found = False

    # Loop until we find the item, or our upper/lower bounds meet
    while lower_bound <= upper_bound and not found:

        # Find the middle position
        middle_pos = (lower_bound + upper_bound) // 2

        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if dictionary[middle_pos] < word.upper():
            lower_bound = middle_pos + 1
        elif dictionary[middle_pos] > word.upper():
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        return True
    else:
        return False

def main():
    dictionary_words = read_in_file("dictionary.txt")
    chapter_lines = read_in_file("AliceInWonderLand200.txt")
    #chapter_words = []

    #for line in chapter lines
    for i in range(len(chapter_lines)):
        words = split_line(chapter_lines[i])
        for word in words:
            #if not linear_search(word.upper(), dictionary_words):
            if not binary_search(word.upper(), dictionary_words):
                print(f'The word\'{word}\' is not in the dictionary.')
                print(f'This word is found on line \'{i +1}\'.')

main()
