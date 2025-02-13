import pygame
import random

# Pygame start
pygame.init()

# Ustawienia okna
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("DVDBounce")
HEIGHT = 1080
WIDTH = 1920

# Wczytuje i laduje logo
dvd_logo = pygame.image.load("Assets/IMG/DVD_logo.png")
logo_width, logo_height = 264, 116
dvd_logo = pygame.transform.scale(dvd_logo, (logo_width, logo_height))

# Losowy kolorek
def random_color():
    return random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)

# Inicjalizacja pozycji i prędkości
x, y = random.randint(0, WIDTH - logo_width), random.randint(0, HEIGHT - logo_height)
speed_x, speed_y = 4, 4
color = random_color()

# Petla
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Czarny ekran
    
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Aktualizacja pozycji
    x += speed_x
    y += speed_y
    
    # Sprawdza czy koliduje z krawędziami
    if x <= 0 or x + logo_width >= WIDTH:
        speed_x = -speed_x
        color = random_color()
    if y <= 0 or y + logo_height >= HEIGHT:
        speed_y = -speed_y
        color = random_color()
    
    # Rysowanie loga z kolorem zmienionym jako filtr
    tinted_logo = dvd_logo.copy()
    tinted_logo.fill(color, special_flags=pygame.BLEND_MULT)
    screen.blit(tinted_logo, (x, y))
    
    pygame.display.flip()
    clock.tick(60)  # Max 60 FPS

pygame.quit()