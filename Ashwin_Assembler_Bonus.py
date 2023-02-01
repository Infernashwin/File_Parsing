# Name: Ashwin_Assembler_Bonus.py
# Programmer: Ashwin Mayurathan
# Date: Nov 17 2020
# Description: This programs reads a file, and splits words up into groups of
#              2, with one being the key word, and the other one being the
#              associated word and then allows user to input keys to create
#              a message.
def main():
    # Intializes Variables
    word_dict = {}
    file_name = ""
    file_open = ""
    line_read = ""
    key_input = ""
    str_output = ""
    key_word = ""
    associate_word = ""

    #Sets info about the file so we can open it as read
    file_name = "raw_meat_bonus.txt"
    file_open = open(file_name, "r")

    # Sets line read to the file line of the file
    line_read = file_open.readline()

    # Loops until an empty line is found (so it will stop reading the file)
    while line_read != "":
        # Removes the newline character
        line_read =line_read.strip("\n")
        # Turns the line into a list, with each index representing each word
        line_read = line_read.split()
        # Creates a loop for how many words are in the line
        for i in range(len(line_read)):
            # if it is an word in an odd index, make it a non key word, and
            # add it to the list
            if i%2:
                associate_word = line_read[i]
                word_dict[key_word] = associate_word 
            # else it is an even index word, make it a key word
            else:
                key_word = line_read[i]
                
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
