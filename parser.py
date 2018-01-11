
import re
#DNF
#Regular Expressions
issue1 = r'''

<b> Here is some bold text </b>
<a> Another Tag </a>

'''
#dataParser = re.compile(r'\<\w\>(\w+)* \<\/\w\>')
dataParser = re.compile(r'\<\w\>(.*)<\/\w\>')
print(dataParser.findall(issue1))





