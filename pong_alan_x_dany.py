import pygame

pygame.init()

#preload
right_click_png = pygame.image.load("mouse_click-gauche.png")
racket_png = pygame.image.load("racket.png")
ball_png = pygame.image.load("ball.png")
background = pygame.image.load("background.png")

#screen size
screen_width = 800
screen_height = 560
background = pygame.transform.scale(background, (screen_width, screen_height))




fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong by Alan and Dany")


#font
font = pygame.font.SysFont(None, 30)





#game variable
live_ball = False
margin = 70
comp_score = 0
player_score = 0
fps = 60
winner = 0
speed_max = 28
game_finished = False
angle = 0

#printing varaibles
echanges = 0
speed_ball = 0

#colors
blue_dark = (9, 10, 16)
white = (165, 165, 165)


def draw_board():
    screen.fill(blue_dark)
#    screen.blit(background, (0, 0))
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin))
#    pygame.draw.line(screen, white, (screen_width/2, margin), (screen_width/2, screen_height))
    pygame.draw.line(screen, white, ((screen_width/3) * 1, 0), (screen_width/4, margin))
    pygame.draw.line(screen, white, ((screen_width/3) * 2, 0), ((screen_width/4) * 3, margin))



def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


























class racket():
    def __init__(self, x, y):
        self.x = x
        self.y = y
#        self.rect = pygame.rect(self.x, self.y, 20, 100)
        self.speed = 8

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.y > margin:
            self.y += -1 * self.speed
#            self.rect.move_ip(0, -1 * self.speed)
        if key[pygame.K_DOWN] and self.y + 100 < screen_height:
            self.y += self.speed
#            self.rect.move_ip(0, self.speed)

    def ia(self):
        #move up
        if self.y + 50 > pong_ball.y + 8 and self.y > margin:
            self.y += -1 * self.speed
        #move down
        if self.y + 50 < pong_ball.y + 8 and self.y + 100 < screen_height:
            self.y += self.speed



    def draw(self):
#        pygame.draw.rect(screen, white, self.rect))
#        pygame.draw.rect(screen, white, (self.x, self.y, 20, 100))
        screen.blit(racket_png, (self.x, self.y))
        




class ball():
    def __init__(self, x, y):
        self.reset(x, y)


    def move(self):
        #collision detection
        #top margin 
        if self.y < margin:
            self.speed_y *= -1
        #bottom screen 
        if self.y + 16 > screen_height:
            self.speed_y *= -1


        #collision with racket
#        if self.rect.colliderect(player_racket) or self.rect.colliderect(comp_racket):
#            self.speed_x *= -1
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
                
            global echanges
            echanges += 1
            if self.speed_x > -speed_max:
                self.speed_x += -1
                if self.speed_y > 0:
                    self.speed_y += 1
                else:
                    self.speed_y += -1

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

            

            echanges += 1
            if self.speed_x < speed_max:
                self.speed_x += 1
                if self.speed_y > 0:
                    self.speed_y += 1
                else:
                    self.speed_y += -1
        
        #check if reach under a racket
        if self.x < 0:
            self.winner = 1
        if self.x > screen_width:
            self.winner = -1

        #update ball position
        self.x += self.speed_x
        self.y += self.speed_y



        global speed_ball
        if self.speed_x > 0:
            speed_ball = self.speed_x
        else:
            speed_ball = -1 * self.speed_x


        return self.winner



    def draw(self):
