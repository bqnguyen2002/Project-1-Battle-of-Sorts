class Linked_List:
   
   class __Node:
      
      def __init__(self, val):
         self.val = val
         self.next = None
         self.prev = None
       # declare and initialize the public attributes
       # for objects of the Node class.
       # TODO replace pass with your implementation

   def __init__(self):
      self.__size = 0
      self.__header = self.__Node(None)
      self.__trailer = self.__Node(None)
      self.__header.next = self.__trailer
      self.__trailer.prev = self.__header
     # declare and initialize the private attributes
     # for objects of the sentineled Linked_List class
     # TODO replace pass with your implementation
     

   def __len__(self):
      return self.__size
     # return the number of value-containing nodes in 
     # this list.
     # TODO replace pass with your implementation

   def append_element(self, val):
      append = Linked_List.__Node(val)
      append.next = self.__trailer 
      append.prev = self.__trailer.prev
      self.__trailer.prev.next = append
      self.__trailer.prev = append
      self.__size += 1
      # increase the size of the list by one, and add a
      # node containing val at the new tail position. this 
      # is the only way to add items at the tail position.
      # TODO replace pass with your implementation

   def insert_element_at(self, val, index):
      insert = Linked_List.__Node(val)
      if index >= len(self) or index < 0:
         raise IndexError 
      cur = self.__header
      for i in range(index):
         cur = cur.next
      insert.next = cur.next
      insert.prev = cur
      cur.next.prev = insert
      cur.next = insert
      self.__size += 1   
      # assuming the head position (not the header node)
      # is indexed 0, add a node containing val at the 
      # specified index. If the index is not a valid 
      # position within the list, raise an IndexError 
      # exception. This method cannot be used to add an 
      # item at the tail position.
      # TODO replace pass with your implementation
     
   def remove_element_at(self, index):
      if index >= len(self) or index < 0:
         raise IndexError
      cur = self.__header
      for i in range(index):
         cur = cur.next
      val = cur.next.val
      cur.next.prev = None
      cur.next.next.prev = cur
      cur.next = cur.next.next
      self.__size -= 1
      return val
      # assuming the head position (not the header node)
      # is indexed 0, remove and return the value stored 
      # in the node at the specified index. If the index 
      # is invalid, raise an IndexError exception.
      # TODO replace pass with your implementation

   def get_element_at(self, index):
      if index >= len(self) or index < 0:
         raise IndexError
      cur = self.__header.next
      for i in range(index):
         cur = cur.next
      return cur.val
      # assuming the head position (not the header node)
      # is indexed 0, return the value stored in the node 
      # at the specified index, but do not unlink it from 
      # the list. If the specified index is invalid, raise 
      # an IndexError exception.
      # TODO replace pass with your implementation

   def rotate_left(self):
      cur = self.__header.next
      self.__header.next.next.prev = self.__header
      self.__header.next = cur.next
      cur.next = None
      cur.prev = None
      cur.next = self.__trailer
      cur.prev = self.__trailer.prev
      self.__trailer.prev.next = cur
      self.__trailer.prev = cur
      # rotate the list left one position. Conceptual indices
      # should all decrease by one, except for the head, which
      # should become the tail. For example, if the list is
      # [ 5, 7, 9, -4 ], this method should alter it to
      # [ 7, 9, -4, 5 ]. This method should modify the list in
      # place and must not return a value.
      # TODO replace pass with your implementation.
     
   def __str__(self):
      if self.__size == 0:
         return '[]'
      list = '[ '
      cur = self.__header
      for i in range(len(self)):
         if i == len(self) - 1:
            list = list + str(cur.next.val) + ' ]'
            break
         list = list + str(cur.next.val) + ', '
         cur = cur.next
      return list
      # return a string representation of the list's
      # contents. An empty list should appear as [ ].
      # A list with one element should appear as [ 5 ].
      # A list with two elements should appear as [ 5, 7 ].
      # You may assume that the values stored inside of the
      # node objects implement the __str__() method, so you
      # call str(val_object) on them to get their string
      # representations.
      # TODO replace pass with your implementation

   def __iter__(self):
      self.__cur = self.__header.next
      # initialize a new attribute for walking through your list
      # TODO insert your initialization code before the return
      # statement. do not modify the return statement.
      return self

   def __next__(self):
      if self.__cur.next == None:
         raise StopIteration
      val = self.__cur.val
      self.__cur = self.__cur.next
      return val
      # using the attribute that you initialized in __iter__(),
      # fetch the next value and return it. If there are no more 
      # values to fetch, raise a StopIteration exception.
      # TODO replace pass with your implementation        

if __name__ == '__main__':
   
   
   
   my_list = Linked_List()
   my_list.append_element(3)
   my_list.append_element(2)
   my_list.append_element(5)
   my_list.append_element(1)
   my_list.append_element(4)
   
   #for k in range(1, len(my_list)):
         #item_to_place = my_list.get_element_at(k)
         #j = k
         #my_list.get_element_at(k)
         #while j > 0 and (my_list.get_element_at(j-1) > item_to_place):
            #j = j - 1
         #if j != k:
            #my_list.insert_element_at(my_list.remove_element_at(k), j)
         #else:
            #continue
            
            
   #for k in range(1, len(my_list)):
      #cur = my_list.get_element_at(k)
      #j = k
      #while j > 0 and my_list.get_element_at(j - 1) > cur:
         #j = j - 1
      #try:
        # my_list.insert_element_at(my_list.remove_element_at(k), j)
      #except:
         #my_list.insert_element_at(my_list.remove_element_at(k), j-1)
         
   #if len(my_list) == 0:
      #raise ValueError
   #current_min = my_list.get_element_at(0)
   #for val in my_list:
      #if val <  current_min:
         #current_min = val 
         
         
   #small = my_list.get_element_at(0)
   #big = my_list.get_element_at(0)
   #for k in range(1, len(my_list)):
      #if my_list.get_element_at(k) < small:
         #small = my_list.get_element_at(k)
      #if my_list.get_element_at(k) > big:
         #big = my_list.get_element_at(k)
   #dif = big - small
   
   
   for k in range(len(my_list) - 1):
      min_loc = k   #the location of the minimum so far
      min_probe = k #the location of a candidate for the new minimum
      while min_probe < len(my_list):
         if my_list.get_element_at(min_probe) < my_list.get_element_at(k):
            min_loc = min_loc + 1
         min_probe = min_probe + 1
      if min_loc != k:  #swap with the minimum
         small = my_list.get_element_at(min_loc)
         my_list.insert_element_at(small, k)
         big = my_list.remove_element_at(min_loc+1)
          
      
   print(my_list)


  
   
    
   # Your test code should go here. Be sure to look at cases
   # when the list is empty, when it has one element, and when 
   # it has several elements. Do the indexed methods raise exceptions
   # when given invalid indices? Do they position items
   # correctly when given valid indices? Does the string
   # representation of your list conform to the specified format?
   # Does removing an element function correctly regardless of that
   # element's location? Does a for loop iterate through your list
   # from head to tail? Your writeup should explain why you chose the
   # test cases. Leave all test cases in your code when submitting.
   # TODO replace pass with your tests