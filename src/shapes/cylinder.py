from .shape3d import Shape3D
import math

class Cylinder(Shape3D):
    def get_3d_points(self):
        points = []
        radius = self.size / 2
        height = self.size
        for i in range(-height // 2, height // 2 + 1, int(height / 10)):
            for angle in range(0, 360, 15):
                theta = math.radians(angle)
                x = radius * math.cos(theta)
                y = radius * math.sin(theta)
                z = i
                points.append((x, y, z))
        return points
