import re

def sum_integers_from_file(file_path):
    # Open the file and read its content
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expression to find all integers in the content
    integers = re.findall(r'\b[0-9]+\b', content)

    # Convert the extracted strings to integers and sum them up
    total_sum = sum(map(int, integers))

    return total_sum

# Replace 'your_file_path.txt' with the actual path of your file
file_path = 'denemetx.md'
result = sum_integers_from_file(file_path)

print("Sum from the actual data:", result)
