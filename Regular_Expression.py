''' 
A regular expression specifies a set of strings that matches it, the functions in this module let us check if a particular string matches a given regular expression.
'''


# 1.) 

sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())

# Output : (‘we’, ‘are’, ‘humans’)

# 2.)
sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.groupdict())

# Output : {‘animal’: ‘horses’, ‘verb’: ‘are’, ‘adjective’: ‘fast’}

# 3.) 
p = re.compile("d")
p.search("door")

# Output : p = re.subn()


# 4.)
import re
re.ASCII

# Output : 256

# 5.)
re.split('[a-c]', '0a3B6', re.I)

# Output : [‘0’, ‘3B6’]
