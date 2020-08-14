import random

from sokoban.node import Node
from sokoban.character import Character
from sokoban.box import Box
from sokoban.storage import Storage

class Generator():
    def __init__(self, nodes:int, size, num_of_boxes):
        self.nodes_grid = nodes
        self.nodes = [
            Node(row, col, size)
            for row in range(self.nodes_grid)
            for col in range(self.nodes_grid)
        ]
        self.size = size
        self.num_of_boxes = num_of_boxes

    def generate_character(self):
        character_node = self._random_node()
        node = self.nodes[character_node]
        return Character(x=node.x * self.size, y=node.y * self.size)

    def generate_storage_places(self):
        storage_places = []

        while len(storage_places) < self.num_of_boxes:
            node = self.nodes[0]
            while not node.x or not node.y or node.x == self.nodes_grid-1 or node.y == self.nodes_grid-1:
                storage_node = self._random_node()
                node = self.nodes[storage_node]
            # box = Box(x=node.x * self.size, y=node.y * self.size)
            storage_places.append(Storage(x=node.x * self.size, y=node.y * self.size)) # depends on the picture
        return storage_places

    def generate_boxes(self):
        boxes = []

        while len(boxes) < self.num_of_boxes:
            node = self.nodes[0]
            while not node.x or not node.y or node.x == self.nodes_grid-1 or node.y == self.nodes_grid-1:
                box_node = self._random_node()
                node = self.nodes[box_node]
            # box = Box(x=node.x * self.size, y=node.y * self.size)
            boxes.append(Box(x=node.x * self.size + 5, y=node.y * self.size + 5)) # depends on the picture
        return boxes

    def _random_node(self):
        return random.randint(0, len(self.nodes)-1)