#!/usr/bin/env python3

import unittest

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generator.generator import Generator


class GeneratorTest(unittest.TestCase):

    def setUp(self):
        global g
        g = Generator()


    def test_setup_grid(self):
        g.setup_grid(4, 4)
        target = False
        result = g.grid[3][3]['visited']
        self.assertEqual(result, target)


    def test_add_cell_to_stack(self):
        target = True
        g.setup_grid(4, 4)
        g.add_cell_to_stack(2, 1)
        result = g.grid[2][1]['visited']
        self.assertEqual(result, target)

        target_tuple = (2, 1)
        result_tuple = g.stack[-1]
        self.assertEqual(result_tuple, target_tuple)


    def test_find_unvisited_neighbors(self):
        g.setup_grid(5,5)
        target = [(3,2), (4,3), (3,4), (2, 3)]
        result = g.find_unvisited_neighbors(3, 3)
        self.assertEqual(result, target)



    def test_find_unvisited_neighbords_at_edges_a(self):
        g.setup_grid(5,5)
        target = [(2, 0), (1, 1), (0, 0)]
        result = g.find_unvisited_neighbors(1, 0)
        self.assertEqual(result, target)


    def test_find_unvisited_neighbords_at_edges_b(self):
        g.setup_grid(5,5)
        target = [(0, 0), (1, 1), (0, 2)]
        result = g.find_unvisited_neighbors(0, 1)
        self.assertEqual(result, target)


    def test_find_unvisited_neighbords_at_edges_c(self):
        g.setup_grid(5,5)
        target = [(4, 2), (4, 4), (3, 3)]
        result = g.find_unvisited_neighbors(4, 3)
        self.assertEqual(result, target)


    def test_find_unvisited_neighbords_at_edges_d(self):
        g.setup_grid(5,5)
        target = [(3, 3), (4, 4), (2, 4) ]
        result = g.find_unvisited_neighbors(3, 4)
        self.assertEqual(result, target)


    def test_process_stack_n(self):
        g.setup_grid(5, 5)
        # Set so there is only one unvisited cell
        g.grid[3][4]['visited'] = True
        g.grid[4][3]['visited'] = True
        g.grid[2][3]['visited'] = True
        g.add_cell_to_stack(3, 3)
        g.process_stack()
        target = False
        result = g.grid[3][3]['n']
        self.assertEqual(result, target)

        neighbor_target = False
        neighbor_result = g.grid[3][2]['s']
        self.assertEqual(neighbor_result, neighbor_target)

    def test_process_stack_s(self):
        g.setup_grid(5, 5)
        # Set so there is only one unvisited cell
        g.grid[3][2]['visited'] = True
        g.grid[4][3]['visited'] = True
        g.grid[2][3]['visited'] = True
        g.add_cell_to_stack(3, 3)
        g.process_stack()
        target = False
        result = g.grid[3][3]['s']
        self.assertEqual(result, target)

        neighbor_target = False
        neighbor_result = g.grid[3][4]['n']
        self.assertEqual(neighbor_result, neighbor_target)


    def test_process_stack_e(self):
        g.setup_grid(5, 5)
        # Set so there is only one unvisited cell
        g.grid[3][2]['visited'] = True
        g.grid[3][4]['visited'] = True
        g.grid[4][3]['visited'] = True
        g.add_cell_to_stack(3, 3)
        g.process_stack()
        target = False
        result = g.grid[3][3]['e']
        self.assertEqual(result, target)

        neighbor_target = False
        neighbor_result = g.grid[2][3]['w']
        self.assertEqual(neighbor_result, neighbor_target)


    def test_process_stack_w(self):
        g.setup_grid(5, 5)
        # Set so there is only one unvisited cell
        g.grid[3][2]['visited'] = True
        g.grid[3][4]['visited'] = True
        g.grid[2][3]['visited'] = True
        g.add_cell_to_stack(3, 3)
        g.process_stack()
        target = False
        result = g.grid[3][3]['w']
        self.assertEqual(result, target)

        neighbor_target = False
        neighbor_result = g.grid[4][3]['e']
        self.assertEqual(neighbor_result, neighbor_target)


if __name__ == "__main__":
    unittest.main()


