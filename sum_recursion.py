# task 26
import time
#sum_rec
num = [1, 4, 6, 7, 8, 9, 12, 13]

# Define Fibonacci sequence by the sum of two new numbers
def sum_recursion(index):

  if index <= 1:
    return index
  else:
    return sum_recursion(index - 1) + sum_recursion(index - 2)


print('========Recursion=========')
rec_time = time.time()
# print out the results

num = int(input('What number do you want to index'))

print(sum_recursion(num))

