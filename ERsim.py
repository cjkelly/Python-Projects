# File: ERsim.py
# Description: This program is designed to simulate an Emergency Room where patients are admitted and assesed for their injury status.
#                 Patients are read into the program via a text file and are assigned either 'Critical', 'Serious', or 'Fair' for their
#                 status. When the file dictates that a patient be treated, patients are treated in order of status importance.
# Student's Name: Connor Kelly
# Student's UT EID: cjk673
# Course Name: CS 313E
# Unique Number: 50597
#
# Date Created: 10/23/15
# Date Last Modified: 10/29/15

# Initialize class Queue as a child of class Object
class Queue(object):

  # Set initial value of queue to an empty list
  def __init__(self):
    self.items = []

  # If self.queue is empty, return True
  def isEmpty(self):
    return self.items == []

  # Insert item at back of queue
  def enqueue(self, item):
    self.items.insert(0, item)

  # Take item of front of queue and return it
  def dequeue(self):
    return self.items.pop()

  # Return the length of self.items as the size of the queue
  def size(self):
    return len(self.items)

  # Look at the item in the front of the queue without removing it
  def peek(self):
    return self.items[-1]

  # Initialize __str__ method that returns a str value of self.items for printing
  def __str__(self):
    return str(self.items)

# Define function printQueues to print the current state of all queues when called
def printQueues(splitList, critical, serious, fair):
  print('Queues are: \
         \nCritical: ', critical, '\
         \nSerious:  ', serious, '\
         \nFair:     ', fair, '\n')

# Define function treatPatient to treat the next patient in order of status or inform user if queues are empty
def treatPatient(splitList, critical, serious, fair):
  
  if critical.isEmpty() and serious.isEmpty() and fair.isEmpty():
    print('No patients in queue\n')

  elif critical.isEmpty():

    if serious.isEmpty():
      print('Treating', fair.dequeue(), 'from Fair queue')
      printQueues(splitList, critical, serious, fair)

    else:
      print('Treating', serious.dequeue(), 'from Serious queue')
      printQueues(splitList, critical, serious, fair)
            
  else:
    print('Treating', critical.dequeue(), 'from Critical queue')
    printQueues(splitList, critical, serious, fair)

def main():

  # Open ERsim.txt for reading
  f = open('ERsim.txt', 'r')

  lineList = []

  # Apend each line in f to lineList
  for line in f:
    lineList.append(line)

  f.close()

  # Initialize each queue for patients of various statuses 
  fair = Queue()
  serious = Queue()
  critical = Queue()

  # For each line in lineList, iterate over the patient or tratment command in that line
  for i in range(len(lineList)):
    # Strip \n and split the line into splitList
    lineList[i].strip()
    splitList = lineList[i].split()

    # If add, enqueue patient to appropriate queue
    if splitList[0] == 'add':
      
      if splitList[2] == 'Critical':
        critical.enqueue(splitList[1])
        
      elif splitList[2] == 'Serious':
        serious.enqueue(splitList[1])
        
      elif splitList[2] == 'Fair':
        fair.enqueue(splitList[1])

      # Inform user of action, print current state of queues  
      print('Add patient', splitList[1], 'to', splitList[2], 'queue')
      printQueues(splitList, critical, serious, fair)

    # If treatment command, check if 'next' or 'all'
    elif splitList[0] == 'treat':

      # If 'next' call treatPatient once
      if splitList[1] == 'next':
        print('Treat next patient \n')
    
        treatPatient(splitList, critical, serious, fair)

      # If 'all' count how many patients left and call treatPatient that many times
      elif splitList[1] == 'all':
        print('Treating all patients  \n')

        count = critical.size() + serious.size() + fair.size()

        for i in range(count):
          treatPatient(splitList, critical, serious, fair)

    # Once the end of file is reached, print Exit
    elif splitList[0] == 'exit':
      print('Exit')
  

main()
