
import pygame
import random

# إنشاء النافذة
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Game 🐍")
clock = pygame.time.Clock()

# الألوان
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (40, 40, 40)

# المتغيرات الأولية
block_size = 20
score = 0
font = pygame.font.SysFont("consolas", 24)
running = True

# إنشاء الثعبان (يبدأ بمربع واحد)
snake = [(100, 100)]
dx, dy = block_size, 0  # الاتجاه: يمين


x, y =snake[0]  # موقع رأس الثعبان  

# إنشاء الطعام في مكان عشوائي
food = (random.randint(0, (600 // block_size) - 1) * block_size,
        random.randint(0, (400 // block_size) - 1) * block_size)

# الحلقة الرئيسية
while running:
    # معالجة الأحداث
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -block_size
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, block_size
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -block_size, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = block_size, 0

    # الحركة
    x += dx
    y += dy
    head = (x, y)
    snake.insert(0, head)

    # التصادم مع الطعام
    if head == food:
        score += 1
        food = (random.randint(0, (600 // block_size) - 1) * block_size,
                random.randint(0, (400 // block_size) - 1) * block_size)
    else:
        snake.pop()

    # التصادم مع الجدران أو الذات
    if (x < 0 or x >= 600 or y < 0 or y >= 400 or head in snake[1:]):
        running = False

    # الرسم
    screen.fill(BLACK)
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, block_size, block_size))
    pygame.draw.rect(screen, RED, (*food, block_size, block_size))
    
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.update()
    clock.tick(10)
    