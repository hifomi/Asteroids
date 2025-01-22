import pygame
from constants import *

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    return screen, clock

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def update_screen(screen):
    screen.fill((0, 0, 0))
    pygame.display.flip()

def main():
    screen, clock = initialize_game()
    dt = 0
    
    while True:  # Main game loop
        if handle_events():  # Check for quit
            break
        
        update_screen(screen)  # Draw the screen
        
        # Get dt in seconds (divide by 1000 to convert from milliseconds)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()