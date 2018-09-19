# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = -2, denominator = 1, return "-2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Given numerator = 5, denominator = 2, return "2.5".

def divide(numerator, denominator): # Using a long division method
    numer = abs(numerator) # Conduct all calculations using positive numbers
    denom = abs(denominator)
    base = numer//denom # Get the base of the quotient (use round since numbers can be negative)
    remainder = numer % denom # Get the remainder of the quotient
    if remainder == 0: # If the numerator divides perfectly into denominator, leave string as is.
        string = [str(base)]
    else: # Executes if remainder exists
        string = [str(base) + '.'] # Take the base and append a decimal
        after_decimal = [numer % denom] # List of all values that appear after the decimal
        while remainder != 0: # Loop to test for repeating values after the decimal
            remainder = remainder * 10 # Algorithm used in long division
            number = remainder // denom
            remainder = remainder % denom
            string.append(str(number))

            if remainder not in after_decimal:
                after_decimal.append(remainder)
            else: # If there is a repeating integer after the decimal
                string.insert(after_decimal.index(remainder)+1, '(') # Find the first instance of the repeating number.
                string.append(')')
                break
    if numerator / denominator < 0: # If the initial quotient was negative, then add a negative sign.
        string.insert(0,'-')
    return ''.join(string) # Return all numbers concatenated together in a string.






