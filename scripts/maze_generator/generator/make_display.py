#!/usr/bin/env python3

import json

json_data = None

with open('maze.json') as _json:
    json_data = json.load(_json)

output = []

output_size = 7

for i in range(0, output_size):
    output.append(['.'] * output_size)

for row_index, row in enumerate(json_data['grid']):
    for cell_index, cell in enumerate(row):
        x_plus = (row_index * 2) + 1
        y_plus = (cell_index * 2) + 1
        print(f"{row_index} - {cell_index} - {x_plus} - {y_plus}")

        if cell["n"] == True:
            output[x_plus - 1][y_plus] = 'x'
            output[x_plus - 1][y_plus + 1] = 'x'
            output[x_plus - 1][y_plus - 1] = 'x'

        if cell["s"] == True:
            output[x_plus + 1][y_plus] = 'x'
            output[x_plus + 1][y_plus + 1] = 'x'
            output[x_plus + 1][y_plus - 1] = 'x'

        if cell["e"] == True:
            output[x_plus][y_plus + 1] = 'x'
            output[x_plus - 1][y_plus + 1] = 'x'
            output[x_plus + 1][y_plus + 1] = 'x'

        if cell["w"] == True:
            output[x_plus][y_plus - 1] = 'x'
            output[x_plus - 1][y_plus - 1] = 'x'
            output[x_plus + 1][y_plus - 1] = 'x'

for row_index, row in enumerate(output):
    for cell_index, cell in enumerate(row):
        print(f"{cell}", end="")
    print()
