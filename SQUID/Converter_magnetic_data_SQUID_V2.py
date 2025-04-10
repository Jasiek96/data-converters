import csv
from itertools import zip_longest

# Open the input data file and read its content, skipping the headers
with open("ac_dc.dat", "r", newline="") as source:
    reader = csv.reader(source)
    content = list(reader)[28:]

# Process the content to convert strings to floats and handle empty values
new_content = []
for row in content:
    line_float = []
    for item in row:
        if item:
            line_float.append(float(item))
        else:
            line_float.append(0)
    new_content.append(line_float)

# Initialize variables to store temperature, magnetic field, and data
temperatura = []
pole = []
data = [[], [], []]
counter = 3

# Process the data to group and organize it based on specific conditions
for i in range(1, len(new_content)):
    if new_content[i-1][26] < new_content[i][26]:
        data[counter-3].append(new_content[i-1][26])
        data[counter-2].append(new_content[i-1][21])
        data[counter-1].append(new_content[i-1][23])
    elif new_content[i-1][26] > new_content[i][26]:
        temperatura.append(new_content[i-1][2])
        temperatura.append(new_content[i-1][2])
        temperatura.append(new_content[i-1][2])
        pole.append(new_content[i-1][3])
        pole.append(new_content[i-1][3])
        pole.append(new_content[i-1][3])
        data[counter-3].append(new_content[i-1][26])
        data[counter-2].append(new_content[i-1][21])
        data[counter-1].append(new_content[i-1][23])
        counter += 3
        data += [[], [], []]

# Append the last set of temperature, magnetic field, and data
temperatura.append(new_content[len(new_content)-1][2])
temperatura.append(new_content[len(new_content)-1][2])
temperatura.append(new_content[len(new_content)-1][2])
pole.append(new_content[len(new_content)-1][3])
pole.append(new_content[len(new_content)-1][3])
pole.append(new_content[len(new_content)-1][3])
data[counter-3].append(new_content[len(new_content)-1][26])
data[counter-2].append(new_content[len(new_content)-1][21])
data[counter-1].append(new_content[len(new_content)-1][23])

# Transpose the data and prepare it for writing to the output file
data_transposed = list(zip_longest(*data))
data_transposed.insert(0, tuple(pole))
data_transposed.insert(0, tuple(temperatura))  
data_final = [list(row) for row in data_transposed]

# Write the processed data to the output file
with open("ac_dc_converted.txt", "w") as target:
    for line in data_final:
        target.write(" ".join(map(str, line)) + "\n")