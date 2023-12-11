def print_values_of(dictionary, keys):
  for key in keys:
    if key in dictionary:
      print(dictionary[key])


# Key with values as catch frases
simpson_catch_phrases = {
    "lisa": "BAAAAAART!",
    "bart": "Eat My Shorts!",
    "marge": "Mmm~mmmmm",
    "homer": "d'oh",
    "maggie": "(Pacifier Suck)"
}
# A list for keys
keys_to_print = ['lisa', 'bart', 'homer']
# Call the function with the three keys as a second argument
print_values_of(simpson_catch_phrases, keys_to_print)