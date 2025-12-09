import asyncio
import pygame


async def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (1280, 800),
        pygame.DOUBLEBUF | pygame.HWSURFACE
    )

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000.0
        print(dt)

        screen.fill((0, 255, 0))

        fps_text = font.render(f"FPS: {clock.get_fps():.2f}", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))

        pygame.display.flip()

        await asyncio.sleep(0)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
