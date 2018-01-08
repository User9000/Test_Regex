import re


area_code = r'(\d\d\d)-(\d\d\d-\d\d\d\d)'

phoneNumRegex = re.compile(area_code)

mo = phoneNumRegex.search('my phone number is 760-620-4572')

print(mo.group())
print(mo.group(1))
print(mo.group(2))


