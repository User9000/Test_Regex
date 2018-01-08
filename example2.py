import re

message = 'Call me 415-555-1011 tomorrow, or 760-444-3434'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#mo = phoneNumRegex.findall(message)
#print(mo.group())
print(phoneNumRegex.findall(message))
