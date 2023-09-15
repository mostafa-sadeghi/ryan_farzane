import random
import pygame

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


img = pygame.image.load("dragon/dragon.png")
dragon = pygame.transform.flip(img, True, False)
dragon_rect = dragon.get_rect()
dragon_rect.topleft = (20, WINDOW_HEIGHT/2)

pygame.mixer.music.load("dragon/bg_music.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

catch_sound = pygame.mixer.Sound("dragon/catch_sound.wav")
miss_sound = pygame.mixer.Sound("dragon/loss_sound.wav")



meat = pygame.image.load("dragon/meat.png")
meat = pygame.transform.scale(meat, (64,64))
meat_rect = meat.get_rect()
meat_rect.center = (WINDOW_WIDTH + 100, random.randint(132, WINDOW_HEIGHT - 32)) 


dragon_velocity = 5
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += 5
    if keys[pygame.K_UP] and dragon_rect.top > 0:
        dragon_rect.y -= 5
    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon, dragon_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
