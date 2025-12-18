import asyncio
import pygame
from grid_system import GridSystem
from entity_system import Egg, MRosey, spawn_dragon_random


async def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (1280, 800),
        pygame.DOUBLEBUF | pygame.HWSURFACE
    )

    grid = GridSystem(hex_radius=35.0)
    egg = Egg()
    mrosey = MRosey()
    dragon = spawn_dragon_random(grid, mrosey.q, mrosey.r, egg.q, egg.r)
    
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                player_moved = False

                # PLAYER PHASE
                if event.key in (pygame.K_UP, pygame.K_w):
                    player_moved = mrosey.move('nw', grid)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    player_moved = mrosey.move('se', grid)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    player_moved = mrosey.move('w', grid)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    player_moved = mrosey.move('e', grid)
                elif event.key == pygame.K_q:
                    player_moved = mrosey.move('ne', grid)
                elif event.key == pygame.K_e:
                    player_moved = mrosey.move('sw', grid)

                # ENEMY PHASE
                if player_moved:
                    dragon.move_towards_target(mrosey.q, mrosey.r, grid)

                    # RESOLUTION PHASE
                    if mrosey.q == egg.q and mrosey.r == egg.r:
                        print("VICTORY - EGG SECURED")

                    if mrosey.q == dragon.q and mrosey.r == dragon.r:
                        print("GAME OVER - CAUGHT BY DRAGON")
                        mrosey.q = 0
                        mrosey.r = 3

        dt = clock.tick(60) / 1000.0

        screen.fill((0, 0, 0))
        grid.render(screen)
        egg.draw(screen, grid)
        dragon.draw(screen, grid)
        mrosey.draw(screen, grid)

        fps_text = font.render(f"FPS: {clock.get_fps():.2f}", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))

        pygame.display.flip()

        await asyncio.sleep(0)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())