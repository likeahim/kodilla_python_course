def is_palindrome(word):
    """
    function is_palindrome
    checks if passed word is a palindrome
    the function ignores case when checking,
    converting all characters to lowercase
    Arguments:
        string
    Return:
        false or true
    """
    return word.lower() == word[::-1].lower()

print(is_palindrome('abba'))
print(is_palindrome('Kajak'))

help(is_palindrome)