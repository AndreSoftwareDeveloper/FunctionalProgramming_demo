if __name__ == '__main__':
      x = input('Enter string:')
      print(f"The string is of type: {type(x)}\n"
            f"Minimal ASCII code: {min(x)}\n"
            f"Maximal ASCII code: {max(x)}\n"
            f"Length of the string: {len(x)}")