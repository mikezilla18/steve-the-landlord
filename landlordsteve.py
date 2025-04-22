import pygame
import os
import sys

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Steve the Landlord: Eviction Quest")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images (with error handling)
def load_image(path, scale=None):
    try:
        img = pygame.image.load(path)
        return pygame.transform.scale(img, scale) if scale else img
    except:
        print(f"Failed to load {path}")
        return pygame.Surface((50, 50))  # Placeholder

# Image paths (UPDATE THESE TO YOUR ACTUAL PATHS)
STEVE_IMG = load_image("images/landlord/druid.png", (50, 80))
TENANT_IMG = load_image("images/tenant/zombie.png", (50, 80))
BG_IMG = load_image("images/background/min.png", (SCREEN_WIDTH, SCREEN_HEIGHT))

# Game states
MENU = 0
GAMEPLAY = 1

class Steve:
    def __init__(self):
        self.x, self.y = 50, SCREEN_HEIGHT - 150
        self.speed = 5
        self.health = 100
        self.image = STEVE_IMG
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, dx):
        self.x += dx * self.speed
        self.rect.x = self.x

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Tenant:
    def __init__(self):
        self.x, self.y = SCREEN_WIDTH - 100, SCREEN_HEIGHT - 150
        self.speed = 2
        self.health = 50
        self.image = TENANT_IMG
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, steve):
        if self.x > steve.x:
            self.x -= self.speed
            self.rect.x = self.x

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def main_menu():
    while True:
        screen.fill(WHITE)
        title = pygame.font.SysFont(None, 60).render("STEVE THE LANDLORD", True, BLACK)
        new_game = pygame.font.SysFont(None, 40).render("1. New Game", True, BLACK)
        load_game = pygame.font.SysFont(None, 40).render("2. Load Game", True, BLACK)
        quit_game = pygame.font.SysFont(None, 40).render("3. Quit", True, BLACK)

        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 100))
        screen.blit(new_game, (SCREEN_WIDTH//2 - new_game.get_width()//2, 250))
        screen.blit(load_game, (SCREEN_WIDTH//2 - load_game.get_width()//2, 300))
        screen.blit(quit_game, (SCREEN_WIDTH//2 - quit_game.get_width()//2, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return GAMEPLAY
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

def game_loop():
    steve = Steve()
    tenant = Tenant()
    clock = pygame.time.Clock()

    while True:
        screen.blit(BG_IMG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            steve.move(-1)
        if keys[pygame.K_RIGHT]:
            steve.move(1)

        tenant.update(steve)
        steve.draw()
        tenant.draw()

        pygame.display.flip()
        clock.tick(60)

def main():
    game_state = MENU
    while True:
        if game_state == MENU:
            game_state = main_menu()
        elif game_state == GAMEPLAY:
            game_loop()

if __name__ == "__main__":
    main()