import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cohete, Estrellas y Asteroides")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Clase Cohete
class Cohete(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Clase Estrella
class Estrella(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.y = random.randint(-100, -20)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 20)
            self.rect.y = random.randint(-100, -20)
            self.speed = random.randint(1, 3)

# Clase Asteroide
class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(-100, -30)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 30)
            self.rect.y = random.randint(-100, -30)
            self.speed = random.randint(2, 5)

# Función principal del juego
def main():
    clock = pygame.time.Clock()
    cohete = Cohete()
    estrellas = pygame.sprite.Group()
    asteroides = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(cohete)

    for _ in range(5):
        estrella = Estrella()
        estrellas.add(estrella)
        all_sprites.add(estrella)

    for _ in range(3):
        asteroide = Asteroide()
        asteroides.add(asteroide)
        all_sprites.add(asteroide)

    score = 0
    vidas = 5
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        # Colisiones con estrellas
        hits_estrellas = pygame.sprite.spritecollide(cohete, estrellas, True)
        for hit in hits_estrellas:
            score += 10
            estrella = Estrella()
            estrellas.add(estrella)
            all_sprites.add(estrella)

        # Colisiones con asteroides
        hits_asteroides = pygame.sprite.spritecollide(cohete, asteroides, True)
        for hit in hits_asteroides:
            vidas -= 1
            if vidas <= 0:
                running = False
            asteroide = Asteroide()
            asteroides.add(asteroide)
            all_sprites.add(asteroide)

        # Dibujar en pantalla
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Mostrar puntuación y vidas
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Puntuación: {score}", True, WHITE)
        vidas_text = font.render(f"Vidas: {vidas}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(vidas_text, (10, 50))

        pygame.display.flip()
        clock.tick(60)

    # Game Over
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 140, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()
    