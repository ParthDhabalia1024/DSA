# Remove all Adjacent Duplicate Characters Recursively in Python
# Here, on this page, we will learn how to write the program to Remove all Adjacent Duplicate Characters Recursively in Python. 
# programming language. After removing all its adjacent duplicate characters, we are given a string and need to return the string.

# Example :

# Input : str = “acaabbbceddd”
# Output : ae

def removeUtil(string, last_removed):

    if len(string) == 0 or len(string) == 1:
        return string

    if string[0] == string[1]:
        last_removed = ord(string[0])

        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]

        string = string[1:]
        return removeUtil(string, last_removed)

    rem_str = removeUtil(string[1:], last_removed)

    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_removed = ord(string[0])
        return rem_str[1:]

    if len(rem_str) == 0 and last_removed == ord(string[0]):
        return rem_str

    return [string[0]] + rem_str


def remove(string):
    last_removed = 0
    return "".join(removeUtil(list(string), last_removed))


string1 = "acaabbbceddd"
print(remove(string1))