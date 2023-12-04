class Planet:
    AU = 149.6e6 * 1000
    G = 6.67408e-11
    SCALE = 250 / AU  # 1 pixel = 250 km | 1 AU = 100 pixels
    TIMESTEP = 3600 * 24  # 1 day = 1 second

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.vel_x = 0
        self.vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2