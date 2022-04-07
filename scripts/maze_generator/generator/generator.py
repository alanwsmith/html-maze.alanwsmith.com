#!/usr/bin/env python3

import json

from random import randint
from string import Template

class Generator():

    def __init__(self):
        self.grid = []
        self.stack = []

    def add_cell_to_stack(self, x, y):
        self.stack.append((x, y))
        self.grid[x][y]['visited'] = True

    def find_unvisited_neighbors(self, x, y):
        cells = []

        x_plus = x + 1
        y_plus = y + 1
        x_minus = x - 1
        y_minus = y - 1

        if y_minus >= 0 and self.grid[x][y_minus]['visited'] == False:
            cells.append((x, y_minus))
        if x_plus < len(self.grid) and self.grid[x_plus][y]['visited'] == False:
            cells.append((x_plus, y))
        if y_plus < len(self.grid[x]) and self.grid[x][y_plus]['visited'] == False:
            cells.append((x, y_plus))
        if x_minus >= 0 and self.grid[x_minus][y]['visited'] == False:
            cells.append((x_minus, y))
        return cells

    def setup_grid(self, x,y):
        for x_index in range(0, x):
            row = []
            for y_index in range(0, y):
                row.append({
                    "visited": False,
                    "n": True,
                    "s": True,
                    "e": True,
                    "w": True
                })
            self.grid.append(row)

    def process_stack(self):
        current_cell = self.stack.pop()
        unvisited_neighbors = self.find_unvisited_neighbors(current_cell[0], current_cell[1])
        if len(unvisited_neighbors) > 0:
            # TODO Make this a random seletion 
            neighbor_cell = unvisited_neighbors[randint(0, len(unvisited_neighbors) - 1)]
            print(f"{current_cell} - {neighbor_cell}")
            self.start_point = neighbor_cell

            if neighbor_cell[0] < current_cell[0]:
                self.grid[current_cell[0]][current_cell[1]]['n'] = False
                self.grid[neighbor_cell[0]][neighbor_cell[1]]['s'] = False

            if neighbor_cell[0] > current_cell[0]:
                self.grid[current_cell[0]][current_cell[1]]['s'] = False
                self.grid[neighbor_cell[0]][neighbor_cell[1]]['n'] = False

            if neighbor_cell[1] < current_cell[1]:
                self.grid[current_cell[0]][current_cell[1]]['w'] = False
                self.grid[neighbor_cell[0]][neighbor_cell[1]]['e'] = False

            if neighbor_cell[1] > current_cell[1]:
                self.grid[current_cell[0]][current_cell[1]]['e'] = False
                self.grid[neighbor_cell[0]][neighbor_cell[1]]['w'] = False

            self.add_cell_to_stack(current_cell[0], current_cell[1])
            self.add_cell_to_stack(neighbor_cell[0], neighbor_cell[1])


if __name__ == "__main__":


    g = Generator()
    g.end_point = (0,0)
    g.setup_grid(3, 3)
    g.add_cell_to_stack(g.end_point[0], g.end_point[1])
    while len(g.stack) > 0:
        g.process_stack()

    rows = []
    for row in g.grid:
        cells = []
        for cell in row:
            cell_string = '<td style="'
            if cell['n'] == True:
                cell_string += 'border-top: 1px solid black;'
            if cell['s'] == True:
                cell_string += 'border-bottom: 1px solid black;'
            if cell['e'] == True:
                cell_string += 'border-right: 1px solid black;'
            if cell['w'] == True:
                cell_string += 'border-left: 1px solid black;'
            cell_string += '"></td>'
            cells.append(cell_string)

        rows.append("".join(cells))


    with open("template.html") as _tmpl:
        skeleton = Template(_tmpl.read())
        with open("index.html", "w") as _out:
            _out.write(skeleton.substitute(
                rows = "</tr><tr>".join(rows)
            ))
    print(g.grid)


    json_data = {
        "end_point": g.end_point,
        "grid": g.grid,
        "start_point": g.start_point
    }

    with open("maze.json", "w") as _json:
        json.dump(json_data, _json, sort_keys=True, indent=2, default=str)

