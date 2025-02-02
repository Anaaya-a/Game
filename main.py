import pygame
from background import Background
from ship import Ship

def main():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Move the Ship")

    # Load the background
    bg = Background("game/background_img.jpg", screen)

    # Load the ship with movement
    ship = Ship("game/ship_img.png", screen, width=150, height=150, speed=1)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Pass events to the ship for movement
            ship.handle_event(event)

        # Update the ship's position
        ship.update()

        # Draw everything
        bg.draw()
        ship.draw()

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
