num_list = input("Enter a list of numbers, separated by spaces: ").split()

# convert the list of strings to a list of integers
num_list = [int(num) for num in num_list]

# create a new list for the cube of even numbers
cubes_of_even_nums = []

# iterate through the list of numbers
for num in num_list:
    if num % 2 == 0:
        cubes_of_even_nums.append(num ** 3)

# print the result
print("The cube of even numbers is: ", cubes_of_even_nums)
