import math
import random
import sys

import pygame

pygame.init()

W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("heart")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 20)

TEXT = "SHABWA"
PINK = (255, 77, 109)
BG = (5, 5, 5)


def heart_points():
    points = []
    cx, cy = W // 2, H // 2
    scale = min(W, H) / 45

    def add_points(count, scale_factor, target_range, delay_range):
        for i in range(count):
            t = (i / count) * math.pi * 2
            x = 16 * math.sin(t) ** 3
            y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
            points.append({
                "x": cx + x * scale * scale_factor,
                "y": cy + y * scale * scale_factor,
                "target": random.uniform(*target_range),
                "delay": random.uniform(*delay_range),
            })

    add_points(180, 1.0, (100, 255), (0, 6000))
    for s in [0.2, 0.4, 0.6, 0.8]:
        add_points(80, s, (80, 180), (0, 8000))

    return points


def draw_text():
    text_surface = font.render(TEXT, True, PINK)
    text_rect = text_surface.get_rect(center=(W // 2, H // 2 + 280))
    screen.blit(text_surface, text_rect)


def main():
    points = heart_points()
    start_time = pygame.time.get_ticks()
    running = True

    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(BG)

        for point in points:
            elapsed = current_time - (start_time + int(point["delay"]))
            if elapsed < 0:
                continue

            progress = min(1.0, elapsed / 1800)
            alpha = int(point["target"] * progress)
            if alpha <= 0:
                continue

            radius = 2 if alpha > 120 else 1
            surface = pygame.Surface((radius * 2 + 1, radius * 2 + 1), pygame.SRCALPHA)
            pygame.draw.circle(surface, (255, 77, 109, alpha), (radius, radius), radius)
            screen.blit(surface, (int(point["x"] - radius), int(point["y"] - radius)))

        draw_text()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
