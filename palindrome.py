def is_palindrome_1(input_str):
    string_length = len(input_str)
    for index in range(0, int(string_length / 2) ):
        if(input_str[index] != input_str[ -(index + 1) ]):
            return False
    return True

def is_palindrome_2(input_str):
  return input_str == input_str[::-1]

if(__name__ == '__main__'):
    print(is_palindrome_1('sample'))
    print(is_palindrome_2('sample'))
    print(is_palindrome_1('malayalam'))
    print(is_palindrome_2('malayalam'))
