import pygame

class Ship:
    def __init__(self, image_path, screen, width=50, height=50, speed=5):
        """
        Initializes the Ship class.

        Args:
            image_path (str): Path to the ship image.
            screen (pygame.Surface): The game screen where the ship will be drawn.
            width (int): The width to resize the ship image.
            height (int): The height to resize the ship image.
            speed (int): The speed at which the ship moves.
        """
        self.screen = screen
        self.speed = speed  # Movement speed

        # Load and resize the ship image
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(original_image, (width, height))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Position the ship at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 10  # Move up slightly

        # Movement flags
        self.moving_left = False
        self.moving_right = False

    def handle_event(self, event):
        """Handles key press events for moving the ship."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.moving_left = True
            elif event.key == pygame.K_RIGHT:
                self.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.moving_left = False
            elif event.key == pygame.K_RIGHT:
                self.moving_right = False

    def update(self):
        # print("hello")
        """Updates the ship's position based on movement flags."""
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed

    def draw(self):
        """Draws the ship on the screen."""
        self.screen.blit(self.image, self.rect)
