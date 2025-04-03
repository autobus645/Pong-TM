import pygame


#ecran
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

WHITE = (255,255,255)
BLACK = (0, 0, 0)

class Paddle:
    VITESSE = 5
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))
    
    def movement(self):

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            if self.y > 0:
                self.y -= self.VITESSE
        if keys[pygame.K_s]:
            if self.y < 500:
                self.y += self.VITESSE



class Ball:
    def __init__(self, x, y, rayon):
        self.x = x
        self.y = y
        self.rayon = rayon

    def draw(self, win):
        pygame.draw.circle(WIN, WHITE,(self.x, self.y), self.rayon)

    





paddle_gauche = Paddle(10, HEIGHT/2-50, 10, 100)
paddle_droite = Paddle(WIDTH-20, HEIGHT/2-50, 10, 100)
balle = Ball(400,300,6)

#boucle pour faire tourner le jeu
CLOCK = pygame.time.Clock()
def main():
    run = True
    
    while run:
        CLOCK.tick(60)
        WIN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        Paddle.draw(paddle_gauche, WIN)
        Paddle.draw(paddle_droite, WIN)
        Paddle.movement(paddle_gauche)
        Ball.draw(balle, WIN)
        

        pygame.display.update()
        
    pygame.quit()

main()