def one():
    """
    1. Write a program that finds the prime factors of a given number using a for loop. A prime factor is a prime number that divides another number exactly without leaving a remainder, e.g. the prime factors of `12` are `2` and `3`.
    """
    print("\ndifficult.one:")

    number = 12
    prime_factors = []

    for possible_factor in range(2, number + 1):

        if number % possible_factor == 0:

            is_prime = True

            for divisor in range(2, possible_factor):
                if possible_factor % divisor == 0:
                    is_prime = False

            if is_prime:
                prime_factors.append(possible_factor)

    print("\t", f"prime factors of {number} = {prime_factors}")

def two():
    """
    2. Write a program that calculates the `n`th term of the Fibonacci sequence using a while loop.
    """
    print("\ndifficult.two:")

    n = 8

    first = 0
    second = 1
    counter = 1

    while counter < n:
        next_number = first + second
        first = second
        second = next_number
        counter = counter + 1

    print("\t", f"term number {n} in the Fibonacci sequence = {first}")

def three():
    """
    3. Write a program that checks if a given string is an anagram using a for loop.
    """
    print("\ndifficult.three:")

    first_text = "listen"
    second_text = "silent"
    first_text = first_text.lower()
    second_text = second_text.lower()
    second_letters = []

    for character in second_text:
        second_letters.append(character)

    is_anagram = True

    if len(first_text) != len(second_text):
        is_anagram = False
    else:
        for character in first_text:
            if character in second_letters:
                second_letters.remove(character)
            else:
                is_anagram = False

    if is_anagram:
        print("\t", f'"{first_text}" and "{second_text}" are anagrams')
    else:
        print("\t", f'"{first_text}" and "{second_text}" are not anagrams')

def four():
    """
    4. Write a program that prints the first `n` terms of the arithmetic sequence using a while loop. An arithmetic sequence is a sequence of numbers in which each term after the first is found by adding a fixed, non-zero number called the common difference to the previous term, e.g. `2, 4, 6, 8, 10, 12, 14, 16, 18, 20, ...`, where the common difference is `2`.
    """
    print("\ndifficult.four:")
    
    n = 10
    term = 2
    difference = 2
    counter = 0

    print("\t", end="")
    
    while counter < n:
        print(term, end="")

        counter = counter + 1
        term = term + difference

        if counter < n:
            print(", ", end="")

    print()

def five(number):
    """
    5. Write a program that finds the median of a given list of numbers using a for loop. The median is the middle value of a list of numbers when they are sorted in ascending order. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
    """
    print("\ndifficult.five:")

    numbers = [12, 4, number, 18, 2, 30]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[i]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

    length = len(numbers)

    if length % 2 == 1:
        middle_index = int(length / 2)
        median = numbers[middle_index]
    else:
        right_middle_index = int(length / 2)
        left_middle_index = right_middle_index - 1
        median = (numbers[left_middle_index] + numbers[right_middle_index]) / 2

    print("\t", f"sorted list = {numbers}")
    print("\t", f"median = {median}")


def six(number):
    """
    6. Write a program that checks if a given number is a perfect number using a while loop. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself, e.g. `6` is a perfect number because `1 + 2 + 3 = 6`.
    """
    print("\ndifficult.six:")

    total = 0
    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            total = total + divisor

        divisor = divisor + 1

    if total == number:
        print("\t", f"{number} is a perfect number")
    else:
        print("\t", f"{number} is not a perfect number")

def seven():
    """
    7. Write a program that prints the sum of all digits in a given number using a for loop. For example, the sum of the digits in `12345` is `1 + 2 + 3 + 4 + 5 = 15`.
    """
    print("\ndifficult.seven:")

    number = 12345
    number_as_string = str(number)

    total = 0

    for digit in number_as_string:
        total = total + int(digit)

    print("\t", f"sum of the digits in {number} = {total}")

def eight(number):
    """
    8. Write a program that finds the longest word in a given sentence using a while loop.
    """
    print("\ndifficult.eight:")

    sentence = "The small turtle walked around the classroom."

    sentence = sentence.replace(".", " ")
    sentence = sentence.replace(",", " ")
    sentence = sentence.replace("!", " ")
    sentence = sentence.replace("?", " ")

    words = sentence.split()

    longest_word = words[0]

    i = 0

    while i < len(words):
        if len(words[i]) > len(longest_word):
            longest_word = words[i]

        i = i + 1

    print("\t", f"longest word = {longest_word}")

def nine():
    """
    9. Write a program that checks if a given string is a pangram using a for loop. A pangram is a sentence that contains every letter of the alphabet at least once, e.g. `The quick brown fox jumps over the lazy dog`.
    """
    print("\ndifficult.nine:")

    text = "The quick brown fox jumps over the lazy dog"
    text = text.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    is_pangram = True

    for letter in alphabet:
        if letter not in text:
            is_pangram = False

    if is_pangram:
        print("\t", f'"{text}" is a pangram')
    else:
        print("\t", f'"{text}" is not a pangram')

def ten():
    """
    10. Write a program that prints the prime numbers between 1 and 1000 using a while loop.
    """
    print("\ndifficult.ten:")

    current_number = 2

    print("\t", end="")

    while current_number <= 1000:

        is_prime = True
        divisor = current_number - 1

        while divisor > 1:
            if current_number % divisor == 0:
                is_prime = False

            divisor = divisor - 1

        if is_prime:
            print(current_number, end=" ")

        current_number = current_number + 1
    
    print()

