# Original codebase by Rohrbaugh 2021
# Modifications by: Cisse
# Last modified: Mar 14 , 2023

import csv
import random
import time
from datetime import datetime

# replace yourlastname with your actual last name here
STUDENT_LASTNAME = 'Cisse'
VERBOSE_OUTPUT = True

# global constants controlling tests
MIN_SIZE = 32
MAX_SIZE = 512
STEP_SIZE = 32
TRIALS = 20

# global variable used to count steps
step_count = 0
comp_count = 0
swap_count = 0
# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high): #Source: https://www.geeksforgeeks.org/python-program-for-quicksort/
  global swap_count
  global comp_count
	# choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      comp_count +=1
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # Swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  swap_count +=1

  # Return the position from where partition is done
  return i + 1

# function to perform quicksort


def quickSort(array, low, high): #Source: https://www.geeksforgeeks.org/python-program-for-quicksort/
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)





def merge(arr, l, m, r): # Source :https://www.geeksforgeeks.org/python-program-for-merge-sort/
  global comp_count 
  global swap_count

  n1 = m - l + 1
  n2 = r - m

  # create temp arrays
  L = [0] * (n1)
  R = [0] * (n2)

  # Copy data to temp arrays L[] and R[]
  for i in range(0, n1):
    L[i] = arr[l + i]

  for j in range(0, n2):
    R[j] = arr[m + 1 + j]

  # Merge the temp arrays back into arr[l..r]
  i = 0	 # Initial index of first subarray
  j = 0	 # Initial index of second subarray
  k = l	 # Initial index of merged subarray

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
    comp_count +=1
    swap_count +=1 

  # Copy the remaining elements of L[], if there
  # are any
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  # Copy the remaining elements of R[], if there
  # are any
  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted




def mergeSort(arr, low, r):

  if low < r:
		# Same as (l+r)//2, but avoids overflow for
		# large l and h
    m = low+(r-low)//2

		# Sort first and second halves
    mergeSort(arr, low, m)
    mergeSort(arr, m+1, r)
    merge(arr, low, m, r)
  
  return arr

# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

def NearlySorted(array): #Source: ChatGPT
  lenght = len(array)
# 5% of data would be
  k = int(0.05*lenght)
  for i in range(k):
    index1, index2 = random.randint(0, lenght-1), random.randint(0, lenght-1)
    array[index1], array[index2] = array[index2], array[index1]
  return array

def ReverseSorted(array): #Source: https://www.programiz.com/python-programming/methods/list/sort
  array = sorted(array, reverse=True)
  return array


#bubble Sort
def bubble_sort(list):
  # step_count must be declared global here
  # otherwise it would create a new variable
  global comp_count 
  global swap_count

  for i in range(len(list)-1):
    for j in range(len(list)-i-1):
      #step_count += 1
      if list[j] > list[j+1]:
        comp_count += 1
        list[j], list[j+1] = list[j+1], list[j]
        swap_count += 1



# Selection sort : https://www.programiz.com/dsa/selection-sort

def selectionSort(array):
  global comp_count 
  global swap_count
  size = len(array)
  for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
              comp_count += 1
              min_idx = i
              swap_count +=1

         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

# Insertion sort : https://www.programiz.com/dsa/insertion-sort

def insertionSort(array):
  global comp_count 
  global swap_count
  for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
          comp_count += 1
          array[j + 1] = array[j]
          swap_count +=1

          j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
size = len(data)
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


data = [-2, 45, 0, 11, -9]
size1 = len(data)
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

def generate_filename():
  filename = STUDENT_LASTNAME + '_'
  filename += datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
  filename += ".csv"
  return filename





t=0
def console_log(message):
  if VERBOSE_OUTPUT:
    print(message)

def main():
  global step_count
  global comp_count 
  global swap_count
#n
with open(generate_filename(), mode='w') as output_file:
  for l in range(3):
    for i in {bubble_sort, selectionSort, insertionSort, mergeSort, quickSort}:
  
        output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        output_writer.writerow(['algorithm',"initial_configuration",'MIN_SIZE','MAX_SIZE','TRIALS'])
        console_log(f"Testing {i} with {TRIALS} trials on arrays sized {MIN_SIZE} to {MAX_SIZE}")
        if l ==0:
          output_writer.writerow([{i}, "random", MIN_SIZE,MAX_SIZE,TRIALS])
        elif l ==1: 
          output_writer.writerow([{i},"almost sorted", MIN_SIZE,MAX_SIZE,TRIALS])
        else:
          output_writer.writerow([{i},"Reverse sorted", MIN_SIZE,MAX_SIZE,TRIALS])

        output_writer.writerow([])
        output_writer.writerow(['size', 'avg_time', 'avg_comps', 'avg_swaps'])


        size = MIN_SIZE
        while size <= MAX_SIZE:

          sort_time = 0
          sort_steps = 0
          sort_comp = 0
          sort_swaps = 0

          for t in range(TRIALS):
            
              # create a list of size elements with values ranging 0..2*size
              list = random.sample(range(0, int(size*2)), size)
              if l ==1:
                list = NearlySorted(sorted(list))
              elif l == 2:
                list = ReverseSorted(list)

              # record time & reset step_count before sorting
              before_time = time.process_time()
              step_count = 0
              comp_count = 0
              swap_count = 0
              if i == mergeSort:
                i(arr, 0, n-1)
              elif i == quickSort:
                i(data, 0, len(data) - 1)
              else:
                i(list)

              # calculate & record elapsed time & steps
              sort_time += (time.process_time() - before_time) * 1000000
              sort_steps += step_count
              sort_comp += comp_count
              sort_swaps += swap_count

          
              
          console_log(f"size: {size}")

          output_writer.writerow([size, sort_time/TRIALS, sort_comp//TRIALS, sort_swaps//TRIALS])

          size += STEP_SIZE
        output_writer.writerow([])
        output_writer.writerow([])
if __name__ == '__main__':
  main()
