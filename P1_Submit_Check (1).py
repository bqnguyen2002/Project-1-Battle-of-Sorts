import sys

try:
  from Sort import insertion_sort, selection_sort
except ImportError:
  print("The grading environment is unable to locate your Sort.py or the expected functions contained within it. You should fix this before submitting.")
  sys.exit(1)
  
if __name__ == '__main__':
  iarr1 = [3]

  sarr1 = [3]
  
  try:
    insertion_sort(iarr1)
    selection_sort(sarr1)
  except:
    print("The grading environment encountered a crash when executing your sorting functions. You should fix this before submitting.")
    sys.exit(2)
  print("If this is the only output you see, then our grading program should be able to access your functions.")
