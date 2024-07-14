import pygame

pygame.init()

window_width = 800
window_height = 600
platform_width = 100
platform_height = 10
platform_speed=2
ball_speedX=3
ball_speedY=3
obstacle_width=50
obstacle_height=20

White=(255, 255, 255)
Blue = (0, 84, 252)
Red = (245, 0, 0)
Green = (0, 255, 0)

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Breakout Game")

platform_x = (window_width - platform_width) // 2
platform_y = window_height - platform_height - 10

def draw_platform(x, y):
    position = (x, y, platform_width, platform_height)
    pygame.draw.rect(screen, Green, position)

def draw_ball():
    radius=float(10)
    position=(300, 500)
    pygame.draw.circle(screen, Red, position, radius)

def draw_obstacle():
    num_columns = 14
    num_rows = 10
    x_start = 10
    y_start = 50
    gap = 5

    for row in range(num_rows):
        for col in range(num_columns):
            x_position = x_start + col * (obstacle_width + gap)
            y_position = y_start + row * (obstacle_height + gap)
            position = (x_position, y_position, obstacle_width, obstacle_height)
            pygame.draw.rect(screen, Blue, position)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform_x -=platform_speed
    if keys[pygame.K_RIGHT]:
        platform_x +=platform_speed

    if platform_x<0:
        platform_x=0
    if platform_x>window_width-platform_width:
        platform_x=window_width-platform_width



    screen.fill(White)
    draw_platform(platform_x, platform_y)
    draw_ball()
    draw_obstacle()

    pygame.display.update()

pygame.quit()
