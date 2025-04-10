import csv
from itertools import zip_longest

# Open the source data file and read its content, skipping the headers
with open("acdH_1_9K.dat", "r", newline="") as source:
    reader = csv.reader(source)
    content = list(reader)[34:]


new_content = []

# Function to check if a value can be converted to a float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# Convert the content of the file into float data, replacing non-float values with 0
for row in content:
    line_float = [float(item) if is_float(item) else 0 for item in row]
    new_content.append(line_float)



# Identify rows where the frequency is 0 and mark them for deletion
to_del = []
for i in range(len(new_content)):
    if new_content[i][15] == 0:
        to_del.append(i)

# Reverse the list of indices to delete rows from the end to avoid index shifting
to_del.reverse()
for i in to_del:
    new_content.pop(i)

# Initialize variables for processing temperature, magnetic field, and data
temperature= []
field = []
data = [[], [], []]
counter = 3

# Process the data to group it based on the 16th column (index 15)
for i in range(1, len(new_content)):
    if new_content[i-1][15] < new_content[i][15]:
        # Append data to the current group
        data[counter-3].append(new_content[i-1][15])
        data[counter-2].append(new_content[i-1][10])
        data[counter-1].append(new_content[i-1][11])

    elif new_content[i-1][15] > new_content[i][15]:
        # Start a new group when the 16th column decreases
        temperature.append(new_content[i-1][2])
        temperature.append(new_content[i-1][2])
        temperature.append(new_content[i-1][2])
        field.append(new_content[i-1][3])
        field.append(new_content[i-1][3])
        field.append(new_content[i-1][3])
        data[counter-3].append(new_content[i-1][15])
        data[counter-2].append(new_content[i-1][10])
        data[counter-1].append(new_content[i-1][11])
        counter += 3
        data += [[], [], []]

# Append the last row's data to the respective lists
temperature.append(new_content[len(new_content)-1][2])
temperature.append(new_content[len(new_content)-1][2])
temperature.append(new_content[len(new_content)-1][2])
field.append(new_content[len(new_content)-1][3])
field.append(new_content[len(new_content)-1][3])
field.append(new_content[len(new_content)-1][3])
data[counter-3].append(new_content[len(new_content)-1][15])
data[counter-2].append(new_content[len(new_content)-1][10])
data[counter-1].append(new_content[len(new_content)-1][11])

# Transpose the data for easier writing to the output file
data_transposed = list(zip_longest(*data))

# Insert temperature and magnetic field data at the beginning of the transposed data
data_transposed.insert(0, tuple(field))
data_transposed.insert(0, tuple(temperature))

# Convert the transposed data into a list of lists for writing
data_final = [list(row) for row in data_transposed]

# Write the processed data to the output file
with open("acdH_1_9K_converted.txt", "+w") as target:
    for line in data_final:
        target.write(" ".join(map(str, line)) + "\n")
