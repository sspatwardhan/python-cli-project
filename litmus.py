juiceNameSequence = "Apple123Orange"
filtered_characters = filter(str.isalpha, juiceNameSequence.lower())
print(filtered_characters)
result_string = ''.join(filtered_characters)
print(result_string)
