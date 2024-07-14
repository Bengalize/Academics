import time
import random
import csv


# first I write the code for linear search that i got from:
# https://www.geeksforgeeks.org/linear-search-vs-binary-search/ and adjusted a little bit

def linearSearch(array, x):
    for index in range(len(array)):
        if array[index] == x:
            return "Linear, The index is ", index
    return "Item Not Found"


# I found a good resource on binary search on the same page on
# https://www.geeksforgeeks.org/linear-search-vs-binary-search/  which i took inspiration to come with this for binary:

def binarysearch(array, x):
    low = 0  # Because the array starts at index 0
    high = len(array) - 1  # Because the index of the last item in the array is 1 less than the length of the array

    while low <= high:
        # I set mid to take the value of the index at the middle
        mid = (low + high) // 2
        if array[mid] == x:
            return "Binary, The index is :", mid
        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
    return "Item Not found"


def main():
    number_of_trials = 1
    searched_item = random.randint(0, 1000)  # To generate random numbers between 0 and 1000
    min_size = int(input("Please indicate the min_size: "))
    max_size = int(input("Please indicate the max_size: "))
    step_size = int(input("Please indicate the step_size: "))
    num_trial = int(input("Please indicate the number of trial you want for each array size "))

    array_size = range(min_size, max_size, step_size)
    header = ["array_size, search_time"]
    row = []
    Average_time = 0
    Average_time2 = 0

    with open('efficiency.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)

        for trial in range(
                number_of_trials):  # I think I could make this simpler by adjusting properly num_trial but i am not
            # sure how
            for size in array_size:
                for tries in range(num_trial):
                    array = random.sample(range(10000), size)  # https://docs.python.org/3/library/random.html

                    start_time = time.time()  # https://pynative.com/python-get-execution-time-of-program/

                    linearSearch(array, searched_item)

                    end_time = time.time()

                    search_time = (end_time - start_time) * 1000000

                    Average_time = (search_time + Average_time)/num_trial


                    start_time2 = time.time()

                    binarysearch(sorted(array), searched_item)  # Sorted the array with sorted()
                    # https://docs.python.org/3/howto/sorting.html
                    end_time2 = time.time()
                    search_time2 = (end_time2 - start_time2) * 1000000

                    Average_time2 = (search_time2 + Average_time2)
                row.append(size)
                row.append(Average_time/num_trial)
                row.append("\n")
                row.append(size)
                row.append(Average_time2/num_trial)
                row.append("\n")


            # write the data
            writer.writerow(row)
            row = []



main()
