class PathFinder():
    def __init__(self, boxes, storage_places):
        self.boxes = boxes
        self.storage_places = storage_places

    def path(self):
        nodes = []
        pairs = self.box_storage_pairs()
        for pair in pairs:
            box, storage = pair
            if storage.x > box.x:
                for x in range(box.node[0], storage.node[0]):
                    nodes.append((x, box.node[1]))
            else:
                for x in range(storage.node[0], box.node[0]):
                    nodes.append((x, box.node[1]))

            if storage.y > box.y:
                for y in range(box.node[1], storage.node[1]):
                    nodes.append((storage.node[0], y))
            else:
                for y in range(storage.node[1], box.node[1]):
                    nodes.append((storage.node[0], y))

        return nodes

    def box_storage_pairs(self):
        return [
            (box, storage)
            for box in self.boxes
            for storage in self.storage_places
        ]
