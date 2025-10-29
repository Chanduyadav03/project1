#single-quoted strings
sin_quo = 'hello, world!'

#string operations with single-quoted strings
length =len(sin_quo)
upper_case =sin_quo.upper()
lower_case = sin_quo.lower()
contains_substring = "world!" in sin_quo

print("length of sin_quo",length)
print("upper version:-",upper_case)
print("lower version:-",lower_case)
print("contains 'hello world!'",contains_substring)