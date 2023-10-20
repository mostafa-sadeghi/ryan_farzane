import random
from tkinter import font
import pygame

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dragon Game")

img = pygame.image.load("dragon/dragon.png")
dragon = pygame.transform.flip(img, True, False)
dragon_rect = dragon.get_rect()
dragon_rect.topleft = (20, WINDOW_HEIGHT/2)

pygame.mixer.music.load("dragon/bg_music.wav")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.3)

catch_sound = pygame.mixer.Sound("dragon/catch_sound.wav")
miss_sound = pygame.mixer.Sound("dragon/loss_sound.wav")


meat = pygame.image.load("dragon/meat.png")
meat = pygame.transform.scale(meat, (64, 64))
meat_rect = meat.get_rect()
meat_rect.center = (WINDOW_WIDTH + 100,
                    random.randint(132, WINDOW_HEIGHT - 32))
MEAT_STARTING_VELOCITY = 5
meat_velocity = MEAT_STARTING_VELOCITY
MEAT_ACCELERATION = 1
score = 0
dragon_velocity = 5

DRAGON_STARTING_LIVES = 3
dragon_lives = DRAGON_STARTING_LIVES

font = pygame.font.Font("dragon/myfont.ttf", 32)
score_text = font.render(f'Score: {score}', True, (255, 255, 255))
score_rect = score_text.get_rect(topleft=(10, 10))
lives_text = font.render(f'lives: {dragon_lives}', True, (255, 255, 255))
lives_rect = lives_text.get_rect(topright=(WINDOW_WIDTH - 30, 10))


def show_text(main_text, sub_text):
    main_text = font.render(main_text, True, (255, 255, 0))
    sub_text = font.render(sub_text, True, (255, 0, 0))
    main_rect = main_text.get_rect()
    sub_rect = sub_text.get_rect()
    main_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    sub_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 40)
    display_surface.blit(main_text, main_rect)
    display_surface.blit(sub_text, sub_rect)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    lives_text = font.render(f'lives: {dragon_lives}', True, (255, 255, 255))
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)


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

    meat_rect.x -= meat_velocity
    if meat_rect.x < 0:
        meat_rect.center = (WINDOW_WIDTH + 100,
                            random.randint(132, WINDOW_HEIGHT - 32))
        miss_sound.play()
        dragon_lives -= 1
        if score % 10 == 0:
            meat_velocity += MEAT_ACCELERATION

    if dragon_lives <= 0:
        show_text('Game Over', 'Press any key to continue...')
        # pygame.mixer.music.stop()
        
        score = 0
        dragon_lives = 3
        meat_velocity = MEAT_STARTING_VELOCITY
        pygame.display.update()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    is_paused = False
                    # pygame.mixer.music.play(-1)
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    if dragon_rect.colliderect(meat_rect):
        meat_rect.center = (WINDOW_WIDTH + 100,
                            random.randint(132, WINDOW_HEIGHT - 32))
        catch_sound.play()
        score += 1

    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    lives_text = font.render(f'lives: {dragon_lives}', True, (255, 255, 255))

    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon, dragon_rect)
    display_surface.blit(meat, meat_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
