import csv
from itertools import zip_longest

with open("BDS_data.txt", "r", newline="") as source:
    reader = csv.reader(source)
    content= list(reader)[3:]



# Convert the content of the file into float data
data = []
for row in content:
    row = row[0].split("\t")
    line_float = []
    for item in row:
        if item.split(" "):
            line_float.append(float(item))
        else:
            line_float.append(0)
    data.append(line_float)

#Pars the data and store it in the modulus list
temperature = []
modulus = [[], [], []]
column_counter = 3

for i in range(1, len(data)):
    if data[i - 1][0] > data[i][0]:
        modulus[column_counter - 3].append(data[i - 1][0])
        modulus[column_counter - 2].append(data[i - 1][2])
        modulus[column_counter - 1].append(data[i - 1][3])
    elif data[i - 1][0] < data[i][0]:
        temperature.extend([data[i - 1][1]] * 3)
        modulus[column_counter - 3].append(data[i - 1][0])
        modulus[column_counter - 2].append(data[i - 1][2])
        modulus[column_counter - 1].append(data[i - 1][3])
        column_counter += 3
        modulus += [[], [], []]

# Store the last data
temperature.extend([data[-1][1]] * 3)
modulus[column_counter - 3].append(data[-1][0])
modulus[column_counter - 2].append(data[-1][2])
modulus[column_counter - 1].append(data[-1][3])


# Transpose the matrix and insert temperature
modulus_transposed = [list(row) for row in zip_longest(*modulus, fillvalue=0)]
modulus_transposed.insert(0, tuple(temperature))
modulus_final = [list(row) for row in modulus_transposed]

# Export data to file
with open("BDS_data_converted.txt", "w") as target:
    for line in modulus_final:
        target.write(" ".join(map(str, line)) + "\n")