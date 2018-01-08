import re

namesRegex = re.compile(r'Agent (\w)\w*')
text1 = 'Agent Alice gave the secret documents to Agent Bob'
print(namesRegex.findall(text1))
#The sub function will replaced the word 'REDACTED for ever Agent <name>
#print(namesRegex.sub('REDACTED', text1))



