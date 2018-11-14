import json
import re

# Function to get words from json file
def load_words():
  with open('words.json', 'r') as f:
    return json.load(f)


words = load_words()

print("Length = {} ", len(words)) #Print number of words


# I Assume only upside down numbers can be used i.e. 0123456789 and
# muliplication symbol X
# So the only letters I allow will be OGBSHEIXL
goodLetters = r'^[ogbsheixl]+$'
longestAcceptableWord = ''


for word in words:
  if len(word) <= len(longestAcceptableWord):
    continue

  if re.search(goodLetters, word):
    longestAcceptableWord = word


print("The Longest Word to fit is: {}".format(longestAcceptableWord))
