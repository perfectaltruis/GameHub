import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up game window
WIDTH, HEIGHT = 800, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

# Load images
dino_img = pygame.image.load("dino.png")
# Resize the image
dino_img = pygame.transform.scale(dino_img, (30, 30))

cactus_img = pygame.image.load("cactus.png")

# Resize the image
cactus_img = pygame.transform.scale(cactus_img, (20, 30))

# Initial positions
dino_x, dino_y = 50, HEIGHT - 60
cacti = []

# Velocities
dino_velocity = 5
cactus_velocity = 5
jump_height = 100
is_jumping = False
cactus_spawn_timer = 0

# Score
score = 0
font = pygame.font.Font(None, 36)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the dinosaur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True

    if is_jumping:
        dino_y -= dino_velocity * 2
        jump_height -= dino_velocity * 2

        if jump_height <= 0:
            is_jumping = False
            jump_height = 100

    if dino_y < HEIGHT - 60 and not is_jumping:
        dino_y += dino_velocity

    # Update cactus position
    for cactus in cacti:
        cactus[0] -= cactus_velocity

    # Spawn new cactus at random intervals
    cactus_spawn_timer -= 1
    if cactus_spawn_timer <= 0:
        cacti.append([WIDTH, HEIGHT - 60])
        cactus_spawn_timer = random.randint(50, 100)

    # Check for collisions
    for cactus in cacti:
        if (
            dino_x < cactus[0] + 30
            and dino_x + 30 > cactus[0]
            and dino_y < cactus[1] + 50
            and dino_y + 50 > cactus[1]
        ):
            print("Game Over! Score:", score)
            pygame.quit()
            sys.exit()

    # Remove off-screen cacti
    cacti = [cactus for cactus in cacti if cactus[0] + 30 > 0]

    # Update score
    score += 1

    # Update display
    window.fill((255, 255, 255))  # Set background color
    window.blit(dino_img, (dino_x, dino_y))
    for cactus in cacti:
        window.blit(cactus_img, (cactus[0], cactus[1]))

    # Display score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_text, (10, 10))

    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)
