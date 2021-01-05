'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''


def is_palindrome(string):
    new_str = string.replace(" ", "")

    if new_str[::-1] == new_str:
        return True

    return False


print(is_palindrome("tacocat"))
