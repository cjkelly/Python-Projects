# File: TreeConvert.py
# Description: This program is designed to read in a list of lists representation of a binary tree from a given text file.
#              It converts this binary tree from Python implementation to Linked List implementation. After doing so, it prints
#              the contents of the tree in inorder, preorder, and postorder notation.
# Student's UT EID: cjk673
# Course Name: CS 313E
# Unique Number: 50597
#
# Date Created: 11/15/15
# Date Last Modified: 11/19/15

# Initalize class BinaryTree with three attributes: data, left, and right
class BinaryTree(object):
  def __init__(self, initVal):
    self.data = initVal
    self.left = None
    self.right = None

  # Initialize method getLeftChild that returns the values of the left child of the root node
  def getLeftChild(self):
    return self.left

  # Initialize method getRightChild that returns the values of the right child of the root node
  def getRightChild(self):
    return self.right

  # Initialize method setRootVal that sets the value fo the root node to a given input
  def setRootVal(self, value):
    self.data = value

  # Initialize method getRootVal that returns the value of the root node
  def getRootVal(self):
    return self.data

  # Initialze method insertLeft that inserts a new node as the left child of the root node.
  # If the root node already has a left child, the new node takes on that left child as its own.
  def insertLeft(self, newNode):
    temp = BinaryTree(newNode)
    if self.left == None:
      self.left = temp
    else:
      temp.left = self.left
      self.left = temp

  # Initialze method insertRight that inserts a new node as the right child of the root node.
  # If the root node already has a right child, the new node takes on that right child as its own.
  def insertRight(self, newNode):
    temp = BinaryTree(newNode)
    if self.right == None:
      self.right = temp
    else:
      temp.right = self.right
      self.right = temp

# Initialize function convert that takes a list of lists as an argument and returns a pointer to the root node of
#   a binary tree 
def convert(pyList):
  if pyList[1] == [] and pyList[2] == []:
    baseCase = BinaryTree(pyList[0])
    return baseCase
  else:
    temp = BinaryTree(pyList[0])
    if pyList[1] != []:
      temp.left = convert(pyList[1])
    if pyList[2] != []:
      temp.right = convert(pyList[2])
    return temp

# Initialize function inorder that takes a binary tree as an argument and prints its contents in inorder notation
def inorder(tree):
  treeString = ''
  if tree.left == None and tree.right == None:
    return str(tree.data) + ' '
  else:
    if tree.left != None:
      treeString = treeString + inorder(tree.left)
    treeString = treeString + str(tree.data) + ' '
    if tree.right != None:
      treeString = treeString + inorder(tree.right)
    return treeString

# Initialize function preorder that takes a binary tree as an argument and prints its contents in preorder notation
def preorder(tree):
  treeString = ''
  if tree.left == None and tree.right == None:
    return str(tree.data) + ' '
  else:
    treeString = treeString + str(tree.data) + ' '
    if tree.left != None:
      treeString = treeString + preorder(tree.left)
    if tree.right != None:
      treeString = treeString + preorder(tree.right)
    return treeString

# Initialize funtion postorder that takes a binary tree as an argument and prints it contents in postorder notation
def postorder(tree):
  treeString = ''
  if tree.left == None and tree.right == None:
    return str(tree.data) + ' '
  else:
    if tree.left != None:
      treeString = treeString + preorder(tree.left)
    if tree.right != None:
      treeString = treeString + preorder(tree.right)
    treeString = treeString + str(tree.data) + ' '
    return treeString

def main():
  # Open treedata.txt for reading
  f = open('treedata.txt', 'r')
  lineList = []
  # For each list in treedata.txt
  for line in f:
    # Use eval to convert string to list of lists
    treeList = eval(line)
    # Print the list
    print('list =  ', treeList)
    # Convert from a list of lists to a tree composed of nodes and pointers
    myTree = convert(treeList)
    # Call functions inorder, preorder, and postorder to analyze the tree and print its contents in the required notation
    print('   inorder:     ', inorder(myTree))
    print('   preorder:    ', preorder(myTree))
    print('   postorder:   ', postorder(myTree), '\n')
  f.close()

main()
      
