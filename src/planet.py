import math
import pygame


class Planet:
    def __init__(self, planet_data, config):
        self.x = planet_data["x"]
        self.y = planet_data["y"]
        self.radius = planet_data["radius"]
        self.color = tuple(planet_data["color"])
        self.mass = planet_data["mass"]

        self.config = config

        self.orbit = []
        self.sun = planet_data.get("sun", False)
        self.distance_to_sun = 0

        self.x_vel = planet_data.get("x_vel", 0)
        self.y_vel = planet_data.get("y_vel", 0)

    def draw(self, win):
        x = self.x * self.config["scale"] + self.config["width"] / 2
        y = self.y * self.config["scale"] + self.config["height"] / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                orbit_x, orbit_y = point
                orbit_x = orbit_x * self.config["scale"] + self.config["width"] / 2
                orbit_y = orbit_y * self.config["scale"] + self.config["height"] / 2
                updated_points.append((orbit_x, orbit_y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        # Draw the planet
        pygame.draw.circle(win, self.color, (int(x), int(y)), self.radius)

        # Display the distance to the sun if the planet is not the sun
        if not self.sun:
            distance_text = self.config["font"].render(
                f"{round(self.distance_to_sun / 1000, 1)}km",
                1,
                self.config["text_color"],
            )
            win.blit(
                distance_text,
                (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2),
            )

    def attraction(self, other):
        pass

    def update_position(self, planets):
        pass
