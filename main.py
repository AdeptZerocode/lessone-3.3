import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/images.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = random.choice([-2, 1])
target_speed_y = random.choice([-2, 1])

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

hits = 0
misses = 0

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

                target_speed_x = random.choice([-2, 1])
                target_speed_y = random.choice([-2, 1])
            else:
                misses += 1


    target_x += target_speed_x
    target_y += target_speed_y

    
    if target_x + target_width > SCREEN_WIDTH or target_x < 0:
        target_speed_x = -target_speed_x
    if target_y + target_height > SCREEN_HEIGHT or target_y < 0:
        target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))

    hit_text = font.render(f"Попадания: {hits}", True, (255, 255, 255))
    miss_text = font.render(f"Промахи: {misses}", True, (255, 255, 255))
    screen.blit(hit_text, (10, 10))
    screen.blit(miss_text, (10, 50))

    pygame.display.update()

pygame.quit()