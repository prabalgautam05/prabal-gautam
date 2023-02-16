def swap_strings(str1, str2, n):
    """
    Function to swap the first n characters of two strings.
    """
    if n <= 0:
        return str1, str2
    elif n >= len(str1) and n >= len(str2):
        return str2, str1
    else:
        return str2[:n] + str1[n:], str1[:n] + str2[n:]

# Example usage
string1 = "Hello, world!"
string2 = "Hi there!"
n = 4

print("Before swapping: ")
print("string1 =", string1)
print("string2 =", string2)

string1, string2 = swap_strings(string1, string2, n)

print("After swapping: ")
print("string1 =", string1)
print("string2 =", string2)
