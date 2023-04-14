def is_palindrome(s):
    s = s.lower()
    # removing non-alphanumeric characters
    s = ''.join(c for c in s if c.isalnum())    # used a generator expression
    return s == s[::-1]


string = "1A man, a plan, a canal: Panama1!"
print(is_palindrome(string))
