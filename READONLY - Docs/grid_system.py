import pygame
import math


class HexTile:
    def __init__(self, q: int, r: int, x: float, y: float, color: tuple = (26, 26, 62)):
        self.q = q
        self.r = r
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen: pygame.Surface, hex_radius: float) -> None:
        # Flat-top hexagon vertices (0°, 60°, 120°, 180°, 240°, 300°)
        vertices = [
            (
                self.x + hex_radius * math.cos(angle),
                self.y + hex_radius * math.sin(angle)
            )
            for angle in (
                0,
                math.pi / 3,
                2 * math.pi / 3,
                math.pi,
                4 * math.pi / 3,
                5 * math.pi / 3,
            )
        ]

        pygame.draw.polygon(screen, self.color, vertices)
        pygame.draw.polygon(screen, (255, 255, 255), vertices, width=2)


class GridSystem:
    def __init__(
        self,
        hex_radius: float = 35.0,
        center_x: float = 640.0,
        center_y: float = 400.0,
    ):
        self.hex_radius = hex_radius
        self.center_x = center_x
        self.center_y = center_y
        self.tiles: dict[tuple[int, int], HexTile] = {}

        self._generate_hex_map(3)

    def _generate_hex_map(self, map_radius: int) -> None:
        for q in range(-map_radius, map_radius + 1):
            for r in range(-map_radius, map_radius + 1):
                if max(abs(q), abs(r), abs(q + r)) <= map_radius:
                    x, y = self.axial_to_pixel(q, r)
                    self.tiles[(q, r)] = HexTile(q, r, x, y)

    def axial_to_pixel(self, q: int, r: int) -> tuple[float, float]:
        x = self.center_x + self.hex_radius * (1.5 * q)
        y = self.center_y + self.hex_radius * (
            math.sqrt(3) / 2 * (2 * r + q)
        )
        return x, y

    def get_tile(self, q: int, r: int) -> HexTile | None:
        return self.tiles.get((q, r))

    def render(self, screen: pygame.Surface) -> None:
        for tile in self.tiles.values():
            tile.draw(screen, self.hex_radius)