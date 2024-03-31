def reverse_string(s):
    if len(s) <= 1:
        return s
    
    return reverse_string(s[1:]) + s[0]

input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("The reversed string:", reversed_string)
