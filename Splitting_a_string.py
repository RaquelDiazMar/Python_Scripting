import re

content = "on the internet you can learn programming and also help others to learn"
word = "\s" #whitespace character for Unicode & 8-bit patterns

def splitStr(word, str):
  content = re.split(word, str)
  print(content)
  
  
splitStr(word, content)

#####################################################################################

#Output = ['on', 'the', 'internet', 'you', 'can', 'learn', 'programming', 'and', 'also', 'help', 'others', 'to', 'learn']

