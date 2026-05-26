import cv2
import numpy
import pygame
import mediapipe
import time

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

# Tạo window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Đặt title
pygame.display.set_caption("My Game")

# Load image
player_image = pygame.image.load("./Assets/Images/Basket/basket.png")
player_image = pygame.transform.scale(player_image, (100, 100))
player_rect = player_image.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

# Game loop
running = True

while running:

    # Bắt event
    for event in pygame.event.get():

        # Đóng window
        if event.type == pygame.QUIT:
            running = False

    # Tô background màu đen
    screen.fill((0, 0, 0))

    # Render image
    screen.blit(player_image, player_rect)
    pygame.draw.line(screen, (255, 0, 0), (0, SCREEN_HEIGHT - 50), (SCREEN_WIDTH, SCREEN_HEIGHT - 50), 5)

    # Update frame
    pygame.display.update()

# Thoát pygame
pygame.quit()
