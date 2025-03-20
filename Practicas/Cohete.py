import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 1280, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cohete, Estrellas y Asteroides")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Cargar imágenes y escalarlas al 50%
try:
    cohete_img = pygame.image.load("cohete.jpg")
    estrella_img = pygame.image.load("estrella.jpg")
    asteroide_img = pygame.image.load("asteroide.jpg")
except pygame.error as e:
    print(f"Error cargando imágenes: {e}")
    pygame.quit()
    exit()

# Escalar imágenes al 50%
# cohete_img = pygame.transform.scale(cohete_img, (cohete_img.get_width() // 2, cohete_img.get_height() // 2))
estrella_img = pygame.transform.scale(estrella_img, (estrella_img.get_width() // 2, estrella_img.get_height() // 2))
asteroide_img = pygame.transform.scale(asteroide_img, (asteroide_img.get_width() // 4, asteroide_img.get_height() // 4))

# Cargar sonidos
try:
    pygame.mixer.music.load("musica_fondo.mp3")  # Música de fondo
    choque_asteroide_sonido = pygame.mixer.Sound("choque_asteroide.mp3")  # Sonido de choque con asteroide
    choque_estrella_sonido = pygame.mixer.Sound("choque_estrella.mp3")  # Sonido de choque con estrella
except pygame.error as e:
    print(f"Error cargando sonidos: {e}")
    pygame.quit()
    exit()

# Reproducir música de fondo en bucle
pygame.mixer.music.play(-1)

# Clase Cohete
class Cohete(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cohete_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:  # Mover hacia arriba
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:  # Mover hacia abajo
            self.rect.y += self.speed

# Clase Estrella
class Estrella(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = estrella_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -20)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -20)
            self.speed = random.randint(1, 3)

# Clase Asteroide
class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = asteroide_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -30)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
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
    ultimo_puntaje_vida = 0  # Para rastrear cuándo se otorgó la última vida
    ultimo_puntaje_velocidad = 0  # Para rastrear cuándo se aumentó la velocidad por última vez
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
            choque_estrella_sonido.play()  # Reproducir sonido de choque con estrella
            estrella = Estrella()
            estrellas.add(estrella)
            all_sprites.add(estrella)

        # Colisiones con asteroides
        hits_asteroides = pygame.sprite.spritecollide(cohete, asteroides, True)
        for hit in hits_asteroides:
            vidas -= 1
            choque_asteroide_sonido.play()  # Reproducir sonido de choque con asteroide
            if vidas <= 0:
                running = False
            asteroide = Asteroide()
            asteroides.add(asteroide)
            all_sprites.add(asteroide)

        # Otorgar una vida cada 100 puntos
        if score // 100 > ultimo_puntaje_vida // 100:
            vidas += 1
            ultimo_puntaje_vida = score  # Actualizar el último puntaje en el que se otorgó una vida

        # Aumentar la velocidad y la cantidad de asteroides cada 100 puntos
        if score // 100 > ultimo_puntaje_velocidad // 100:
            # Aumentar la velocidad de las estrellas y asteroides
            for estrella in estrellas:
                estrella.speed += 1  # Aumentar la velocidad de las estrellas
            for asteroide in asteroides:
                asteroide.speed += 1  # Aumentar la velocidad de los asteroides

            # Añadir un nuevo asteroide
            if len(asteroides) < 10:  # Límite máximo de 10 asteroides
                nuevo_asteroide = Asteroide()
                asteroides.add(nuevo_asteroide)
                all_sprites.add(nuevo_asteroide)

            ultimo_puntaje_velocidad = score  # Actualizar el último puntaje en el que se aumentó la velocidad

        # Dibujar en pantalla
        screen.fill(WHITE)  # Fondo blanco
        all_sprites.draw(screen)

        # Mostrar puntuación y vidas
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Puntuación: {score}", True, BLACK)  # Texto negro
        vidas_text = font.render(f"Vidas: {vidas}", True, BLACK)  # Texto negro
        screen.blit(score_text, (10, 10))
        screen.blit(vidas_text, (10, 50))

        pygame.display.flip()
        clock.tick(60)

    # Game Over
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Game Over", True, BLACK)  # Texto negro
    screen.blit(game_over_text, (WIDTH // 2 - 140, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()
