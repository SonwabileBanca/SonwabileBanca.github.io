##Initialise and cast it into list
text = 'Google.com'
new_text = list(text)
print(new_text)
# Create an empty Dictionary and will use it for thr loop
###
text_dict = {}

# A for loop that counts the repeated letters
###
for i in new_text:
  text_key = text_dict.keys()
  # if condition that increase if there is more than one letter
  if i in text_key:
    text_dict[i] += 1
  else:
    text_dict[i] = 1
###
print(text_dict)