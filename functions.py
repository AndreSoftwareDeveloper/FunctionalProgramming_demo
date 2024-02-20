import re

global global_variable
global_variable = 31


def predefined_functions_demo():
    x = input('Enter string:')
    print(f"The string is of type: {type(x)}\n"
          f"Minimal ASCII code: {min(x)}\n"
          f"Maximal ASCII code: {max(x)}\n"
          f"Length of the string: {len(x)}")

    text = "merito gdansk 4ever"
    text_match = regex_demo(text)
    print(f"The text is: {text}")
    if text_match:
        print("Match found!")
    else:
        print("Match not found!")


def regex_demo(text):
    pattern = "^merito.*4ever"
    searching_result = re.search(pattern, text)
    return searching_result


def global_variable_demo(additional=0):
    local_variable = 32

    print(f"This is value of the global variable: {global_variable}")
    print(f"This is value of the local variable: {local_variable}")
    print(additional)


def function_as_argument(function, argument):
    return function(argument)


def return_even_numbers(numbers_array):
    even_numbers = []
    for number in numbers_array:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def filter_demo(word_list):
    starting_with_a = filter(check_if_word_starts_with_lettter, word_list)
    return starting_with_a


def check_if_word_starts_with_lettter(word_list):
    if word_list[0] == 'a':
        return True
    return False

def square_power(number):
    return number ** 2

def add_5(number):
    return number + 5

def apply_functions(function_list, value):
    value = function_list[0](value)
    value = function_list[1](value)
    return value