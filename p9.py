def count_frequency(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

def replace_char(string, old_char, new_char):
    
    new_string = ""
    for c in string:
        if c == old_char:
            new_string += new_char
        else:
            new_string += c
    return new_string

def remove_first_occurrence(string, char):

    index = string.find(char)
    if index == -1:
        return string
    else:
        return string[:index] + string[index+1:]

def remove_all_occurrences(string, char):

    return string.replace(char, "")

# Example usage
my_string = input("ENTER THE STRING= ")
print(count_frequency(my_string, 'A'))    # Output: 3
print(replace_char(my_string, 'A', 'z'))  # Output: hezzo worzd
print(remove_first_occurrence(my_string, 'N'))  # Output: hlo world
print(remove_all_occurrences(my_string, 'A'))   # Output: heo word
