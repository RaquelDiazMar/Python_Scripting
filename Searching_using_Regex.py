#[regular expressions 101](https://regex101.com/)
#[Python RegEx](https://www.w3schools.com/python/python_regex.asp)

import re

content = "on the internet you can learn programming and also help others to learn either how to program or else"
word = "prog\w*"

def findWord(word, str):
  content = re.findall(word, str)
  print(content)
  
  
findWord(word, content)

##################################################################################################################

#Output = ['programming', 'program']
