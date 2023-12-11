# Create a empty list to store the floats
num_list = []
# loop in range of 0 to 10
for i in range(1, 11):
  # add the float after i as an input
  float_num = i + float(input('Enter a float'))
  num_list.append(float_num)

print(f'These are the float and numbers on your list\n{num_list}.')

#Total, minimum and maximun of the list
print(sum(num_list))

### index the first and last float
##
#Use 0 for first and -1 for last
#
print('This is the first float on the list.\t',num_list[0])
print('This is the last float on the list.\t',num_list[-1])
###
#average
print(sum(num_list)//10)
#median
print((min(num_list)+max(num_list))//2)