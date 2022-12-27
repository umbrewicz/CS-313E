#  File: LeftSum.py

#  Description: Get the left sum of the BST

#  Student Name: Nick Umbrewicz

#  Student UT EID: nju96

#  Course Name: CS 313E

#  Unique Number: 52520


import sys

class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # ***There is no reason to change anything above this line***
  def get_height (self):
    if self.lchild != None and self.rchild != None:
      return 1 + max(self.lchild.get_height(), self.rchild.get_height())
    
    elif self.lchild != None:
      return 1 + self.lchild.get_height()
    
    elif self.rChild != None:
      return 1 + self.rchild.get_height()
    
    else:
      return 1


  # Returns a list of nodes at a given level from left to right
  def get_level(self, level):
    if self.root == None or level > self.get_height():
        return []

    if level == 0:
        return [self.root]
    
    else:
        list_nodes = []
        current_level = 0
        self.get_level_helper(self.root, current_level, level, list_nodes)

        return list_nodes


  # Recursively builds list_nodes with all nodes on a 
  # given level, which is then returned by get_level()
  def get_level_helper(self, node, current_level, target_level, list_nodes):
    if node == None:
        return node

    if current_level == target_level:
        list_nodes.append(node)

    if node != None:
        current_level += 1
        self.get_level_helper(node.lchild, current_level, target_level, list_nodes)
        self.get_level_helper(node.rchild, current_level, target_level, list_nodes)


  # Returns an integer for the left sum of the BST
  def get_left_sum(self):
    # Base case
    if self.root == None:
        return 0
    
    max_level = [0]
    left_sum = [0]
    self.left_sum_helper(self.root, 1, max_level, left_sum)
    return left_sum[0]


  # Helper function that calculates the left sum
  def left_sum_helper(self, node, level, max_level, left_sum):
    # Base case
    if node == None:
      return
 
    # If this is the first node of its level
    if (max_level[0] < level):
        left_sum[0] += node.data
        max_level[0] = level
 
    # Recur for left and right subtrees
    self.left_sum_helper(node.lchild, level + 1, max_level, left_sum)
    self.left_sum_helper(node.rchild, level + 1, max_level, left_sum)


# ***There is no reason to change anything below this line***

def main():
    # Create tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints

    tree = Tree()
    for i in tree_input:
      tree.insert(i)

    print(tree.get_left_sum())

if __name__ == "__main__":
  main()
