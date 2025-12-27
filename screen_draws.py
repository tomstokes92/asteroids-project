import pygame

from constants import *


def draw_score(screen: pygame.Surface, font: pygame.font.Font, score: int) -> None:
    score_surface = font.render(str(score), True, "white")
    rect = score_surface.get_rect(midtop=(SCREEN_WIDTH //2, 10))
    screen.blit(score_surface, rect)

