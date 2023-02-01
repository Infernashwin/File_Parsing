# Name: Ashwin_Assembler_Bonus.py
# Programmer: Ashwin Mayurathan
# Date: Nov 17 2020
# Description: This programs reads a file, and splits each line into a key word
#              and assosciate word and allows user to make a message by
#              inputting keys.

def main():
    # Intializes Variables
    word_dict = {}
    file_name = ""
    file_open = ""
    line_read = ""
    key_input = ""
    str_output = ""

    #Sets info about the file so we can open it as read
    file_name = "raw_meat.txt"
    file_open = open(file_name, "r")

    # Sets line read to the file line of the file
    line_read = file_open.readline()

    # Loops until an empty line is found (so it will stop reading the file)
    while line_read != "":
        # Removes the newline character
        line_read =line_read.strip("\n")
        # Turns the line into a list, with each index representing each word
        line_read = line_read.split()
        # Creates an entry in the dictionary using the first word as the key and
        # the second word is associated with the key
        word_dict[line_read[0]] = line_read[1]
        # Reads the next line
        line_read = file_open.readline()

    # Closes the file
    file_open.close()
        
    # Prints the dictionary with the words and the keys
    print(word_dict)
    # Now it loops while you want to give a key, input STOP to stop
    while key_input != "STOP":
        # Allows user to input a key
        key_input = input("Enter a key: ")
        
        # Tries to find it in the dictionary 
        try:
            # If it is found then it adds the word associated with the key and
            # adds it to the output message
            str_output += word_dict[key_input] + " "
            
        # If it can't then it checks if the user wanted to stop
        except:
            # Checks if the user wants to stop
            if key_input == "STOP":
                # Prints the output message the user wants
                print(str_output)


main()
