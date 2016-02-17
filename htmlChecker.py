# File: htmlChecker.py
# Description: This program is designed to read a file of html code and pull out each 'tag' into a list. It then iterates through that
#                 list and determines if the tags are all appropriately matched and ordered (much like paretheses) using a stack object.
# Student's Name: Connor Kelly
# Student's UT EID: cjk673
# Course Name: CS 313E
# Unique Number: 50597
#
# Date Created: 10/20/15
# Date Last Modified: 10/23/15

# Initialize class Stack as an object
class Stack(object):
  
  # Set initial value for stack as an empty list
  def __init__(self):
    self.items = []
  
  # Initialize push method to add item to top of stack (a.k.a. the end of the list)
  def push(self, item):
    self.items.append(item)

  # Initialize pop method to return the top value on the stack and remove it from the stack 
  def pop(self):
    return self.items.pop()

  # Initialize peek method to return the top value of the stack without removing it
  def peek(self):
    return self.items[-1]

  # Iitialize isEmpty method to return boolean value based on if the list has any contents
  def isEmpty(self):
    return self.items == []

  # Initialize size method to return the size of the stack
  def size(self):
    return len(self.items)
  # Initialize __str__ method that returns a printable str for the self.items list
  def __str__(self):
    return str(self.items)

# Define function getTag that returns a a list of tags contained within htmlfile.txt
def getTag():
  # Open htmlfile.txt and create lists tagList and lineList
  file = open('htmlfile.txt', 'r')
  tagList = []
  lineList = []

  # Append each line in file to lineList
  for line in file:
    lineList.append(line)

  # Loop over each line in lineList
  for i in range(len(lineList)):
    # Loop over each character in a line
    for j in range(len(lineList[i])):

      # If the current character is '<', start recording the tag
      if lineList[i][j] == '<':
        tag = ''
        count = 1
        marker = lineList[i][j + count]
        # While loop creates tag until end of tag conditions are met
        while marker != ' ' and marker != '>' and marker != '':
          tag = tag + marker
          count += 1
          marker = lineList[i][j + count]
        # Append each tag to tagList
        tagList.append(tag)
      
  # Close file and return the list of tags
  file.close()
  return tagList

def main():

  # Run getTag function to return the list of tags
  tagList = getTag()

  # Initialize tagStack
  tagStack = Stack()
  error = False
  counter = 0
  # Set a list of exception tags that do not need a match
  exceptionsList = ['meta', 'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'param', 'source', \
                    'track', 'wbr']

  # Iterate over each tag in tagList
  while counter < len(tagList) and not error:

    # If the tag is an exception, do not add it to stack, print appropriate message 
    if tagList[counter] in exceptionsList:
      print('Tag is ', tagList[counter], ': does not need to match: stack is now ', tagStack)

    else:
      # If the first character of the tag is not '/)' (i.e. it is not an end tag, push the tag on the stack
      if tagList[counter][0] != '/':
        tagStack.push(tagList[counter])
        print('Tag is ', tagList[counter], ': pushed: stack is now ', tagStack)

      # If it is not and end tag and it matches the top of the stack, pop the top of the stack
      #   and print the apropriate message for matching tags
      elif tagList[counter][0] == '/' and tagList[counter][1:] == tagStack.peek():
        tagStack.pop()
        print('Tag is ', tagList[counter], ': matches: stack is now ', tagStack)

      # If the tag is an end tag and it does not match the top of the stack, set error to True and print message for non-matches
      elif tagList[counter][0] == '/' and tagList[counter][1:] != tagStack.peek():
        error = True
        print('Error: tag is ', tagList[counter], 'but top of stack is ', tagStack.peek())

    counter += 1

  # Print appropriate message for stack conditions once the tagList has been iterated through completely
  if tagStack.size() == 0:
    print('Processing complete. No mismatches found.')
  else:
    print('Processing complete. Unmatched tags remain on stack: ', tagStack) 

main()
  
  
