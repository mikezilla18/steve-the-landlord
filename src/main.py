import pygame
import sys
import random
from systems.asset_loader import AssetLoader
from systems.animation import Animation

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Steve the Landlord")
clock = pygame.time.Clock()

# Initialize systems
loader = AssetLoader()

# Load assets with placeholder fallback
def load_animation(frames, category, prefix, scale=(50,80)):
    images = []
    for i, frame in enumerate(frames, 1):
        img = loader.load(
            f"characters/{category}",
            f"{prefix}_{str(i).zfill(2)}.png",
            scale
        )
        images.append(img)
    return images

# Create test animation (will use placeholders if files missing)
steve_frames = load_animation(["idle"], "steve", "idle")
steve_anim = Animation(steve_frames, fps=8)

# Player class
class Player:
    def __init__(self):
        self.x = 100
        self.y = 400
        self.speed = 5
        self.facing_right = True

    def move(self, dx):
        self.x += dx * self.speed
        if dx != 0:
            self.facing_right = dx > 0

# Game state
player = Player()
running = True

# Main game loop
while running:
    dt = pygame.time.get_ticks()
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement
    keys = pygame.key.get_pressed()
    dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    player.move(dx)
    
    # Update animation
    steve_anim.update(dt)
    
    # Drawing
    screen.fill((50, 50, 70))  # Dark blue background
    
    # Draw player (flipped if facing left)
    frame = pygame.transform.flip(
        steve_anim.current_image(),
        not player.facing_right,
        False
    )
    screen.blit(frame, (player.x, player.y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()