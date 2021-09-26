#[Python Regular Expression Operations](https://docs.python.org/3/library/re.html)
import re

str = "on the internet you can learn programming and also help others to learn"
word = "internet"

def findWord(word, str):
  content = re.findall(word, str)
  print(content)
  
  
findWord(word, content)

####################################################

# [Output]: ['internet']
