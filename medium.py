def one():
    """
    Write a program that finds the largest element in a given list using a for loop.
    """
    print("\nmedium.one:")

    numbers = [4, 12, 7, 30, 18, 25]

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    
    print("\t", f"largest number = {largest}")

def two():
    """
    Write a program that calculates the average of a list of numbers using a while loop. You are not allowed to use the built-in `sum()` function.
    """
    print("\nmedium.two:")

    numbers = [82, 90, 76, 88, 94]

    total = 0
    i = 0

    while i < len(numbers):
        total = total + numbers[i]
        i = i + 1

    average = total / len(numbers)

    print("\t", f"average = {average}")

def three():
    """
    3. Write a program that checks if a given string is a palindrome using a for loop. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, e.g. `radar`, `level`, `12321`, `mom`, `noon`, `civic`, `deified`, `racecar`, `madam`, `refer`, `repaper`, `rotor`, `sagas`, `solos`, `stats`, `tenet`, `wow`, ...
    """
    print("\nmedium.three:")

    text = "racecar"

    is_palindrome = True

    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            is_palindrome = False
    
    if is_palindrome:
        print("\t", f'"{text}" is a palindrome')
    else:
        print("\t", f'"{text}" is not a palindrome')

def four():
    """
    Write a program that prints the first _n_ terms of the geometric sequence using a while loop. A geometric sequence is a sequence of numbers in which each term after the first is found by multiplying the previous term by a fixed, non-zero number called the common ratio, e.g. `2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...`, where the common ratio is `2`.
    """
    print("\nmedium.four:")

    n = 10
    term = 2
    ratio = 2
    counter = 0

    print("\t", end="")

    while counter < n:
        print(term, end="")

        counter = counter + 1
        term = term * ratio

        if counter < n:
            print(", ", end="")
    
    print()

def five(number):
    """
    Write a program that finds the second largest element in a given list using a for loop.
    """
    print("\nmedium.five:")

    numbers = [14, 8, number, 3, 19, 25, 11]

    largest = numbers[0]
    second_largest = numbers[0]

    for value in numbers:
        if value > largest:
            second_largest = largest
            largest = value
        elif value > second_largest and value != largest:
            second_largest = value
    
    print("\t", f"second largest number = {second_largest}")


def six(number):
    """
    Write a program that calculates the factorial of a given number using a while loop.
    """
    print("\nmedium.six: ")

    product = 1
    i = number

    while i > 0: 
        product = product * i
        i = i - 1

    print("\t", f"{number} factorial = {product}")

    
def seven():
    """
    7. Write a program that checks if a given number is a perfect square using a for loop. A perfect square is a number that can be expressed as the product of two equal integers, e.g. `1`, `4`, `9`, `16`, `25`, `36`, `49`, `64`, `81`, `100`, ...
    """
    print("\nmedium.seven:")

    number = 64
    is_perfect_square = False

    for i in range(1, number + 1):
        if i * i == number:
            is_perfect_square = True

    if is_perfect_square:
        print("\t", f"{number} is a perfect square")
    else:
        print("\t", f"{number} is not a perfect square")

def eight(number):
    """
    8. Write a program that prints the sum of all prime numbers between 1 and 100 using a while loop.
    """
    print("\nmedium.eight:")

    total = 0
    current_number = 2
    while current_number <= 100:

        is_prime = True
        divisor = current_number - 1

        while divisor > 1:
            if current_number % divisor == 0:
                is_prime = False
            divisor = divisor - 1

        if is_prime:
            total = total + current_number

        current_number = current_number + 1

    print("\t", f"sum of all prime numbers between 1 and 100 = {total}")

def nine():
    """
    9. Write a program that counts the number of words in a given sentence using a for loop. Words can be separated by spaces, commas, periods, exclamation marks, question marks, etc. You may be interested in the built-in `split()` function, which splits a string into a list of words based on a delimiter. The delimiter is a space by default, but you can specify a different delimiter, e.g. `split(',')`, `split('.')`, `split('!')`, `split('?')`, etc. You can even specify multiple delimiters, e.g. `split(',.!?')`.
    """
    print("\nmedium.nine: ")
    sentence = "Hello, world! This is a test."

    sentence = sentence.replace(",", " ")
    sentence = sentence.replace(".", " ")
    sentence = sentence.replace("!", " ")
    sentence = sentence.replace("?", " ")

    words = sentence.split()

    count = 0

    for word in words:
        count = count + 1

    print("\t", f"number of words = {count}")

def ten():
    """
    10. Write a program that prints the common elements between two lists using a while loop.
    """
    print("\nmedium.ten:")

    first_list = [3, 6, 9, 12, 15]
    second_list = [4, 6, 8, 12, 16]

    i = 0

    print("\t", end="")

    while i < len(first_list):
        if first_list[i] in second_list:
            print(first_list[i], end=" ")

        i = i + 1
    
    print()

