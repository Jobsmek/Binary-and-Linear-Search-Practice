''' ++++++++++++++++++++++++++++++
    Binary Search
    Author: Job Wosmek
    ++++++++++++++++++++++++++++++
'''
# import packages for time functions and random numbers
import time
from numpy import random

''' Function to do linear search of key'''
# def linear_search(numbers, key):
#     for i in range(len(numbers)):
#         if numbers[i] == key:
#              return i
#     return -1  # not found

''' Binary Search '''
# The binary search def is named linear_search so I can easily comment out and compare lineara and binary
def linear_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1


''' Create a random array of unsorted values '''
def create_random_array(array_size):
    random_nums = random.randint(9999999, size=(array_size))
    #random_nums.sort()
    return random_nums

''' Create a random array of sorted values '''
def create_random_sorted_array(array_size):
    random_nums = random.randint(9999999, size=(array_size))
    random_nums.sort()
    return random_nums

''' Prompts the user and creates Sorted and Unsorted lists '''
size = input("Enter a size for the array to sort: ")
#size = 20000000
random_nums = create_random_array(int(size))
random_nums_sorted = create_random_sorted_array(int(size))

#Number of times to run                                      
numTimes = 10

''' Unsorted list '''
# tot_toc = 0
# for i in range(0,numTimes):
#    key = random_nums[random.randint(int(size),size=1)]
# #    key = -1
#    ''' Time the function as it performs the linear search '''
#    tic = time.perf_counter()
#    linear_search(random_nums, key)
#    toc = time.perf_counter()
#    tot_toc += (toc-tic)
   
#    print(f"The time taken to complete linear search was {toc-tic:0.4f} seconds ")

# avg_time = tot_toc / numTimes
# print(f"The average time take to complete linear search was {avg_time:0.4f} seconds ")
# print("Unsorted run completed.\n\n")


''' Sorted list '''
tot_toc = 0
for i in range(0,numTimes):
    #Change This Key to -1 to test for worst case
    key = random_nums_sorted[random.randint(int(size),size=1)]
    # key = -1
    ''' Time the function as it performs the linear search '''
    tic = time.perf_counter()
    linear_search(random_nums_sorted, key)
    toc = time.perf_counter()
    tot_toc += (toc-tic)
    
    print(f"The time taken to complete linear search was {toc-tic:0.4f} seconds ")

avg_time = tot_toc / numTimes
print(f"The average time take to complete linear search was {avg_time:0.4f} seconds ")
print("Sorted run completed.\n\n")
