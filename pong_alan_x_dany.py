import pygame

pygame.init()

#preload
racket_png = pygame.image.load("racket.png") # ligne 84
ball_png = pygame.image.load("ball.png") # ligne 222
right_click_png = pygame.image.load("mouse_click-gauche.png") # ligne 284
directions_keys_png = pygame.image.load("direction_keys_pressed.png") # ligne 284

#screen variables
screen_width = 800
screen_height = 560
margin = 70
fpsClock = pygame.time.Clock()
fps = 60
echanges = 0
speed_ball = 0
blue_dark = (9, 10, 16)
white = (165, 165, 165)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong by Alan and Dany")
font = pygame.font.SysFont(None, 30)


#game variables
live_ball = False
game_finished = False
comp_score = 0
player_score = 0
winner = 0
speed_max = 28



def draw_board():
    screen.fill(blue_dark)
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin))
#   pygame.draw.line(screen, white, (screen_width/2, margin), (screen_width/2, screen_height))
    pygame.draw.line(screen, white, ((screen_width/3) * 1, 0), (screen_width/4, margin))
    pygame.draw.line(screen, white, ((screen_width/3) * 2, 0), ((screen_width/4) * 3, margin))

def draw_text(text, font, text_color, x, y):
    text_img = font.render(text, True, text_color)
    screen.blit(text_img, (x, y))











class racket():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8


    def move(self):
        key = pygame.key.get_pressed()
        #move up
        if key[pygame.K_UP] and self.y > margin:
            self.y += -1 * self.speed
        #move down
        if key[pygame.K_DOWN] and self.y + 100 < screen_height:
            self.y += self.speed


    def ia(self):
        #move up
        if self.y + 50 > pong_ball.y + 8 and self.y > margin:
            self.y += -1 * self.speed
        #move down
        if self.y + 50 < pong_ball.y + 8 and self.y + 100 < screen_height:
            self.y += self.speed


    def draw(self):
#        pygame.draw.rect(screen, white, (self.x, self.y, 20, 100))
        screen.blit(racket_png, (self.x, self.y))
        




class ball():
    def __init__(self, x, y):
        self.reset(x, y) #variables ligne 225


    def move(self):
        #variables d'affichages
        global echanges
        global speed_ball

        #collisions detection
        #top margin
        if self.y < margin:
            self.speed_y *= -1
        #bottom screen
        if self.y + 16 > screen_height:
            self.speed_y *= -1


        #collision with player's racket
        if self.x + 16 > player_racket.x and self.y +16 > player_racket.y and self.y < player_racket.y + 100:
            self.speed_x *= -1
            #moitié haute
            if self.y + 8 < player_racket.y + 20:
                if self.speed_y > 0:
                    self.speed_y *= -1.25
                else:
                    self.speed_y *= 1.25
            #mid haut
            if self.y + 8 < player_racket.y + 20 and self.y + 8 < player_racket.y + 40:
                if self.speed_y > 0:
                    self.speed_y *= -1
                else:
                    self.speed_y *= 1
            #middle
            if self.y + 0 > player_racket.y + 40 and self.y + 0 > player_racket.y + 60:
                if self.speed_y > 0:
                    self.speed_y *= 0.5
                else:
                    self.speed_y *= -0.5
            #mid bas
            if self.y + 0 > player_racket.y + 60 and self.y + 0 > player_racket.y + 80:
                if self.speed_y > 0:
                    self.speed_y *= 1
                else:
                    self.speed_y *= -1
            #moitié basse
            if self.y + 0 > player_racket.y + 80:
                if self.speed_y > 0:
                    self.speed_y *= 1.25
                else:
                    self.speed_y *= -1.25
            
            #update des échanges
            echanges += 1

            #augmentation de la vitesse tant que la vitesse max n'est pas atteinte
            if self.speed_x > -speed_max:
                self.speed_x += -1
                if self.speed_y > 0:
                    self.speed_y += 1
                else:
                    self.speed_y += -1


        #collision with computer's racket
        if self.x < comp_racket.x + 20  and self.y + 16 > comp_racket.y and self.y < comp_racket.y + 100:
            self.speed_x *= -1
            #moitié haute
            if self.y + 8 < player_racket.y + 20:
                if self.speed_y > 0:
                    self.speed_y *= -1.25
                else:
                    self.speed_y *= 1.25
            #mid haut
            if self.y + 8 > player_racket.y + 20 and self.y + 8 > player_racket.y + 40:
                if self.speed_y > 0:
                    self.speed_y *= -1
                else:
                    self.speed_y *= 1
            #middle
            if self.y + 8 > player_racket.y + 40 and self.y + 8 > player_racket.y + 60:
                if self.speed_y > 0:
                    self.speed_y *= 0.5
                else:
                    self.speed_y *= -0.5
            #mid bas
            if self.y + 8 > player_racket.y + 60 and self.y + 8 > player_racket.y + 80:
                if self.speed_y > 0:
                    self.speed_y *= 1
                else:
                    self.speed_y *= -1
            #moitié basse
            if self.y + 8 > player_racket.y + 80:
                if self.speed_y > 0:
                    self.speed_y *= 1.25
                else:
                    self.speed_y *= -1.25

            #update des échanges
            echanges += 1

            #augmentation de la vitesse tant que la vitesse max n'est pas atteinte
            if self.speed_x < speed_max:
                self.speed_x += 1
                if self.speed_y > 0:
                    self.speed_y += 1
                else:
                    self.speed_y += -1
        
        #check if reach behind a racket
        if self.x < 0:
            self.winner = 1
        if self.x > screen_width:
            self.winner = -1

        #update ball position
        self.x += self.speed_x
        self.y += self.speed_y

        #update la valeur pour qu'elle soit toujours affiché en positif
        if self.speed_x > 0:
            speed_ball = self.speed_x
        else:
            speed_ball = -1 * self.speed_x


        return self.winner


    def draw(self):
