from itertools import combinations

def findJuiceMix(juices, caloriesPerJuice, targetCalorieIntake):
    # remove fist element as its not a calorie
    caloriesPerJuice = caloriesPerJuice[1:]
    # print(caloriesPerJuice)
    # print(juices)
    # print(targetCalorieIntake)

    # Create a dictionary to map unique alphabets to numbers in list2
    alphabet_mapping = {char: num for char, num in zip(sorted(set(juices)), caloriesPerJuice)}

    # Expand caloriesPerJuice to the length of juiceNames by mapping values
    caloriesPerJuice = [alphabet_mapping[char] for char in juices]
    # print(caloriesPerJuice)


    # Check if the lengths of juices and caloriesPerJuice are the same
    if len(juices) != len(caloriesPerJuice):
        print("Error: The lengths of 'juices' and 'caloriesPerJuice' must be the same.")
        return

    # Find all combinations of indices
    index_combinations = [comb for i in range(1, len(juices) + 1) for comb in combinations(range(len(juices)), i)]

    # Initialize found_combination as an empty list
    found_combination = []

    # Check each combination
    for indices in index_combinations:
        current_sum = sum(caloriesPerJuice[i] for i in indices)
        if current_sum == targetCalorieIntake:
            found_combination = [juices[i] for i in indices]
            break  # Exit the loop if a successful combination is found

    return ''.join(found_combination)

# Example usage
# findJuiceMix(['a','a','a','b','a','c','b','a','b','c','c'], [3, 4, 5, 6], 15)
