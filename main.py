import pygame
from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():  # Indented correctly
            if event.type == pygame.QUIT:  # Further indented correctly
                return  # This exits the game loop
        
        screen.fill((0, 0, 0))  # These lines align with the `for`, inside the while loop
        pygame.display.flip()
        print("Frame updated!")  # This will spam your console but helps debug


if __name__ == "__main__":
    main()
