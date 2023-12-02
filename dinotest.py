import pygame
import sys
import random

WIDTH, HEIGHT = 800, 400

class DinoGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dino Game")

        self.dino_y = HEIGHT - 60
        self.cacti = []
        self.dino_velocity = 5
        self.cactus_velocity = 5
        self.jump_height = 100
        self.is_jumping = False
        self.cactus_spawn_timer = 0
        self.score = 0
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True

        if self.is_jumping:
            self.dino_y -= self.dino_velocity * 2
            self.jump_height -= self.dino_velocity * 2

            if self.jump_height <= 0:
                self.is_jumping = False
                self.jump_height = 100

        if self.dino_y < HEIGHT - 60 and not self.is_jumping:
            self.dino_y += self.dino_velocity

        # Update cactus position
        for cactus in self.cacti:
            cactus[0] -= self.cactus_velocity

        # Spawn new cactus at random intervals
        self.cactus_spawn_timer -= 1
        if self.cactus_spawn_timer <= 0:
            self.cacti.append([WIDTH, HEIGHT - 60])
            self.cactus_spawn_timer = random.randint(50, 100)

        # Check for collisions
        for cactus in self.cacti:
            if (
                50 < cactus[0] + 30
                and 50 + 30 > cactus[0]
                and self.dino_y < cactus[1] + 50
                and self.dino_y + 50 > cactus[1]
            ):
                print("Game Over!")
                pygame.quit()
                sys.exit()

        # Remove off-screen cacti
        self.cacti = [cactus for cactus in self.cacti if cactus[0] + 30 > 0]

        # Update score
        self.score += 1

        # Update display
        self.screen.fill((255, 255, 255))  # Set background color
        pygame.draw.rect(self.screen, (0, 0, 0), (50, self.dino_y, 30, 30))  # Draw dino
        for cactus in self.cacti:
            pygame.draw.rect(self.screen, (0, 0, 0), (cactus[0], cactus[1], 30, 30))  # Draw cactus

        pygame.display.flip()

        # Control the frame rate
        self.clock.tick(30)

# Example usage
if __name__ == "__main__":
    game = DinoGame()
    while True:
        game.handle_events()
        game.update()
