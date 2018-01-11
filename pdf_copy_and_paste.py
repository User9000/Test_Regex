#! python3
import re, pyperclip
#todo: Create a regex for phone numbers
# 415-555-0000, 555-0000, (415) 555-0000, ext 1234, ext. 12345 , x12345
phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))? # area code ( optional) '\' <- literal
(\s|-)                     # first separator 
\d\d\d                     # first 3 digits
-                          # separator
\d\d\d\d                   # last 4 digits
(((ext(\.)?\s)| x )        # extension word part (optional)
(\d{2,5}))?                # extension number part (optional)
)
''', re.VERBOSE) #Verbose allows to write as programming language
#todo: create a regex for email addresses
#some.+_thing@something.com
emailRegex = re.compile(r''' 
[a-zA-Z0-9_.+]+ #name part, CUSTOM [], no need to use '\' literal
@               # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)
#todo: extract the email/phone from this text
text = pyperclip.paste()
#todo:Copy the extracted email/phone to the clipboard
extracted_phones = phoneRegex.findall(text)
extracted_email = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extracted_phones:
    allPhoneNumbers.append(phoneNumber[0])
results = '\n'.join(allPhoneNumbers) +  "\n" +'\n'.join(extracted_email)

pyperclip.copy(results)
print(allPhoneNumbers)
print(extracted_email)