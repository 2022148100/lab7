import re

# Function to find function declarations and calls in a Python file
def find_function_declarations_and_calls(file_path):
    func_decl_pattern = r"def\s+(\w+)\("
    func_call_pattern = r"(\w+)\("

    declarations = []
    calls = []

    with open(file_path, 'r') as file:
        for i, line in enumerate(file, start=1):
            if re.search(func_decl_pattern, line):
                declarations.append((i, line.strip()))
            elif re.search(func_call_pattern, line):
                calls.append((i, line.strip()))

    return declarations, calls


# Function to organize the output
def organize_output(declarations, calls):
    output = {}
    for line_num, decl in declarations:
        func_name = decl.split()[1].split('(')[0]
        output[func_name] = {"def": line_num, "calls": []}

    for line_num, call in calls:
        for func_name in output:
            if re.search(fr"\b{func_name}\(", call):
                output[func_name]["calls"].append(line_num)

    return output

# Path to the input file
file_path = 'input_7_1.txt'

# Find function declarations and calls
declarations, calls = find_function_declarations_and_calls(file_path)

# Organize the output
organized_output = organize_output(declarations, calls)

# Displaying the organized output
for func_name, details in organized_output.items():
    print(f"{func_name}: def in {details['def']}, calls in {details['calls']}")
