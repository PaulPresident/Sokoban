# import unittest
# from math import sqrt

# from sokoban.generator import Generator
# from sokoban.node import Node

# class GeneratorTest(unittest.TestCase):
#     def test_generates_boxes(self):
#         pass

# nodes = [
#     Node(row, col)
#     for row in range(int(sqrt(25)))
#     for col in range(int(sqrt(25)))
# ]

# generator = Generator(nodes=nodes, size=60)

# print(generator.generate_boxes())