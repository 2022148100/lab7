def count_alphabets(file_path):
    # Initialize a dictionary to store the count of each alphabet
    alphabet_count = {chr(i): 0 for i in range(65, 91)}  # A-Z

    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    # Increment the count of the alphabet (considering case-insensitive)
                    alphabet_count[char.upper()] += 1

    # Filter out alphabets with zero count
    alphabet_count = {k: v for k, v in alphabet_count.items() if v > 0}

    # Convert dictionary items to list and sort by count in descending order
    sorted_alphabets = sorted(alphabet_count.items(), key=lambda x: x[1], reverse=True)

    # Extracting only the alphabet characters
    sorted_alphabets = [item[0] for item in sorted_alphabets]

    return sorted_alphabets

# Replace 'file_path' with the path to your input file
file_path = 'input_7_2.txt' 

# Count alphabets and sort them in descending order of their counts
sorted_alphabets = count_alphabets(file_path)

# Printing the sorted list of alphabets
print(sorted_alphabets)
