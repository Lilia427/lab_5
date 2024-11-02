from .shape3d import Shape3D
import math

class Sphere(Shape3D):
    def get_3d_points(self):
        points = []
        for i in range(0, 180, 20):
            for j in range(0, 360, 20):
                theta = math.radians(i)
                phi = math.radians(j)
                x = self.size * math.sin(theta) * math.cos(phi)
                y = self.size * math.sin(theta) * math.sin(phi)
                z = self.size * math.cos(theta)
                points.append((x, y, z))
        return points
