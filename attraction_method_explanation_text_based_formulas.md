# Detailed Physics and Mathematics in the `attraction` Method

## Newton's Law of Universal Gravitation

### Gravitational Constant (G)

- **Definition**: The gravitational constant, denoted as `G`, is a fundamental physical constant that quantifies the
  strength of the gravitational force between two objects.
- **Value**: `G = 6.674 x 10^-11 Nm^2/kg^2`.
- **Units**:
    - `N` (Newton) is the unit of force in the International System of Units (SI).
    - `m` (meter) is the unit of distance.
    - `kg` (kilogram) is the unit of mass.
    - Therefore, `Nm^2/kg^2` indicates how much force (in Newtons) acts over a square meter per square kilogram.
- **Application in the Method**: `self.G` likely represents the gravitational constant `G` and is used in the formula to
  calculate the gravitational force.

### The Formula

- **Mathematical Representation**:
  `F = G * (m1 * m2) / r^2`
- **Application in the Method**:
  ```python
  force = self.G * self.mass * other.mass / distance**2
  ```
  This line directly applies Newton's law, using the masses of the two objects (`self.mass` and `other.mass`) and their
  distance (`distance`) to calculate the gravitational force (`force`).

## Vector Decomposition

### Angle (Theta)

- **Definition**: In mathematics, `theta` represents an angle in radians.
- **Context in Physics**: In the method, `theta` represents the angle of the gravitational force vector relative to the
  horizontal axis.
- **Application in the Method**:
  ```python
  theta = math.atan2(distance_y, distance_x)
  ```
  This line calculates the angle `theta` between the line connecting `self` and `other` and the horizontal axis.

### Trigonometric Functions: Cosine and Sine

- **Cosine (cos)**:
    - **Definition**: In a right-angled triangle, the cosine of an angle is the ratio of the length of the adjacent side
      to the length of the hypotenuse.
    - **Application in the Method**:
      ```python
      force_x = math.cos(theta) * force
      ```
      This line calculates the x-component of the gravitational force, considering the angle `theta`.
- **Sine (sin)**:
    - **Definition**: In a right-angled triangle, the sine of an angle is the ratio of the length of the opposite side
      to the length of the hypotenuse.
    - **Application in the Method**:
      ```python
      force_y = math.sin(theta) * force
      ```
      This line calculates the y-component of the gravitational force, also considering the angle `theta`.

## atan2 Function

- **Definition**: The `atan2(y, x)` function returns the arctangent of `y/x` in radians, which is the angle formed by
  the line with the positive x-axis.
- **Why atan2 and Not atan**: `atan2` is preferred over `atan` as it handles the cases where `x` is zero and can
  determine the correct quadrant of the angle.
- **Application in the Method**:
  ```python
  theta = math.atan2(distance_y, distance_x)
  ```
  This calculates the angle of the gravitational force vector in relation to the horizontal axis, ensuring the correct
  direction of the force is obtained.
