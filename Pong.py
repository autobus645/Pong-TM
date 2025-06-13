import pygame 

pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0, 0, 0)

#ecran
WIDTH, HEIGHT = 1280, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

#options jeu
vitesse_balle = 3
rayon_balle = 6
width_paddle = 10
height_paddle = 100
vitesse_paddle = 10
difficulté_IA = 0       #le nombre multiplie la vitesse du paddle, 0 = pas de IA, donc on peut jouer à 2 joueurs
key_up_gauche = pygame.K_w
key_down_gauche = pygame.K_s
key_up_droite = pygame.K_UP
key_down_droite = pygame.K_DOWN


#score
score_gauche = 0
score_droite = 0


class Paddle:
    VITESSE = vitesse_paddle
    def __init__(self, x, y, width, height, key_up, key_down):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vitesse_y = 0
        self.key_up = key_up
        self.key_down = key_down

    def draw(self, win):
        pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[self.key_up]:
            if self.y > 0:
                self.y -= self.VITESSE
                self.vitesse_y = -self.VITESSE
        if keys[self.key_down]:
            if self.y < HEIGHT - self.height:
                self.y += self.VITESSE
                self.vitesse_y = self.VITESSE
        if keys[self.key_down] and keys[self.key_up] == False:
            self.vitesse_y = 0

    def movementAI(self):       #IA
        centreypaddle = self.height/2
        if self.y > 0:
            if self.y + centreypaddle > balle.y:
                self.y -= self.VITESSE * difficulté_IA
        if self.y < HEIGHT - self.height:
            if self.y + centreypaddle < balle.y:
                self.y += self.VITESSE * difficulté_IA

            

class Ball:
    vitesse_balle_x = vitesse_balle
    vitesse_balle_y = vitesse_balle
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
            self.vitesse_balle_x = vitesse_balle
            self.vitesse_balle_y = vitesse_balle
            return "point_gauche"       #ajouter un point pour la gauche
        if self.x <= 0:
            self.x = WIDTH // 2
            self.y = HEIGHT // 2
            self.vitesse_balle_x = -vitesse_balle
            self.vitesse_balle_y = vitesse_balle
            return "point_droite"       #ajouter un point pour la droite
            

    def check_collision(self, paddle):
        if (
            self.x - self.rayon <= paddle.x + paddle.width and      #cote gauche de la balle avec cote droit du paddle
            self.x + self.rayon >= paddle.x and         #cote droit de la balle avec cote gauche du paddle
            self.y >= paddle.y and                             
            self.y <= paddle.y + paddle.height
        ):
            self.vitesse_balle_x *= -1
            self.vitesse_balle_y += paddle.vitesse_y // 8
           
   

paddle_gauche = Paddle(10, HEIGHT/2-50, width_paddle, height_paddle, key_up_gauche, key_down_gauche)
paddle_droite = Paddle(WIDTH-20, HEIGHT/2-50, width_paddle, height_paddle, key_up_droite, key_down_droite )
balle = Ball(WIDTH/2,HEIGHT/2,rayon_balle)

font = pygame.font.SysFont("Arial", 50)

#boucle pour faire tourner le jeu
CLOCK = pygame.time.Clock()
def main():
    global score_gauche, score_droite       #pour utiliser ces variables en dehors de main
    run = True
    
    while run:
        CLOCK.tick(60)
        WIN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.draw.line(WIN, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT))       #ligne au milieu
        paddle_gauche.draw(WIN)     #dessiner les raquettes
        paddle_droite.draw(WIN)
        paddle_gauche.movement()      #movement des raquettes
        paddle_droite.movement()
        paddle_droite.movementAI()      #raquette droite IA
        balle.draw(WIN)       #dessiner la balle
        balle.movement()        #movement de la balle
        point = balle.movement()        #score
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