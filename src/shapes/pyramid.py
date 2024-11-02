from .shape3d import Shape3D

class Pyramid(Shape3D):
    def get_3d_points(self):
        s = self.size / 2
        return [
            (0, 0, s), (-s, -s, -s), (s, -s, -s), (s, s, -s), (-s, s, -s)
        ]
