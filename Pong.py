import pygame 

pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0, 0, 0)

#ecran
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

#score
score_gauche = 0
score_droite = 0


class Paddle:
    VITESSE = 10
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vitesse_y = 0

    def draw(self, win):
        pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))
    
    def movementleft(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.y > 0:
                self.y -= self.VITESSE
                self.vitesse_y = -self.VITESSE
        if keys[pygame.K_s]:
            if self.y < HEIGHT - self.height:
                self.y += self.VITESSE
                self.vitesse_y = self.VITESSE
        if keys[pygame.K_s] and keys[pygame.K_w] ==  False:
            self.vitesse_y = 0

    def movementright(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] :
            if self.y > 0:
                self.y -= self.VITESSE
                self.vitesse_y = -self.VITESSE
        if keys[pygame.K_DOWN]:
            if self.y < HEIGHT - self.height:
                self.y += self.VITESSE
                self.vitesse_y = self.VITESSE



class Ball:
    vitesse_balle_x = 3
    vitesse_balle_y = 3
    def __init__(self, x, y, rayon):
        self.x = x
        self.y = y
        self.rayon = rayon
        

    def draw(self, win):
        pygame.draw.circle(WIN, WHITE,(self.x, self.y), self.rayon)

    def movement(self):
        self.x += self.vitesse_balle_x
        self.y += self.vitesse_balle_y
        if self.y <= 0:
            self.vitesse_balle_y *= -1
        if self.y >= HEIGHT:
            self.vitesse_balle_y *= -1
        if self.x >= WIDTH:
            self.x = WIDTH // 2
            self.y = HEIGHT // 2
            self.vitesse_balle_x = 3
            self.vitesse_balle_y = 3
            return "point_gauche"                                           #ajouter un point pour la droite
        if self.x <= 0:
            self.x = WIDTH // 2
            self.y = HEIGHT // 2
            self.vitesse_balle_x = -3
            self.vitesse_balle_y = 3
            return "point_droite"                                           #ajouter un point pour la gauche
            

    def check_collision(self, paddle):
        if (
            self.x - self.rayon <= paddle.x + paddle.width and              #cote gauche de la balle avec cote droit du paddle
            self.x + self.rayon >= paddle.x and                             #cote droit de la balle avec cote gauche du paddle
            self.y >= paddle.y and                             
            self.y <= paddle.y + paddle.height
        ):
            self.vitesse_balle_x *= -1
            self.vitesse_balle_y += paddle.vitesse_y // 2
           
   

paddle_gauche = Paddle(10, HEIGHT/2-50, 10, 100)
paddle_droite = Paddle(WIDTH-20, HEIGHT/2-50, 10, 100)
balle = Ball(400,300,6)

font = pygame.font.SysFont("Arial", 50)

#boucle pour faire tourner le jeu
CLOCK = pygame.time.Clock()
def main():
    global score_gauche, score_droite                                           #pour utiliser ces variables en dehors de main
    run = True
    
    while run:
        CLOCK.tick(60)
        WIN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.draw.line(WIN, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT))           #ligne au milieu
        Paddle.draw(paddle_gauche, WIN)                                         #dessiner les raquettes
        Paddle.draw(paddle_droite, WIN)
        Paddle.movementleft(paddle_gauche)                                      #movement des raquettes
        Paddle.movementright(paddle_droite)
        Ball.draw(balle, WIN)                                                   #dessiner la balle
        Ball.movement(balle)                                                    #movement de la balle
        point = balle.movement()                                                #score
        if point == "point_gauche":
            score_gauche += 1
        if point == "point_droite":
            score_droite += 1
        balle.check_collision(paddle_gauche)
        balle.check_collision(paddle_droite)
        score_text = font.render(f"{score_gauche}    {score_droite}", 1, WHITE)
        WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))
        pygame.display.update()
        
    pygame.quit()

main()