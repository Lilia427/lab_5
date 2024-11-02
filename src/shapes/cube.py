from .shape3d import Shape3D

class Cube(Shape3D):
    def get_3d_points(self):
        s = self.size / 2
        return [
            (-s, -s, -s), (s, -s, -s), (s, s, -s), (-s, s, -s),
            (-s, -s, s), (s, -s, s), (s, s, s), (-s, s, s)
        ]