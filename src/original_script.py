import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (200, 200, 200)
YELLOW = (255, 174, 66)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
GREEN = (0, 255, 0)
DARK_GRAY = (80, 78, 81)

FONT = pygame.font.SysFont("comicsans", 16)


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

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        """
        Draw the celestial body and its orbit on the Pygame window.

        Parameters:
        win (Pygame Surface): The window or surface on which the celestial body and its orbit will be drawn.

        Note:
        This method assumes that the celestial body has attributes like x, y for position,
        SCALE for scaling the position values, WIDTH and HEIGHT for the dimensions of the window,
        an orbit list to track the trajectory, a color attribute for the body's color,
        a radius for its size, and a boolean attribute sun to determine if the body is a sun.
        """

        # Scale and translate the position of the celestial body for the Pygame window
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        # Check if there are enough points to draw the orbit
        if len(self.orbit) > 2:
            updated_points = []
            # Scale and translate each point in the orbit for the Pygame window
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            # Draw the orbit lines on the window
            pygame.draw.lines(win, self.color, False, updated_points, 2)

        # Draw the celestial body as a circle on the window
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        # If the celestial body is not the sun, draw the distance to the sun
        if not self.sun:
            # Render the distance text
            distance_text = FONT.render(
                f"{round(self.distance_to_sun / 1000, 1)}km", 1, GREEN
            )
            # Place the text on the window, centered on the celestial body
            win.blit(
                distance_text,
                (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2),
            )

    def attraction(self, other):
        """
        Calculate the gravitational force exerted by 'other' on the instance 'self'.

        Parameters:
        other (SomeClass): Another object of the same class, representing a celestial body.

        Returns:
        tuple: A tuple containing the x and y components of the gravitational force.

        Note:
        This method assumes a 2D space and uses Newton's law of universal gravitation.
        """

        # Extract the position of the 'other' object.
        other_x, other_y = other.x, other.y

        # Calculate the difference in position between 'self' and 'other' along x and y axes.
        distance_x = other_x - self.x
        distance_y = other_y - self.y

        # Calculate the Euclidean distance between 'self' and 'other'.
        distance = math.sqrt(distance_x**2 + distance_y**2)

        # If 'other' is a sun, store the distance to it.
        # This is likely specific to the simulation's context, possibly tracking distance to a central body.
        if other.sun:
            self.distance_to_sun = distance

        # Calculate the gravitational force.
        # Newton's law: F = G * (m1 * m2) / r^2
        # where G is the gravitational constant, m1 and m2 are the masses, and r is the distance.
        force = self.G * self.mass * other.mass / distance**2

        # Calculate the angle (theta) of the force in radians.
        # This is the angle between the line connecting 'self' and 'other' and the horizontal axis.
        theta = math.atan2(distance_y, distance_x)

        # Decompose the force into its x and y components.
        # This uses trigonometry, where force_x is the adjacent side
        # and force_y is the opposite side of the right-angled triangle formed.
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        # Return the x and y components of the force.
        return force_x, force_y

    def update_position(self, planets):
        """
        Update the position of the current celestial body based on the gravitational
        forces exerted by other celestial bodies in the 'planets' list.

        Parameters:
        planets (list): A list of celestial body objects, which may include planets, stars, etc.

        Note:
        This method assumes that each object in the 'planets' list, including 'self',
        has attributes for position (x, y), velocity (x_vel, y_vel), mass, and a predefined
        TIMESTEP constant that represents the time step for the simulation.
        """

        # Initialize total force variables in x and y directions
        total_fx = total_fy = 0

        # Iterate through each celestial body in the 'planets' list
        for planet in planets:
            # Skip the calculation if the 'planet' is the current object ('self')
            if self == planet:
                continue

            # Calculate the gravitational force exerted on 'self' by 'planet'
            fx, fy = self.attraction(planet)

            # Accumulate the total forces in the x and y directions
            total_fx += fx
            total_fy += fy

        # Update the velocity of 'self' in the x direction
        # This is done by adding the acceleration (force/mass) to the current velocity
        # The acceleration is calculated as the total force in the x direction
        # divided by the mass of 'self', and then multiplied by the TIMESTEP
        self.x_vel += total_fx / self.mass * self.TIMESTEP

        # Update the velocity of 'self' in the y direction, similar to the x direction
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        # Update the position of 'self' in the x direction
        # The new position is calculated by adding the product of the velocity in the x direction
        # and the TIMESTEP to the current x position
        self.x += self.x_vel * self.TIMESTEP

        # Update the position of 'self' in the y direction, similar to the x direction
        self.y += self.y_vel * self.TIMESTEP

        # Append the new position (x, y) to the 'orbit' attribute of 'self'
        # This keeps track of the path that 'self' has traversed
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.989e30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.972e24)
    earth.y_vel = 29.783 * 1000  # 29.783 km/s

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39e23)
    mars.y_vel = 24.077 * 1000  # 24.077 km/s

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GRAY, 3.285e23)
    mercury.y_vel = -47.362 * 1000  # 47.362 km/s

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.867e24)
    venus.y_vel = -35.02 * 1000  # 35.02 km/s

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
