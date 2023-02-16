def find_all_occurrences(str1, str2):
    """
    Function to find all occurrences of str2 in str1 and return their indices as a list.
    If str2 is not present in str1, return -1.
    """
    if str2 not in str1:
        return -1

    indices = []
    start_index = 0
    while True:
        index = str1.find(str2, start_index)
        if index == -1:
            break
        indices.append(index)
        start_index = index + 1

    return indices
# Example usage
string1 = "hello world"
string2 = "o"
indices = find_all_occurrences(string1, string2)
print(indices)  # Output: [4, 7]

string3 = "abc"
string4 = "d"
indices = find_all_occurrences(string3, string4)
print(indices)  # Output: -1
    