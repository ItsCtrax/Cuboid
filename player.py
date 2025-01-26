from panda3d.core import NodePath
from direct.showbase.ShowBase import ShowBase

class Player:
    def __init__(self, map_data, render):
        self.map_data = map_data
        self.render = render
        self.player = NodePath("player")
        self.create_player()
        self.is_vertical = True  # Вертикальное положение игрока

    def create_player(self):
        start_positions = [tile["pos"] for tile in self.map_data if tile["type"] == "start"]
        if not start_positions:
            raise ValueError("Start block not found! Player cannot be spawned.")

        start_pos = start_positions[0]
        cube = loader.loadModel("cube.egg")
        cube.setScale(0.5, 0.5, 1)  # Размер игрока
        cube.setColor(0, 0, 1, 1)
        cube.reparentTo(self.player)
        self.player.setPos(start_pos[0], start_pos[1], 1.5)
        self.player.reparentTo(self.render)

    def move(self, dx, dy):
        current_pos = self.player.getPos()
        new_x = current_pos.x + dx
        new_y = current_pos.y + dy

        if not self.is_valid_position(new_x, new_y):
            return

        # Логика изменения ориентации
        if dy != 0:  # Движение вперед/назад
            self.is_vertical = True
            self.player.setR(0)  # Вертикальное положение
        elif dx != 0:  # Движение влево/вправо
            self.is_vertical = False
            self.player.setR(90)  # Горизонтальное положение

        self.player.setPos(new_x, new_y, current_pos.z)

    def is_valid_position(self, x, y):
        return any(tile["pos"] == (x, y) for tile in self.map_data)