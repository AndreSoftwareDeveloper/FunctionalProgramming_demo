import re

global global_variable
global_variable = 31


def regex_demo(text):
    pattern = "^merito.*4ever"
    searching_result = re.search(pattern, text)
    return searching_result


def global_variable_demo():
    local_variable = 32

    print(f"This is value of the global variable: {global_variable}")
    print(f"This is value of the local variable: {local_variable}")
