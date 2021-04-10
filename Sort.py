import timeit
import random

def generate_inc(num): #produces an array of size (num) in increasing order (1, 2, 3, ...)
   arr= [None] * num
   for i in range(1, num + 1):
      arr[i - 1] = i
   return arr
   
def generate_dec(num): #returns an array of size (num) in decreasing order (5, 4, 3, ...)
   arr= [None] * num
   count = 0
   for i in range(num, 0, -1):
      arr[count] = i
      count += 1
   return arr
   
def generate_rand(num): #returns an array of size (num) in random order (4, 9, 0, ...)
   arr = [None] * num
   for i in range(num):
      arr[i] = (random.randrange(1, num))
   return arr
   
def insertion_sort(arr): #reorders array in increasing order using insertion sort
   for k in range(1, len(arr)):
      cur = arr[k]
      j = k
      while j > 0 and arr[j-1] > cur:
         arr[j] = arr[j-1]
         j = j - 1
      arr[j] = cur

def selection_sort(arr): #reorders array in increasing order using selection sort
   for cur in range(0, len(arr) - 1): #ranges from 0 to second to last element (last element doesn't need to be iterated through because it will always be the greatest value)
      j = cur + 1 #index for used for comparison starts at the index after cur 
      min_index = cur #set min_index to cur as the starting point for each traversal 
      while j < len(arr): #traverse to the end of the array
         if arr[min_index] > arr[j]: #checks to see if the value after it is smaller than the value at min_index 
            min_index = j #if value at j is smaller than value at min_index, value at j becomes the new value at min_index
         j = j + 1 #used to iterate through the whole array
      arr[min_index], arr[cur] = arr[cur], arr[min_index] #swaps the minimum value with the current value

      
if __name__ == '__main__':
   
   length = [1000, 2500, 5000, 7500, 10000] 
   arr = [[0 for y in range(6)] for x in range(5)] #stores all 30 times in a 5 X 6 2D array with each row representing the lengths in the order (1000, 2500, 5000, 7500, 10000) and each column representing the sorting method / type of array in the order of (inc_insertion, dec_insertion, rand_insertion, inc_selection, dec_selection, rand_selection) 
   times = [[0 for y in range(6)] for x in range(5)] #stores all 30 times in a 5 X 6 2D array with each row representing the lengths in the order (1000, 2500, 5000, 7500, 10000) and each column representing the sorting method / type of array in the order of (inc_insertion, dec_insertion, rand_insertion, inc_selection, dec_selection, rand_selection) 

   i = 0
   for r in range(5):
      arr[r][0] = generate_inc(length[i]) #represents increasing array that is going to be sorted using insertion sort for the 5 different lengths
      arr[r][1] = generate_dec(length[i]) #represents decreasing array that is going to be sorted using insertion sort for the 5 different lengths
      arr[r][2] = generate_rand(length[i]) #represents random array that is going to be sorted using insertion sort for the 5 different lengths
      arr[r][3] = generate_inc(length[i]) #represents decreasing array that is going to be sorted using insertion sort for the 5 different lengths
      arr[r][4] = generate_dec(length[i]) #represents random array that is going to be sorted using insertion sort for the 5 different lengths
      arr[r][5] = arr[r][2].copy() #represents random array that is going to be sorted using selection sort for the 5 different lengths
      i += 1
      
   for r in range(5): #times each element(how long it takes to sort (insertion/selection) an increasing, decreasing, or random array of differing lengths) in arr and stores them in the same corresponding spot in the times array
      arr_to_sort = arr[r][0]
      times[r][0] = timeit.timeit('insertion_sort(arr_to_sort)', \
         setup='from __main__ import insertion_sort, arr_to_sort', \
         number=1)
       
      arr_to_sort = arr[r][1]
      times[r][1] = timeit.timeit('insertion_sort(arr_to_sort)', \
         setup='from __main__ import insertion_sort, arr_to_sort', \
         number=1) 
      
      arr_to_sort = arr[r][2]
      times[r][2] = timeit.timeit('insertion_sort(arr_to_sort)', \
         setup='from __main__ import insertion_sort, arr_to_sort', \
         number=1) 
      
      arr_to_sort = arr[r][3]
      times[r][3] = timeit.timeit('selection_sort(arr_to_sort)', \
         setup='from __main__ import selection_sort, arr_to_sort', \
         number=1)
      
      arr_to_sort = arr[r][4]
      times[r][4] = timeit.timeit('selection_sort(arr_to_sort)', \
         setup='from __main__ import selection_sort, arr_to_sort', \
         number=1)
      
      arr_to_sort = arr[r][5]
      times[r][5] = timeit.timeit('selection_sort(arr_to_sort)', \
         setup='from __main__ import selection_sort, arr_to_sort', \
         number=1) 
   
   for r in range(5): #reformats all elements in the times array to 6 decimal places
      for c in range(6):
         times[r][c] = '{:.6f}'.format(times[r][c]) 

   print('Five Increasing Insertion:', [col[0] for col in times])
   print('Five Decreasing Insertion:', [col[1] for col in times])
   print('Five Random Insertion:', [col[2] for col in times])
   print('Five Increasing Selection:', [col[3] for col in times])
   print('Five Decreasing Selection:', [col[4] for col in times])
   print('Five Random Selection:', [col[5] for col in times])