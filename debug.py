import pygame
pygame.init()
font = pygame.font.Font(None, 36)

def debug_text(text, position=(10, 10), color=(255, 255, 255)):
    display_surface = pygame.display.get_surface()
    degub_surf = font.render(text, True, color)
    debug_rect = degub_surf.get_rect(topleft=position)
    pygame.draw.rect(display_surface, (0, 0, 0), debug_rect)
    display_surface.blit(degub_surf, debug_rect.topleft)