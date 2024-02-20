import math
from functions import regex_demo, global_variable_demo, return_even_numbers, predefined_functions_demo, \
    function_as_argument, filter_demo, square_power, add_5, apply_functions

if __name__ == '__main__':
    predefined_functions_demo()
    global_variable_demo()
    print("\nNow the function has been passed as an argument!")
    function_as_argument(global_variable_demo, 58)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_numbers = return_even_numbers(numbers)
    print("\nEven numbers:")
    for even_number in even_numbers:
        print(even_number)

    word_list = ["admin", "debug", "python", "asembler"]
    filtered_word_list = filter_demo(word_list)
    print("\nWords starting with a:")
    for word in filtered_word_list:
        print(word)

    print("Powers of numbers:")
    numbers_pow2 = map(lambda x: pow(x, 2), numbers)
    for number in numbers_pow2:
        print(number)

    function_list = [square_power, add_5]
    altered_value = apply_functions(function_list, 8)
    print(f"\nAltered value: {altered_value}")

    square_numbers = [pow(x, 2) for x in range(1, 11)]
    print("\nSquare numbers:")
    for number in square_numbers:
        print(number)

    print("\nWord list:")
    for word in word_list:
        print(word)

    words_lenghts = [ len(word) for word in word_list ]
    print("\nLengths of these words:")
    for length in words_lenghts:
        print(length)