#        pygame.draw.circle(screen, white, (self.rect.x + self.rad, self.rect.y + self.rad), self.rad)
#        pygame.draw.circle(screen, (226, 155, 22), (self.x + self.rad, self.y + self.rad), self.rad)
        screen.blit(ball_png, (self.x , self.y))
    
    def reset(self, x, y):
        self.x = x
        self.y = y
        self.rad = 8
        self.rect = (self.x, self.y, self.rad * 2, self.rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0 # 1 means player has scored, -1 for comp






























#create rackets
player_racket = racket(screen_width -40, screen_height // 2)
comp_racket = racket(20, screen_height // 2)

#create ball
pong_ball = ball(screen_width - 70, screen_height // 2 + 70)



run = True
while run:

    fpsClock.tick(fps)



    draw_board()
    draw_text("Ordi : " + str(comp_score), font, white, 25, 25)
    draw_text("Joueur: " + str(player_score), font, white, screen_width - 115, 25)
    if game_finished == False:
        draw_text("Échanges: " + str(echanges), font, white, screen_width // 2 - 65, 10)
        draw_text("Vitesse: " + str(speed_ball), font, white, screen_width // 2 - 50, 40)


    #draw racket
    player_racket.draw()
    comp_racket.draw()

    if live_ball == True:
        #move ball
        winner = pong_ball.move()
        if winner == 0:
            #move racket
            player_racket.move()
            comp_racket.ia()
            #draw ball
            pong_ball.draw()

        else:
            live_ball = False
            if winner == 1:
                player_score += 1
            elif winner == -1:
                comp_score += 1

    if live_ball == False:
        screen.blit(right_click_png, (screen_width / 2 - 45, screen_height / 2 - 50))


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
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False :
            if game_finished == True:
                player_score = 0
                comp_score = 0
                game_finished = False
            echanges = 0
            live_ball = True
            pong_ball.reset(screen_width - 70, screen_height // 2 + 70)




    pygame.display.update()

pygame.quit()







#all fonts existing

"""
['lato', 'tlwgtypo', 'accanthisadfstd', 'latinmodernmonolight', 'dejavuserif', 'notosansthai', 'notosansmodi', 'urwbookman', 'ebgaramondinitialsfill1', 'kalapi', 'rekha', 'notosanspahawhhmong', 'tlwgtypewriter', 'comfortaa', 'latinmodernmono', 'roboto', 'notosansoldnortharabian', 'dejavusansmono', 'ubuntumono', 'notosanscypriot', 'notosanspsalterpahlavi', 'rachana', 'notosanswarangciti', 'liberationmono', 'gilliusadfno2', 'foulisgreek', 'stix', 'stixintegralsup', 'notosanslisu', 'notosansmongolian', 'tinos', 'stixintegralsupd', 'anjalioldlipi', 'dejavusans', 'opensans', 'notosanslimbu', 'texgyrebonum', 'notoserifcjksc', 'latinmodernroman', 'keraleeyam', 'garuda', 'nimbusmonops', 'notosansugaritic', 'notosansmono', 'notosanskhmer', 'texgyrecursor', 'notoserifcjktc', 'notosansarmenian', 'notosansgujarati', 'freesans', 'p052', 'liberationsansnarrow', 'notosansoriya', 'gfscomplutum', 'notosanscaucasianalbanian', 'notoserifhebrew', 'cousine', 'notosansinscriptionalparthian', 'texgyretermes', 'berenisadfpro', 'kacstfarsi', 'padaukbook', 'nimbussans', 'rasa', 'notosansmayannumerals', 'notosanstakri', 'carlito', 'notonaskharabic', 'stixnonunicode', 'liberationsans', 'nimbussansnarrow', 'notoseriftelugu', 'stixsizetwosym', 'notosanscuneiform', 'berenisadfpromath', 'padmaa', 'stixvariants', 'universalisadfstd', 'notoserifcjkjp', 'notoserifcjkkr', 'ebgaramondsc', 'freeserif', 'stixintegralssm', 'c059', 'latinmodernmonocaps', 'latinmodernsans', 'uroob', 'yrsa', 'texgyreadventor', 'mrykacstqurn', 'tlwgtypist', 'kacstone', 'gilliusadf', 'freemono', 'notoseriftamil', 'gentiumplus', 'notosanstibetan', 'notosanssyriac', 'gayathri', 'notosanscjkjp', 'arimo', 'notosanscjkhk', 'notosanscjkkr', 'loma', 'notosanstifinagh', 'robotocondensed', 'notoserifdisplay', 'notoserifbalinese', 'texgyrescholamath', 'gentiumpluscompact', 'notosansmyanmar', 'liberationserif', 'padauk', 'notoserifgurmukhi', 'notosansmarchen', 'kacstdigital', 'notosanssaurashtra', 'ubuntu', 'texgyrepagellamath', 'notoserifahom', 'latinmodernmonoproplight', 'kacstpen', 'notoserifbengali', 'linuxlibertineo', 'notosanscjksc', 'laksaman', 'chilanka', 'notosanscjktc', 'kinnari', 'notosansrunic', 'lohitgurmukhi', 'gentiumbookbasic', 'tlwgmono', 'latinmodernromandunhill', 'notosansnewtailue', 'notokufiarabic', 'texgyrepagella', 'latinmodernsansdemicond', 'junicode', 'waree', 'texgyreheros', 'linuxlibertineinitialso', 'sarai', 'notosansoldsogdian', 'ebgaramond', 'notosansnko', 'manjari', 'notoserifgujarati', 'umpush', 'fontawesome', 'stixintegralsd', 'notoserifarmenian', 'go', 'notosanscanadianaboriginal', 'notosans', 'latinmodernromancaps', 'z003', 'urwgothic', 'mitramono', 'notosansbhaiksuki', 'notoserifkhmer', 'notosansjavanese', 'sawasdee', 'texgyreheroscn', 'notoserifmalayalam', 'notosansdisplay', 'notosanslinearb', 'notosanskannada', 'lohitbengali', 'kacstscreen', 'notosanslycian', 'lobstertwo', 'kacstart', 'notosansshavian', 'notosansbengali', 'gentiumalt', 'stixsizethreesym', 'notosanskhudawadi', 'notosansyi', 'notosanslineara', 'saab', 'samyaktamil', 'lohitgujarati', 'cabin', 'notosansolchiki', 'notosansinscriptionalpahlavi', 'd050000l', 'notoserifdogra', 'lohitassamese', 'accanthisadfstdno2', 'notosanslydian', 'notosanstagalog', 'latinmodernsansquotation', 'linuxlibertinemonoo', 'gfsneohellenic', 'notosansosmanya', 'notosanshanunoo', 'notosansbamum', 'notosansdevanagari', 'texgyreschola', 'notosansethiopic', 'norasi', 'notosansoldsoutharabian', 'notosanselbasan', 'notoserifmyanmar', 'notosansgeorgian', 'ebgaramondinitialsfill2', 'notoseriftangut', 'purisa', 'caladea', 'latinmodernmath', 'gfsartemisia', 'notosansgrantha', 'gfsolga', 'notosansbassavah', 'nimbusroman', 'khmeros', 'cantarell', 'latinmodernmonoprop', 'muktinarrow', 'notoserifethiopic', 'notosansgurmukhi', 'notoserifsinhala', 'asanamath', 'stixintegralsupsm', 'notosanskharoshthi', 'notosansrejang', 'ebgaramondinitials', 'notosansmeeteimayek', 'lohitdevanagari', 'dejavumathtexgyre', 'gentiumbasic', 'kalimati', 'notoserif', 'stixgeneral', 'droidsansfallback', 'notoserifdevanagari', 'notosanstaiviet', 'notosansduployan', 'notosansbuhid', 'notosansthaana', 'notosansmro', 'khmerossystem', 'notosanstamil', 'accanthisadfstdno3', 'latinmodernromanunslanted', 'notosansdeseret', 'notosansadlamunjoined', 'notosansosage', 'texgyrebonummath', 'notosanscham', 'notoseriftamilslanted', 'lohittelugu', 'notosanslepcha', 'notosanslao', 'gosmallcaps', 'notosansmiao', 'latinmodernromanslanted', 'notoserifgeorgian', 'linuxbiolinumo', 'notosansoldturkic', 'notoseriflao', 'notosansnewa', 'texgyretermesmath', 'notomusic', 'notosansegyptianhieroglyphs', 'notosansimperialaramaic', 'lohitodia', 'karumbi', 'latinmodernromandemi', 'notosanssorasompeng', 'notosansmath', 'notosanstirhuta', 'phetsarathot', 'kacstdecorative', 'lklug', 'ebgaramond12allsc', 'notosansbuginese', 'notosansolditalic', 'notoserifthai', 'gomono', 'notosanssylotinagri', 'lohittamilclassical', 'notosansavestan', 'notosanssinhala', 'notosansoldpermic', 'notosanspalmyrene', 'notosansmalayalam', 'notosanssundanese', 'texgyrechorus', 'jamrul', 'stixsizeonesym', 'notosanskhojki', 'linuxlibertinedisplayo', 'pagul', 'stixmath', 'lohittamil', 'likhan', 'notonastaliqurdu', 'notosanspaucinhau', 'notosansgothic', 'notosanssamaritan', 'notosanscoptic', 'samyakdevanagari', 'notosanskaithi', 'notosanstagbanwa', 'notosansmeroitic', 'gentium', 'notosansmonocjktc', 'latinmodernmonolightcond', 'notoserifkannada', 'gfsdidot', 'lohitmalayalam', 'notosansmonocjksc', 'notosansmonocjkkr', 'notosansmonocjkhk', 'notosansarabic', 'notosansmonocjkjp', 'stixsizefoursym', 'notosanstamilsupplement', 'stixsizefivesym', 'kacsttitlel', 'notosansoldpersian', 'notosansanatolianhieroglyphs', 'notosanssymbols2', 'notosansmanichaean', 'notosansbatak', 'notosanssharada', 'notosanstaitham', 'notosanshatran', 'navilu', 'ubuntucondensed', 'tibetanmachineuni', 'notosansmultani', 'gomedium', 'kacstletter', 'standardsymbolsps', 'ori1uni', 'raghumalayalamsans', 'opensymbol', 'aakar', 'notosanscarian', 'notomono', 'notosanschakma', 'notoseriftibetan', 'texgyredejavumath', 'notosanscherokee', 'notosanshanifirohingya', 'notosansbrahmi', 'lohitkannada', 'dyuthi', 'meera', 'notosanssymbols', 'notosansmendekikakui', 'notosansvai', 'pothana2000', 'gubbi', 'gargi', 'notosanstelugu', 'notocoloremoji', 'notosanshebrew', 'samyakgujarati', 'notosansmandaic', 'chandas', 'kacstbook', 'kacstposter', 'notosanskayahli', 'notosansmahajani', 'padmaabold11', 'notosansoldhungarian', 'notosansindicsiyaqnumbers', 'sahadeva', 'opensanscondensed', 'notosansadlam', 'kacstqurn', 'linuxbiolinumkeyboardo', 'gfssolomos', 'kacstnaskh', 'notosanssiddham', 'notosansogham', 'notosanstaile', 'notosansphagspa', 'nakula', 'notosansphoenician', 'latinmodernmonoslanted', 'samanata', 'vemana2000', 'ani', 'suruma', 'kacsttitle', 'samyakmalayalam', 'notosansglagolitic', 'kacstoffice', 'notosansnabataean', 'abyssinicasil']"""
