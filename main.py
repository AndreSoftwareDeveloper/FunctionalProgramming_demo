from functions import regex_demo, global_variable_demo

if __name__ == '__main__':
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

    global_variable_demo()
