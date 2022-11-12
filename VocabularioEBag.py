import sys
import re
import unidecode as uni

def ListCompare(di):
  print(di[1])
  result = []
  for word in di[1]:
    result.append(1 if word in di[2] else 0) 
  return result

def SelectWords(words):
  select = set()
  addSet = select.add
  select = [x for x in words if not (x in select or addSet(x))]
  return list(select)

def ProcessWords(listWords):
  words = []
  for word in listWords:
    result = ((uni.unidecode(word)).lower()).split()
    words = [y for x in [result, words] for y in x]
  return sorted(words)

def OpenArq(arq):
  with open(arq, "r") as doc:
    lines = doc.readlines()
  return lines

arg = sys.argv
i = 1
dictList = dict()

while(i < len(arg)):
  doc = OpenArq(arg[i])
  
  words = ProcessWords(doc)
  listWords = SelectWords(words)
  dictList[i] = listWords
  print("\n")
  print(dictList)
  i = i + 1	
result = ListCompare(dictList)
print(result)
