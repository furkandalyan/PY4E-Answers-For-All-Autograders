filename = 'mbox-short.txt'

# Create a dictionary to store the counts for each hour
hour_counts = dict()

# Open the file and read line by line
with open(filename, 'r') as file:
    for line in file:
        if line.startswith('From '):
            # Split the line and extract the time portion
            words = line.split()
            time = words[5]
            
            # Split the time using a colon to get the hour
            hour = time.split(':')[0]
            
            # Update the count in the dictionary
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Sort the dictionary by hour
sorted_hour_counts = sorted(hour_counts.items())

# Print the result
for hour, count in sorted_hour_counts:
    print('{hour} {count}')
