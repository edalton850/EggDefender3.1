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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position
                mouse_x, mouse_y = event.pos
                
                # Find closest valid neighbor to click
                from entity_system import HEX_DIRECTIONS
                player_moved = False
                closest_distance = float('inf')
                best_direction = None
                
                # Check each possible direction
                for direction, (dq, dr) in HEX_DIRECTIONS.items():
                    neighbor_q = mrosey.q + dq
                    neighbor_r = mrosey.r + dr
                    
                    # Check if this neighbor exists
                    if grid.get_tile(neighbor_q, neighbor_r) is not None:
                        # Get pixel position of this neighbor
                        neighbor_x, neighbor_y = grid.axial_to_pixel(neighbor_q, neighbor_r)
                        
                        # Calculate distance from mouse click to tile center
                        distance = ((mouse_x - neighbor_x)**2 + (mouse_y - neighbor_y)**2)**0.5
                        
                        # If this is the closest valid neighbor (within 50 pixels)
                        if distance < closest_distance and distance < 50:
                            closest_distance = distance
                            best_direction = direction
                
                # Move to the clicked neighbor
                if best_direction:
                    player_moved = mrosey.move(best_direction, grid)
                    
                    # ENEMY PHASE (only if player moved)
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