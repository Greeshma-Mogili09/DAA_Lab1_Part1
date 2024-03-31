def is_palindrome(s):
    if len(s) <= 1:
        return True
    
    first_char = s[0]
    last_char = s[-1]
    if first_char != last_char:
        return False
    
    return is_palindrome(s[1:-1])

input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
