#!/usr/bin/env python3

import json

from string import Template

json_data = None


with open('template_display.html') as _tmpl:
    chrome = Template(_tmpl.read())

with open('maze.json') as _json:
    json_data = json.load(_json)

output = []

output_size = (len(json_data['grid']) * 2) + 1

for i in range(0, output_size):
    output.append(['.'] * output_size)

for row_index, row in enumerate(json_data['grid']):
    for cell_index, cell in enumerate(row):
        x_plus = (row_index * 2) + 1
        y_plus = (cell_index * 2) + 1
        # print(f"{row_index} - {cell_index} - {x_plus} - {y_plus}")

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
        if cell == '.':
            output_rows = ''
            for r_index, r in enumerate(output):
                output_rows += '<tr>'
                for c_index, c in enumerate(r):
                    x_plus = row_index + 1
                    y_plus = cell_index + 1
                    x_minus = row_index - 1
                    y_minus = cell_index - 1
                    if output[r_index][c_index] == 'x':
                        output_rows += f'<td width="26" height="26" bgcolor="#000000">&nbsp;</td>'
                    else:
                        if r_index == row_index and c_index == cell_index:
                            output_rows += '<td align="center"><font color="#048531">&block;</font></td>'
                        elif r_index == 15 and c_index == 15:
                            output_rows += f'<td align="center"><font color="#ff6666">$</font></td>'
                        elif r_index == x_plus and c_index == cell_index and output[x_plus][cell_index] != 'x':
                            output_rows += f'<td align="center"><a href="{x_plus}x{cell_index}.html"><font color="#449999">v</font></a></td>'
                        elif r_index == x_minus and c_index == cell_index and output[x_minus][cell_index] != 'x':
                            output_rows += f'<td align="center"><a href="{x_minus}x{c_index}.html"><font color="#449999">^</font></a></td>'
                        elif r_index == row_index and c_index == y_plus and output[r_index][y_plus] != 'x':
                            output_rows += f'<td align="center"><a href="{r_index}x{y_plus}.html"><font color="#449999">&gt;</font></a></td>'
                        elif r_index == row_index and c_index == y_minus and output[r_index][y_minus] != 'x':
                            output_rows += f'<td align="center"><a href="{r_index}x{y_minus}.html"><font color="#449999">&lt;</font></a></td>'
                        else:
                            output_rows += f"<td></td>"
                output_rows += '</tr>'

            if row_index == 14 and cell_index == 15:
                # Don't overwrite the manual ending screen
                pass
            else:
                with open(f'../../../site/positions/{row_index}x{cell_index}.html', 'w') as _pos:
                    _pos.write(chrome.substitute(rows=output_rows))

        print(f"{cell}", end="")
    print()



