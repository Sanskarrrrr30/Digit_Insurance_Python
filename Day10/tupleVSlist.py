# comparing the size and time taken by tuple and list
import sys
import time

# creating a tuple and a list with the same elements
my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4, 5]

# comparing the size of tuple and list
print("Size of tuple:", sys.getsizeof(my_tuple))
print("Size of list:", sys.getsizeof(my_list))

# comparing the time taken to create a tuple and a list
start_time = time.time()
my_tuple = tuple(range(1000000))
end_time = time.time()
print("Time taken to create a tuple:", end_time - start_time, "seconds")

start_time = time.time()
my_list = list(range(1000000))
end_time = time.time()
print("Time taken to create a list:", end_time - start_time, "seconds")

