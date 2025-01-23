import pygame
from constants import *
from circleshape import CircleShape



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):

        self.timers(dt)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):

        if self.timer <= 0:
            # Determine the direction and velocity of the bullet
            direction = pygame.Vector2(0, 1).rotate(self.rotation)  # Facing upward, rotated to player's direction
            velocity = direction * PLAYER_SHOOT_SPEED  # Scale direction by shoot speed

            # Create a new shot using the player's position, SHOT_RADIUS, and velocity
            new_shot = Shot(self.position.x, self.position.y, velocity)

            self.timer = PLAYER_SHOOT_COOLDOWN

    def timers(self, dt):
    # Only decrement the timer if it is greater than 0
        if self.timer > 0:
            self.timer -= dt
            

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)  # Properly pass `x`, `y`, and radius to parent class

        # Ensure position is a Vector2 (inherited from CircleShape)
        self.position = pygame.Vector2(x, y)

        # Assign the velocity passed from the Player's shoot method
        self.velocity = velocity

    def draw(self, screen):
        # Draw the shot as a circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), SHOT_RADIUS)

    def update(self, dt):
        # Update position using velocity and delta time
        self.position += self.velocity * dt

        # Remove the shot if it leaves the screen
        if not (0 <= self.position.x <= SCREEN_WIDTH and 0 <= self.position.y <= SCREEN_HEIGHT):
            self.kill()