class MapLoader:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_level(self):
        level_data = []
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    elements = line.strip().split("><")
                    for element in elements:
                        if element.startswith("<"):
                            element = element[1:]
                        if element.endswith(">"):
                            element = element[:-1]

                        if not element or "=" not in element:
                            continue

                        type_and_pos = dict(item.split("=") for item in element.split(","))
                        pos = tuple(map(int, type_and_pos["Pos"].split("_")))
                        level_data.append({"type": type_and_pos["Type"], "pos": pos})
        except FileNotFoundError:
            print(f"Level file {self.file_name} not found!")
        return level_data

    def generate_map(self, map_data, render):
        for tile_data in map_data:
            block_type = tile_data["type"]
            x, y = tile_data["pos"]
            self.create_block(x, y, block_type, render)

    def create_block(self, x, y, block_type, render):
        block = loader.loadModel("cube.egg")
        block.setScale(0.5)
        block.setPos(x, y, 0)

        if block_type == "tile":
            block.setColor(1, 1, 1, 1)
        elif block_type == "start":
            block.setColor(0, 1, 0, 1)
        elif block_type == "goal":
            block.setColor(1, 0, 0, 1)
        else:
            block.setColor(0.5, 0.5, 0.5, 1)

        block.reparentTo(render)