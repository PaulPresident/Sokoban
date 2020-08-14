class PathFinder():
    def __init__(self, nodes):
        self.nodes = nodes
        self.boxes = [node for node in self.nodes if node.has_box]
        self.storage_places = [node for node in self.nodes if node.is_storage]

    def path(self):
        nodes = []
        pairs = self.box_storage_pairs()
        for pair in pairs:
            box, storage = pair
            if storage.x > box.x:
                for x in range(box.x, storage.x):
                    nodes.append((x, box.y))
            else:
                for x in range(storage.x, box.x):
                    nodes.append((x, box.y))

            if storage.y > box.y:
                for y in range(box.y, storage.y):
                    nodes.append((storage.x, y))
            else:
                for y in range(storage.y, box.y):
                    nodes.append((storage.x, y))

        return nodes

    def box_storage_pairs(self):
        return [
            (box, storage)
            for box in self.boxes
            for storage in self.storage_places
        ]
