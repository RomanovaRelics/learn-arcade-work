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

    print( "There are", len(line_list), "lines in the file.")

    return line_list

def main():
    #dictionary_lines = read_in_file("dictionary.txt")
    #for word in dictionary_lines:
        #print(word)
    chapter_lines = read_in_file("AliceInWonderLand200.txt")
    chapter_words = []
    #for word in alice_lines:
        #print(word)

    for line in chapter_lines:
        line_words = split_line(line)
        for word in line_words:
            chapter_words.append(word)
            print(word)

def linear_search(word, dictionary):

    # Start at the beginning of the list
    current_position_in_dictionary = 0

    found = False

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the word
    while current_position_in_dictionary < len(dictionary) and dictionary[current_position_in_dictionary] != word:
        # Advance to the next word in the dictionary
        current_position_in_dictionary += 1

    if current_position_in_dictionary < len(dictionary):
        print("The name is at position", current_position_in_dictionary)
        return True
    else:
        print("The name was not in the list.")
        return False

main()
