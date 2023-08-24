import pygame

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


img = pygame.image.load("dragon.png")
dragon = pygame.transform.flip(img, True, False)
dragon_rect = dragon.get_rect()
dragon_rect.topleft = (20, WINDOW_HEIGHT/2)

dragon_velocity = 5
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        dragon_rect.y += 5
    if keys[pygame.K_UP]:
        dragon_rect.y -= 5
    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon, dragon_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
