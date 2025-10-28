#The first "Donuts" function
def donuts (count):
    #If count is 10 or more, return 'Number of donuts: many'
    if count >= 10:
        return 'Number of donuts: many'
    #Otherwise, return 'Number of donuts: <count>'
    else:
        return 'Number of donuts: ' + str(count)
#Example usage:
print(donuts(8))   # Output: Number of donuts: 8
print(donuts(23))  # Output: Number of donuts: many


#The second "Both_ends" function
def both_ends(s):
    #If the string length is less than 2, return an empty string
    if len(s) < 2:
        return ''
    #Otherwise, return the first 2 and the last 2 characters of the string
    else:
        return s[:2] + s[-2:]
#Example usage:
print(both_ends('Bekzat'))  # Output: Bzat
print(both_ends('a'))       # Output:

#The third "Fix_start" function
def fix_start(s):
    #Store the first character
    first_char = s[0]
    #Replace all occurrences of the first character in the rest of the string with '*'
    modified_string = first_char + s[1:].replace(first_char, '*')
    return modified_string
#Example usage:
print(fix_start('mammal'))  # Output: ma**al
print(fix_start('gogogo'))  # Output: go*o*o
print(fix_start('hello'))   # Output: hello

#The fourth "Mix_up" function
def mix_up(a, b):
    #Swap the first two characters of each string and concatenate them with a space
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
#Example usage:
print(mix_up('mix', 'pod'))    # Output: pox mid
print(mix_up('dog', 'dinner')) # Output: dig donner
print(mix_up('gnash', 'sport')) # Output: spash gnort
print(mix_up('pezzy', 'firm'))  # Output: fizzy perm