#       pygame.draw.circle(screen, (226, 155, 22), (self.x + self.rad, self.y + self.rad), self.rad)
        screen.blit(ball_png, (self.x , self.y))
    
    #permet de relancer la balle au début de chaque manche
    def reset(self, x, y):
        self.x = x
        self.y = y
        self.rad = 8
        self.rect = (self.x, self.y, self.rad * 2, self.rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0 # 1 means player has scored, -1 for comp






#create objects
player_racket = racket(screen_width -40, screen_height // 2)
comp_racket = racket(20, screen_height // 2)
pong_ball = ball(screen_width - 70, screen_height // 2 + 70)



game_playing = True
while game_playing:

    fpsClock.tick(fps)

    #affichage de l'interface
    draw_board()
    draw_text("Ordi : " + str(comp_score), font, white, 25, 25)
    draw_text("Joueur: " + str(player_score), font, white, screen_width - 115, 25)
    if game_finished == False:
        draw_text("Échanges: " + str(echanges), font, white, screen_width // 2 - 65, 10)
        draw_text("Vitesse: " + str(speed_ball), font, white, screen_width // 2 - 50, 40)


    #draw rackets
    player_racket.draw()
    comp_racket.draw()

    if live_ball == True:
        #fait spawn la balle
        winner = pong_ball.move()
        if winner == 0:
            #déplacement des rackets
            player_racket.move()
            comp_racket.ia()
            #affichage de la balle
            pong_ball.draw()

        else:
            live_ball = False
            #pour vérifier qui a marqué le points
            if winner == 1:
                player_score += 1
            elif winner == -1:
                comp_score += 1

    #affiche une image indiquant comment lancer la manche
    if live_ball == False:
        screen.blit(directions_keys_png, (screen_width / 2 - 70, screen_height / 2 - 50))
        pass


    #affichage victoire/défaite
    if player_score == 10:
        game_finished = True
        live_ball = False
        draw_text("Victoire !", pygame.font.SysFont(None, 50), white, screen_width // 2 - 80, screen_height // 4)
    if comp_score == 10:
        game_finished = True
        live_ball = False
        draw_text("Défaite !", pygame.font.SysFont(None, 50), white, screen_width // 2 - 70, screen_height // 4)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()


        
        
        #lance la manche
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] or key[pygame.K_DOWN]:
            if live_ball == False:
                if game_finished == True:
                    player_score = 0
                    comp_score = 0
                    game_finished = False
                echanges = 0
                live_ball = True
                pong_ball.reset(screen_width - 70, screen_height // 2 + 70)


    pygame.display.update()

pygame.quit()
