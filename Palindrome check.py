def is_palindrome(s):
    s = s.lower()
    # removing non-alphanumeric characters
    s = ''.join(c for c in s if c.isalnum())    # used a generator expression
    return s == s[::-1]


string = "12 A man, a plan, a canal: Panama 21!"
print(is_palindrome(string))
