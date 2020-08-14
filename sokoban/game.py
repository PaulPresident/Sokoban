import pygame

from sokoban.generator import Generator
from sokoban.pathfinder import PathFinder

class Game():
    def __init__(self, size:int, nodes:list, character, storage_places:list, boxes:list):
        self.size = size
        self.nodes = nodes
        self.character = character
        self.storage_places = storage_places
        self.boxes = boxes
        self.unstored_boxes = self.boxes[:]
        self.stored_boxes = []

    def create_map(self):
        pathfinder = PathFinder(nodes=self.nodes)

        for node_coor in pathfinder.path():
            for node in self.nodes:
                if node.x == node_coor[0] and node.y == node_coor[1]:
                    node.closed = False
                    node.open = True

    def draw(self, screen):
        for node in self.nodes:
            if node.closed:
                screen.blit(node.wall, (node.x * 60, node.y * 60))
        for box in self.boxes:
            box.draw(screen=screen)
        for storage in self.storage_places:
            storage.draw(screen=screen)

    def check_nodes(self):
        unoccupied_nodes = []
        for node in self.nodes:
            if node.hitbox.colliderect(self.character.hitbox):
                node.closed = False
                node.open = True
                node.occupied = True
            for box in self.boxes:
                if node.hitbox.colliderect(box.hitbox):
                    node.closed = False
                    node.open = True
                    node.occupied = True
                    node.has_box = True
            for storage in self.storage_places:
                if node.hitbox.colliderect(storage.hitbox):
                    node.closed = False
                    node.open = True
                    node.is_storage = True
            if not node.closed or node.has_box:
                unoccupied_nodes.append(node)
        self.character.unoccupied_nodes = unoccupied_nodes
        for box in self.boxes:
            box.unoccupied_nodes = unoccupied_nodes

    def check_stored(self):
        for box in self.unstored_boxes:
            if box.is_stored(self.storage_places):
                self.stored_boxes.append(box)
                self.unstored_boxes.remove(box)

    def win(self):
        self.check_stored()
        if len(self.unstored_boxes) == 0:
            return True
        return False


# TODO figure out sizes
    @classmethod
    def generate(cls):
        generator = Generator(nodes=10, size=60, num_of_boxes=3)
        return cls(
            size=60, nodes=generator.nodes,
            character=generator.generate_character(),
            storage_places=generator.generate_storage_places(),
            boxes=generator.generate_boxes()
        )