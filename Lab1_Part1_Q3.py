def string_to_integer(string):
    if not string:
        return 0    
    first_digit = ord(string[0]) - ord('0')
    remaining_value = string_to_integer(string[1:])
    
    return first_digit * (10 ** len(string[1:])) + remaining_value

input_string = input("Enter a string of digits: ")
integer_representation = string_to_integer(input_string)
print("The integer representation:", integer_representation)
