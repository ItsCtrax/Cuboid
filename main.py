from direct.showbase.ShowBase import ShowBase
from map_loader import MapLoader
from player import Player
from camera_control import CameraControl

class CubeGame(ShowBase):
    def __init__(self):
        super().__init__()

        # Загрузка карты
        self.map_loader = MapLoader("level_0")
        self.map_data = self.map_loader.load_level()
        self.map_loader.generate_map(self.map_data, self.render)

        # Создание игрока
        self.player = Player(self.map_data, self.render)

        # Настройка камеры
        self.camera_control = CameraControl(self.player.player)

        # Привязка управления
        self.setup_controls()

    def setup_controls(self):
        self.accept("w", self.player.move, [0, 1])  # Вперед
        self.accept("s", self.player.move, [0, -1])  # Назад
        self.accept("a", self.player.move, [-1, 0])  # Влево
        self.accept("d", self.player.move, [1, 0])  # Вправо

if __name__ == "__main__":
    app = CubeGame()
    app.run()