text = ''

# Open the file 
with open('DOB.txt', 'r+') as f:

  for line in f:
    temp = line.strip() 
    temp = temp.split(' ') # Use temp to split
    print(temp[0],temp[1])
# Open the file again
print("")
with open('DOB.txt', 'r+') as f:
  print('Date of Birth:')
  for loop in f:
    temp = loop.strip()
    temp = temp.split(' ')
    print(temp[2],temp[3],temp[4])
 # print(contents[0])