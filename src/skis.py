import pygame
from random import uniform
from math import cos, sin, radians, exp

Surface = pygame.Surface
Rect = pygame.Rect


def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vecto30r2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.

class Ski:

    def __init__(self, img: Surface, is_left: bool) -> None:
        max_angle_factor = 16
        self.max_momentum = 250
        self.momentum_base_factor = 220
        self.momentum_reduction = 0.05
        self.min_speed_reduction = 1
        self.angle = 90
        self.angle_max = 60
        self.max_angle = self.angle + 60 + is_left * max_angle_factor
        self.min_angle = self.angle - 60 - (not is_left) * max_angle_factor
        self.momentum = 0
        self.bounce_ratio = 0.5
        self.center_offset = pygame.math.Vector2(0, img.get_height() // 4)

        self.img = img

    def set_angle(self, new_angle: float) -> float:
        if (new_angle > self.max_angle or new_angle < self.min_angle):
            self.momentum = -self.momentum * self.bounce_ratio
        self.angle = max(min(self.max_angle, new_angle), self.min_angle)
        return self.angle

    def change_angle(self, angle_diff: float) -> float:
        return self.set_angle(self.angle + angle_diff)

    def set_momentum(self, new_momentum: float) -> None:
        self.momentum = max(min(self.max_momentum, new_momentum), -self.max_momentum)

    def reduce_momentum(self, dt: float):
        self.set_momentum(self.momentum - (self.momentum * dt * 2))

    def add_momentum(self, factor: float) -> None:
        self.set_momentum(self.momentum + factor * self.momentum_base_factor)

    def shake(self):
        self.add_momentum(uniform(-self.max_momentum, self.max_momentum))

    def update(self, dt: float) -> tuple[Surface, Rect]:
        self.change_angle(self.momentum * dt)
        self.reduce_momentum(dt)

    def get_rect(self, offset: tuple[float, float]) -> tuple[Surface, Rect]:
        return rotate(self.img, self.angle + 90, offset, self.center_offset)


class Skis:
    def __init__(self) -> None:
        self.pos = pygame.math.Vector2(0, 0)
        self.img = pygame.image.load("assets/ski.png")
        self.left_ski = Ski(self.img, True)
        self.right_ski = Ski(self.img, False)
        self.y = (3 / 4)
        self.x = (1 / 12)
        self.speed = 1
        self.max_speed = 883 / 3
        self.max_speed_gain = self.max_speed / 7.5
        self.max_speed_penalty = 3
        self.drag_ratio = 0.9
        self.speed_ratio = 3

        self.max_points = 100

    def update_speed(self, dt: float):
        d = self.angle_diff() / 180
        alpha = ((self.left_ski.angle) + (self.right_ski.angle)) / 2 - 90
        penalty = max(self.max_speed_penalty * d, 0)
        self.speed += exp(-(alpha/60) ** 2) * self.max_speed_gain * dt
        self.speed -= self.speed * (penalty * dt)
        self.speed *= 1 -((1 - self.drag_ratio) * dt)
        if (self.speed > self.max_speed):
            self.speed = self.max_speed

    def calc_score(self, dt: float):
        k = 5
        x = self.angle_diff()
        m = self.max_points
        return (m - m * x / (k + x)) * dt

    def get_deplacement(self, dt: float):
        alpha = radians(180 - ((self.left_ski.angle) + (self.right_ski.angle)) / 2)
        res = pygame.Vector2(cos(alpha), sin(alpha))
        return res * self.speed * dt * self.speed_ratio

    def angle_diff(self) -> float:
        return abs(self.left_ski.angle - self.right_ski.angle)

    def update(self, screen: pygame.surface.Surface, dt: float, x: float = 0) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            self.right_ski.add_momentum(-1 * dt)
        if keys[pygame.K_l]:
            self.right_ski.add_momentum(1 * dt)
        if keys[pygame.K_s]:
            self.left_ski.add_momentum(-1 * dt)
        if keys[pygame.K_d]:
            self.left_ski.add_momentum(1 * dt)

        y = screen.get_height() * self.y
        width = screen.get_width()
        x_diff = width * self.x
        c = width / 2

        self.left_ski.update(dt)
        s, r = self.left_ski.get_rect((c - x_diff, y))
        r.left += x
        screen.blit(s, r)

        self.right_ski.update(dt)
        s, r = self.right_ski.get_rect((c + x_diff, y))
        r.left += x
        screen.blit(s, r)
        self.pos += self.get_deplacement(dt)
        self.update_speed(dt)
