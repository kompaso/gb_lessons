import numpy as np
import math
import time
import sys

# terminal_args = sys.argv
# print(terminal_args)
input_range = int(sys.argv[1])
print(input_range)
our_demo_list = []
for i in range(input_range):
    our_demo_list.append((i**3 + 7)/3)

our_demo_list_array = np.array(our_demo_list)
start = time.time()
result_for_list = list(map(math.sqrt, our_demo_list))
end = time.time()
print('List ', end - start)

if sys.argv[2] == 'greetings':
    print('Hello!')
    sys.exit(0)

start = time.time()
result_demo_list_array = np.sqrt(our_demo_list_array)
end = time.time()
print('Array ', end - start)

