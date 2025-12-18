import pygame
from typing import Tuple
from grid_system import GridSystem
import random

HEX_DIRECTIONS = {
    'ne': (+1, -1),
    'e':  (+1,  0),
    'se': ( 0, +1),
    'sw': (-1, +1),
    'w':  (-1,  0),
    'nw': ( 0, -1),
}

def axial_distance(q1: int, r1: int, q2: int, r2: int) -> int:
    return (abs(q1 - q2) + abs(r1 - r2) + abs((q1 + r1) - (q2 + r2))) // 2

class Entity:
    def __init__(self, q: int, r: int, color: tuple, radius: float = 20.0):
        self.q = q
        self.r = r
        self.color = color
        self.radius = radius

    def get_pixel_pos(self, grid_system: GridSystem) -> Tuple[float, float]:
        return grid_system.axial_to_pixel(self.q, self.r)

    def draw(self, screen: pygame.Surface, grid_system: GridSystem) -> None:
        x, y = self.get_pixel_pos(grid_system)
        center = (int(x), int(y))
        pygame.draw.circle(screen, self.color, center, int(self.radius))
        pygame.draw.circle(screen, (0, 0, 0), center, int(self.radius), width=1)

class Egg(Entity):
    def __init__(self):
        super().__init__(q=0, r=-3, color=(255, 215, 0), radius=15.0)

class MRosey(Entity):
    def __init__(self):
        super().__init__(q=0, r=3, color=(0, 255, 255), radius=18.0)

    def move(self, direction: str, grid_system: GridSystem) -> bool:
        if direction not in HEX_DIRECTIONS:
            return False
        dq, dr = HEX_DIRECTIONS[direction]
        target_q = self.q + dq
        target_r = self.r + dr
        if grid_system.get_tile(target_q, target_r) is not None:
            self.q = target_q
            self.r = target_r
            return True
        return False

class Dragon(Entity):
    def __init__(self, q: int, r: int):
        super().__init__(q=q, r=r, color=(255, 0, 0), radius=18.0)

    def move_towards_target(self, target_q: int, target_r: int, grid_system: GridSystem) -> bool:
        valid_neighbors = []
        for dq, dr in HEX_DIRECTIONS.values():
            nq = self.q + dq
            nr = self.r + dr
            if grid_system.get_tile(nq, nr) is not None:
                valid_neighbors.append((nq, nr))
        if not valid_neighbors:
            return False
        best_neighbor = min(valid_neighbors, key=lambda pos: axial_distance(pos[0], pos[1], target_q, target_r))
        self.q, self.r = best_neighbor
        return True

def spawn_dragon_random(grid_system: GridSystem, mrosey_q: int, mrosey_r: int, egg_q: int, egg_r: int) -> Dragon:
    valid_tiles = list(grid_system.tiles.keys())
    spawn_candidates = [(q, r) for (q, r) in valid_tiles if (q, r) != (mrosey_q, mrosey_r) and (q, r) != (egg_q, egg_r)]
    spawn_q, spawn_r = random.choice(spawn_candidates)
    return Dragon(spawn_q, spawn_r)