#code for palindrome
def is_palindrome(s):
    return s == s[::-1]
# Test the function
if __name__ == "__main__":
    print(is_palindrome("radar"))  # True
    print(is_palindrome("hello"))  # False
