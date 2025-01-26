from direct.task.Task import Task
from direct.showbase.ShowBaseGlobal import globalClock

class CameraControl:
    def __init__(self, player_node):
        base.disableMouse()
        self.player_node = player_node
        self.zoom_level = 0.37
        base.camera.setPos(25 * self.zoom_level, 5 * self.zoom_level, 15 * self.zoom_level)
        base.camera.setHpr(75, -37, 0)
        taskMgr.add(self.camera_movement, "CameraTask")

    def set_zoom(self, zoom_level):
        self.zoom_level = zoom_level

    def zoom_in(self):
        self.zoom_level *= 0.7

    def zoom_out(self):
        self.zoom_level *= 1.3

    def camera_movement(self, task):
        cube_pos = self.player_node.getPos()
        dt = globalClock.getDt()
        base.camera.setX(base.camera.getX() - (base.camera.getX() - cube_pos.x - 18 * self.zoom_level) * 0.8 * dt)
        base.camera.setY(base.camera.getY() - (base.camera.getY() - cube_pos.y + 5 * self.zoom_level) * 0.8 * dt)
        base.camera.setZ(15 * self.zoom_level)
        return Task.cont