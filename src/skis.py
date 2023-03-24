import pygame

Surface = pygame.Surface
Rect = pygame.Rect


def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.

class Ski:

    def __init__(self, img: Surface) -> None:
        self.max_momentum = 150
        self.momentum_base_factor = 180
        self.momentum_reduction = 0.1
        self.angle = 90
        self.momentum = 0
        self.img = img
        self.center_offset = pygame.math.Vector2(0, 25)

    def set_angle(self, new_angle: float) -> float:
        if (new_angle > 180 or new_angle < 0):
            self.momentum = 0
        self.angle = max(min(180, new_angle), 0)
        return self.angle

    def change_angle(self, angle_diff: float) -> float:
        return self.set_angle(self.angle + angle_diff)

    def set_momentum(self, new_momentum: float) -> None:
        self.momentum = max(min(self.max_momentum, new_momentum), -self.max_momentum)

    def reduce_momentum(self, dt: float):
        self.momentum *= 1 - ((1 - self.momentum_reduction) * dt)
        print(1 - ((1 - self.momentum_reduction) * dt))


    def add_momentum(self, factor: float) -> None:
        self.set_momentum(self.momentum + factor * self.momentum_base_factor)

    def update(self, dt: float) -> tuple[Surface, Rect]:
        self.change_angle(self.momentum * dt)
        self.reduce_momentum(dt)

    def get_rect(self, offset: tuple[float, float]) -> tuple[Surface, Rect]:
        return rotate(self.img, self.angle + 90, offset, self.center_offset)


class Skis:
    def __init__(self) -> None:
        self.img = pygame.image.load("assets/ski.png")
        self.left_ski = Ski(self.img)
        self.right_ski = Ski(self.img)
        self.y = (3 / 4)
        self.x = (1 / 9)

    def angle_diff(self) -> float:
        return abs(self.left_ski.angle - self.right_ski.angle)

    def update(self, screen: pygame.surface.Surface, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            self.right_ski.add_momentum(-1 * dt)
        if keys[pygame.K_l]:
            self.right_ski.add_momentum(1 * dt)
        if keys[pygame.K_s]:
            self.left_ski.add_momentum(-1 * dt)
        if keys[pygame.K_d]:
            self.left_ski.add_momentum(1 * dt)

        y = screen.get_bounding_rect().height * self.y
        width = screen.get_bounding_rect().width
        x_diff = width * self.x
        c = width / 2

        self.left_ski.update(dt)
        s, r = self.left_ski.get_rect((c - x_diff, y))
        screen.blit(s, r)

        self.right_ski.update(dt)
        s, r = self.right_ski.get_rect((c + x_diff, y))
        screen.blit(s, r)

