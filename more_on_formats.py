__author__ = 'Brij'
#The code snippets shows more on formats in Python

#decimal (.) precision of 3 for float '0.333'
print ('{0:.3f}'.format(1.0/3))

# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print ('{0:_^11}'.format('hello'))

# keyword-based 'Python is Best'
print ('{lang} is {attri}'.format(lang='Python',attri='Best'))

#To prevent this newline character from being printed, you can end the statement with a comma
print('a'),
print('b')

#'What’s your name?'
print('What’s your name?')

#'This is the first line\nThis is the second line'
print('This is the first line\nThis is the second line')

#Raw String:-no special processing such as escape sequences are handled,by prefixing r or R to the string.
print(r"Newlines are indicated by \n escape sequence not handled")

#you can break it into multiple physical lines by using the backslash. This is referred to as explicit line joining
s = 'This is a string. \
This continues the string.'
print (s)
