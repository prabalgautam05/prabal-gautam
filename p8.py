def num_to_words(num):
    """Converts a numeric digit into words."""
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    num=int(num)
    if num == 0:
        return "zero"

    words = ""
    
    if num // 1000 > 0:
        words += num_to_words(num // 1000) + " thousand "
        num %= 1000

    if num // 100 > 0:
        words += ones[num // 100] + " hundred "
        num %= 100

    if num >= 10 and num <= 19:
        words += teens[num - 10]
    else:
        if num >= 20:
            words += tens[num // 10] + " "
            num %= 10
        words += ones[num]

    return words.strip()


num= input("enter any character= ")
if (
    num.isalpha()) and (num.islower()):
    print("THE CHARCTER IS ALPHABET AND IS LOWERCASE")
elif(
    num.isalpha()) and (num.isupper()):
    print("THE CHARACTER ENTERED IS ALPHABET AND UPPERCASE")
elif(
    num.isdigit()):
    print((num_to_words(num)))
else:
    print("THE CHARACTER ENTERED IS SPECIAL CHACTER")                    