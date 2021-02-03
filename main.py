import pygame
from pygame.locals import *
import sys
import random

class Rolit(object):
    #initilisation des assets du jeu
    def __init__(self):
        #initilisation de la fenetre
        pygame.init()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("Slime-it")
        icon = pygame.image.load("assets/slime.png")
        pygame.display.set_icon(icon)
        self.background = pygame.image.load("assets/wallpaper.jpg")
        self.wallpaper = pygame.image.load("assets/img/wallpaper.png")
        self.police = pygame.font.Font("assets/verdana.ttf",30)        

        #initialisation des assets

        #images du premier écran
        self.title = pygame.image.load("assets/text/title.PNG").convert_alpha()
        self.play = pygame.image.load("assets/img/play.png").convert_alpha()
        self.play_hover = pygame.image.load("assets/img/play_hover.png").convert_alpha()

        #images de la selection de la forme du plateau
        self.square = pygame.image.load("assets/text/square.PNG").convert_alpha()
        self.diamond = pygame.image.load("assets/text/diamond.PNG").convert_alpha()
        self.circle = pygame.image.load("assets/text/circle.PNG").convert_alpha()
        self.donut = pygame.image.load("assets/text/donut.PNG").convert_alpha()
        self.jar = pygame.image.load("assets/text/jar.PNG").convert_alpha()
        self.cheese = pygame.image.load("assets/text/cheese.PNG").convert_alpha()
        self.heart = pygame.image.load("assets/text/heart.PNG").convert_alpha()
        self.square_form = pygame.image.load("assets/img/form_square.PNG").convert_alpha()
        self.diamond_form= pygame.image.load("assets/img/form_diamond.png").convert_alpha()
        self.circle_form = pygame.image.load("assets/img/form_circle.png").convert_alpha()
        self.donut_form = pygame.image.load("assets/img/form_donut.PNG").convert_alpha()
        self.jar_form= pygame.image.load("assets/img/form_pot.PNG").convert_alpha()
        self.cheese_form = pygame.image.load("assets/img/form_cheese.PNG").convert_alpha()
        self.heart_form = pygame.image.load("assets/img/form_heart.PNG").convert_alpha()
        self.select_board = pygame.image.load("assets/text/select_board.PNG").convert_alpha()
        self.select_character = pygame.image.load("assets/text/select.PNG").convert_alpha()
        self.game_board = "square"
        self.game = 1
        self.game_sort = 1

        #images de la selection du nombre de joueur
        self.nb_players_2 = pygame.image.load("assets/text/2_players.png").convert_alpha()
        self.nb_players_3 = pygame.image.load("assets/text/3_players.png").convert_alpha()
        self.nb_players_4 = pygame.image.load("assets/text/4_players.png").convert_alpha()
        self.nb_players = 2
        self.current_player = 1

        #images de la selection des personnages
        self.red_1 = pygame.image.load("assets/pionts/red_1.png").convert_alpha()
        self.red_2 = pygame.image.load("assets/pionts/red_2.png").convert_alpha()
        self.red_3 = pygame.image.load("assets/pionts/red_3.png").convert_alpha()
        self.blue_1 = pygame.image.load("assets/pionts/blue_1.png").convert_alpha()
        self.blue_2 = pygame.image.load("assets/pionts/blue_2.png").convert_alpha()
        self.blue_3 = pygame.image.load("assets/pionts/blue_3.png").convert_alpha()
        self.yellow_1 = pygame.image.load("assets/pionts/yellow_1.png").convert_alpha()
        self.yellow_2 = pygame.image.load("assets/pionts/yellow_2.png").convert_alpha()
        self.yellow_3 = pygame.image.load("assets/pionts/yellow_3.png").convert_alpha()
        self.green_1 = pygame.image.load("assets/pionts/green_1.png").convert_alpha()
        self.green_2 = pygame.image.load("assets/pionts/green_2.png").convert_alpha()
        self.green_3 = pygame.image.load("assets/pionts/green_3.png").convert_alpha()
        self.rect_red = pygame.image.load("assets/rects/rect_red.png").convert_alpha()
        self.rect_blue = pygame.image.load("assets/rects/rect_blue.png").convert_alpha()
        self.rect_green = pygame.image.load("assets/rects/rect_green.png").convert_alpha()
        self.rect_yellow = pygame.image.load("assets/rects/rect_yellow.png").convert_alpha()
        self.rect_red_select = pygame.image.load("assets/rects/rect_red_select.png").convert_alpha()
        self.rect_blue_select = pygame.image.load("assets/rects/rect_blue_select.png").convert_alpha()
        self.rect_green_select = pygame.image.load("assets/rects/rect_green_select.png").convert_alpha()
        self.rect_yellow_select = pygame.image.load("assets/rects/rect_yellow_select.png").convert_alpha()
        self.red_select = pygame.image.load("assets/rects/red_select.png").convert_alpha()
        self.blue_select = pygame.image.load("assets/rects/blue_select.png").convert_alpha()
        self.green_select = pygame.image.load("assets/rects/green_select.png").convert_alpha()
        self.yellow_select = pygame.image.load("assets/rects/yellow_select.png").convert_alpha()
        self.rect_grey = pygame.image.load("assets/rects/rect_grey.png").convert_alpha()
        self.rect_grey_select = pygame.image.load("assets/rects/rect_grey_select.png").convert_alpha()
        self.grey_1 = pygame.image.load("assets/achievements/locked/grey_1.png").convert_alpha()
        self.grey_2 = pygame.image.load("assets/achievements/locked/grey_2.png").convert_alpha()
        self.grey_3 = pygame.image.load("assets/achievements/locked/grey_3.png").convert_alpha()
        self.grey_4 = pygame.image.load("assets/achievements/locked/grey_4.png").convert_alpha()
        self.grey_5 = pygame.image.load("assets/achievements/locked/grey_5.png").convert_alpha()
        self.grey_6 = pygame.image.load("assets/achievements/locked/grey_6.png").convert_alpha()
        self.grey_1_lock = pygame.image.load("assets/achievements/locked/grey_1_lock.png").convert_alpha()
        self.grey_2_lock = pygame.image.load("assets/achievements/locked/grey_2_lock.png").convert_alpha()
        self.grey_3_lock = pygame.image.load("assets/achievements/locked/grey_3_lock.png").convert_alpha()
        self.grey_4_lock = pygame.image.load("assets/achievements/locked/grey_4_lock.png").convert_alpha()
        self.grey_5_lock = pygame.image.load("assets/achievements/locked/grey_5_lock.png").convert_alpha()
        self.grey_6_lock = pygame.image.load("assets/achievements/locked/grey_6_lock.png").convert_alpha()
        self.tips_barre = pygame.image.load("assets/achievements/tips/tips_barre.PNG").convert_alpha()

        #image des écrans des règles du jeu
        self.how = pygame.image.load("assets/text/how.PNG").convert_alpha()
        self.fr_flag = pygame.image.load("assets/img/fr_flag.jpg").convert_alpha()
        self.en_flag = pygame.image.load("assets/img/en_flag.png").convert_alpha()
        self.arrow_precedent = pygame.image.load("assets/img/arrow_precedent.png").convert_alpha()
        self.arrow_suivant = pygame.image.load("assets/img/arrow_suivant.png").convert_alpha()
        self.arrow_previous = pygame.image.load("assets/img/arrow_previous.png").convert_alpha()
        self.arrow_next = pygame.image.load("assets/img/arrow_next.png").convert_alpha()
        self.skip = pygame.image.load("assets/text/skip.png").convert_alpha()
        self.passer = pygame.image.load("assets/text/passer.png").convert_alpha()
        self.plateau_screen = pygame.image.load("assets/img/plat.PNG").convert_alpha()
        self.language = "en"
        self.page = 1

        #image durant l'écran de jeu
        self.hole = pygame.image.load("assets/img/hole_.png").convert_alpha()
        self.choose_text = pygame.image.load("assets/text/choose.PNG").convert_alpha()
        self.player_1 = pygame.image.load("assets/text/player_1.png"). convert_alpha()
        self.player_1_current = pygame.image.load("assets/text/player_1_current.png"). convert_alpha()
        self.player_2 = pygame.image.load("assets/text/player_2.PNG"). convert_alpha()
        self.player_2_current = pygame.image.load("assets/text/player_2_current.png"). convert_alpha()
        self.player_3 = pygame.image.load("assets/text/player_3.PNG"). convert_alpha()
        self.player_3_current = pygame.image.load("assets/text/player_3_current.png"). convert_alpha()
        self.player_4 = pygame.image.load("assets/text/player_4.PNG"). convert_alpha()
        self.player_4_current = pygame.image.load("assets/text/player_4_current.png"). convert_alpha()
        self.score = pygame.image.load("assets/text/score.PNG"). convert_alpha()
        self.carre = pygame.image.load("assets/carre.jpg").convert_alpha()
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.score_player_3 = 0
        self.score_player_4 = 0

        #images sur l'écran final
        self.back = pygame.image.load("assets/text/back.PNG").convert_alpha()
        self.replay = pygame.image.load("assets/text/replay.PNG").convert_alpha()
        self.winner = pygame.image.load("assets/text/winner.PNG").convert_alpha()
        self.nobody = pygame.image.load("assets/text/nobody.png").convert_alpha()
        self.quit = pygame.image.load("assets/text/quit.PNG").convert_alpha()
        self.p1_text = pygame.image.load("assets/text/p1.png").convert_alpha()
        self.p2_text = pygame.image.load("assets/text/p2.png").convert_alpha()
        self.p3_text = pygame.image.load("assets/text/p3.png").convert_alpha()
        self.p4_text = pygame.image.load("assets/text/p4.png").convert_alpha()

    #affiche le premier écran du jeu et si appuye sur la manette passe à l'écran suivant
    def Set_menu(self):
        self.screen.blit(self.wallpaper,(0, 0))
        self.screen.blit(self.title,(75, 25))
        pygame.display.flip()
        while True:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            for event in pygame.event.get():
                if (event.type == QUIT):
                    sys.exit()

                if (x > 850 and y > 480):
                    self.screen.blit(self.play_hover, (850, 480))
                    pygame.display.flip()
                    if (event.type == MOUSEBUTTONDOWN):
                        self.Choose_game()
                else :
                    self.screen.blit(self.play,(850, 480))  
                    pygame.display.flip() 

    #affiche l'ecra avec les regles du jeu et son fonctionnement
    def How_to_play(self):

        while True:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            for event in pygame.event.get():
                if (event.type == QUIT):
                    sys.exit()

                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.fr_flag, (5, 5))
                self.screen.blit(self.en_flag, (50, 5))
                if (x > 5 and x < 35 and y > 5 and y < 30 and event.type == MOUSEBUTTONDOWN):
                    self.language = "fr"
                    self.page = 1
                elif (x > 50 and x < 80 and  y > 5 and y < 30 and event.type == MOUSEBUTTONDOWN):
                    self.language = "en"
                    self.page = 1
                
                if (self.language == "fr"):
                    if (self.page == 1):
                        if (x > 580 and x < 695 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 2
                        self.Fr_p1()
                    elif (self.page == 2):
                        if (x > 580 and x < 695 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 3
                        if (x > 270 and x < 420 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 1
                        self.Fr_p2()
                    elif (self.page == 3):
                        if (x > 580 and x < 695 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 4
                        if (x > 270 and x < 420 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 2
                        self.Fr_p3()
                    elif (self.page == 4):
                        if (x > 580 and x < 695 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 5
                        if (x > 270 and x < 420 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 3
                        self.Fr_p4()
                    elif (self.page == 5):
                        if (x > 270 and x < 420 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 4
                        self.Fr_p5()
                    if (x > 910 and y < 35 and event.type == MOUSEBUTTONDOWN):
                        self.Choose_game()

                elif (self.language == "en"):
                    if (self.page == 1):
                        if (x > 580 and x < 695 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 2
                        self.En_p1()
                    elif (self.page == 2):
                        if (x > 580 and x < 695 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 3
                        if (x > 270 and x < 420 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 1
                        self.En_p2()
                    elif (self.page == 3):
                        if (x > 580 and x < 695 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 4
                        if (x > 270 and x < 420 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 2
                        self.En_p3()
                    elif (self.page == 4):
                        if (x > 580 and x < 695 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 5
                        if (x > 270 and x < 420 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 3
                        self.En_p4()
                    elif (self.page == 5):
                        if (x > 270 and x < 420 and y > 480 and y < 590 and event.type == MOUSEBUTTONDOWN):
                            self.page = 4
                        self.En_p5()

                    if (x > 945 and y < 35 and event.type == MOUSEBUTTONDOWN):
                        self.Choose_game()
            
            pygame.display.flip()

    #affiche l'ecran avec les regles du jeu et son fonctionnement EN_page1
    def En_p1(self):
        self.screen.blit(self.arrow_next, (580, 480))
        self.screen.blit(self.skip, (945, 8))
        self.screen.blit(self.police.render(open("assets/en/en_1_1.txt", 'r').read(), True, pygame.Color("#000000")), (20, 90))
        self.screen.blit(self.police.render(open("assets/en/en_1_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(self.plateau_screen, (235, 180))

    #affiche l'ecran avec les regles du jeu et son fonctionnement EN_page2
    def En_p2(self):
        self.screen.blit(self.arrow_previous, (270, 480))
        self.screen.blit(self.arrow_next, (580, 480))
        self.screen.blit(self.skip, (945, 8))
        self.screen.blit(self.police.render(open("assets/en/en_2_1.txt", 'r').read(), True, pygame.Color("#000000")), (20, 90))
        self.screen.blit(self.police.render(open("assets/en/en_2_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(pygame.image.load("assets/img/play_.PNG").convert_alpha(), (350, 180))

    #affiche l'ecran avec les regles du jeu et son fonctionnement EN_page3
    def En_p3(self):
        self.screen.blit(self.arrow_previous, (270, 480))
        self.screen.blit(self.arrow_next, (580, 480))
        self.screen.blit(self.skip, (945, 8))
        self.screen.blit(self.police.render(open("assets/en/en_3_1.txt", 'r').read(), True, pygame.Color("#000000")), (15, 90))
        self.screen.blit(self.police.render(open("assets/en/en_3_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(pygame.image.load("assets/img/chara.PNG").convert_alpha(), (75, 200))
        self.screen.blit(pygame.image.load("assets/img/chara_2.PNG").convert_alpha(), (525, 200))

    #affiche l'ecran avec les regles du jeu et son fonctionnement EN_page4
    def En_p4(self):
        self.screen.blit(self.arrow_previous, (270, 480))
        self.screen.blit(self.arrow_next, (580, 480))
        self.screen.blit(self.skip, (945, 8))
        self.screen.blit(self.police.render(open("assets/en/en_4_1.txt", 'r').read(), True, pygame.Color("#000000")), (15, 90))
        self.screen.blit(self.police.render(open("assets/en/en_4_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(self.police.render(open("assets/en/en_4_3.txt", 'r').read(), True, pygame.Color("#000000")), (20, 150))
        self.screen.blit(self.police.render(open("assets/en/en_4_4.txt", 'r').read(), True, pygame.Color("#000000")), (20, 195))
        self.screen.blit(self.police.render(open("assets/en/en_4_5.txt", 'r').read(), True, pygame.Color("#000000")), (20, 225))
        self.screen.blit(self.police.render(open("assets/en/en_4_6.txt", 'r').read(), True, pygame.Color("#000000")), (20, 255))

    #affiche l'ecran avec les regles du jeu et son fonctionnement EN_page5
    def En_p5(self):
        self.screen.blit(self.arrow_previous, (270, 480))
        self.screen.blit(self.skip, (945, 8))
        self.screen.blit(self.police.render(open("assets/en/en_5_1.txt", 'r').read(), True, pygame.Color("#000000")), (15, 90))
        self.screen.blit(self.police.render(open("assets/en/en_5_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(pygame.image.load("assets/img/game.PNG").convert_alpha(), (50, 180))
        self.screen.blit(pygame.image.load("assets/img/game_1.PNG").convert_alpha(), (250, 180))
        self.screen.blit(pygame.image.load("assets/img/game_2.PNG").convert_alpha(), (470, 200))
        self.screen.blit(pygame.image.load("assets/img/game_3.PNG").convert_alpha(), (730, 200))

    #affiche l'ecran avec les regles du jeu et son fonctionnement FR_page1
    def Fr_p1(self):
        self.screen.blit(self.arrow_suivant, (580, 480))
        self.screen.blit(self.passer, (910, 8))
        self.screen.blit(self.police.render(open("assets/fr/fr_1_1.txt", 'r').read(), True, pygame.Color("#000000")), (20, 90))
        self.screen.blit(self.police.render(open("assets/fr/fr_1_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(self.plateau_screen, (235, 180))

    #affiche l'ecran avec les regles du jeu et son fonctionnement FR_page2
    def Fr_p2(self):
        self.screen.blit(self.arrow_precedent, (270, 480))
        self.screen.blit(self.arrow_suivant, (580, 480))
        self.screen.blit(self.passer, (910, 8))
        self.screen.blit(self.police.render(open("assets/fr/fr_2_1.txt", 'r').read(), True, pygame.Color("#000000")), (15, 90))
        self.screen.blit(self.police.render(open("assets/fr/fr_2_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(pygame.image.load("assets/img/play_.PNG").convert_alpha(), (350, 180))

    #affiche l'ecran avec les regles du jeu et son fonctionnement FR_page3
    def Fr_p3(self):
        self.screen.blit(self.arrow_precedent, (270, 480))
        self.screen.blit(self.arrow_suivant, (580, 480))
        self.screen.blit(self.passer, (910, 8))
        self.screen.blit(self.police.render(open("assets/fr/fr_3_1.txt", 'r').read(), True, pygame.Color("#000000")), (15, 90))
        self.screen.blit(self.police.render(open("assets/fr/fr_3_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(pygame.image.load("assets/img/chara.PNG").convert_alpha(), (75, 200))
        self.screen.blit(pygame.image.load("assets/img/chara_2.PNG").convert_alpha(), (525, 200))

    #affiche l'ecran avec les regles du jeu et son fonctionnement FR_page4
    def Fr_p4(self):
        self.screen.blit(self.arrow_precedent, (270, 480))
        self.screen.blit(self.arrow_suivant, (580, 480))
        self.screen.blit(self.passer, (910, 8))
        self.screen.blit(self.police.render(open("assets/fr/fr_4_1.txt", 'r').read(), True, pygame.Color("#000000")), (15, 90))
        self.screen.blit(self.police.render(open("assets/fr/fr_4_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(self.police.render(open("assets/fr/fr_4_3.txt", 'r').read(), True, pygame.Color("#000000")), (20, 150))
        self.screen.blit(self.police.render(open("assets/fr/fr_4_4.txt", 'r').read(), True, pygame.Color("#000000")), (20, 195))
        self.screen.blit(self.police.render(open("assets/fr/fr_4_5.txt", 'r').read(), True, pygame.Color("#000000")), (20, 225))
        self.screen.blit(self.police.render(open("assets/fr/fr_4_6.txt", 'r').read(), True, pygame.Color("#000000")), (20, 255))

    #affiche l'ecran avec les regles du jeu et son fonctionnement FR_page5
    def Fr_p5(self):
        self.screen.blit(self.arrow_precedent, (270, 480))
        self.screen.blit(self.passer, (910, 8))
        self.screen.blit(self.police.render(open("assets/fr/fr_5_1.txt", 'r').read(), True, pygame.Color("#000000")), (15, 90))
        self.screen.blit(self.police.render(open("assets/fr/fr_5_2.txt", 'r').read(), True, pygame.Color("#000000")), (20, 120))
        self.screen.blit(pygame.image.load("assets/img/game.PNG").convert_alpha(), (50, 180))
        self.screen.blit(pygame.image.load("assets/img/game_1.PNG").convert_alpha(), (250, 180))
        self.screen.blit(pygame.image.load("assets/img/game_2.PNG").convert_alpha(), (470, 200))
        self.screen.blit(pygame.image.load("assets/img/game_3.PNG").convert_alpha(), (730, 200))

    #écran permettant de choisir la forme du plateau du jeu
    def Choose_game(self):
        self.screen.blit(self.background,(0, 0))
        self.screen.blit(self.how, (7, 565))
        self.screen.blit(self.select_board, (180, 15))
        self.screen.blit(self.square, (92, 250))
        self.screen.blit(self.square_form, (90, 125))
        self.screen.blit(self.diamond, (250, 250))
        self.screen.blit(self.diamond_form, (270, 125))
        self.screen.blit(self.circle, (452, 250))
        self.screen.blit(self.circle_form, (450, 125))
        self.screen.blit(self.donut, (625, 250))
        self.screen.blit(self.donut_form, (620, 125))
        self.screen.blit(self.jar, (822, 250))
        self.screen.blit(self.jar_form, (800, 125))
        self.screen.blit(self.cheese, (264, 450))
        self.screen.blit(self.cheese_form, (270, 325))
        self.screen.blit(self.heart, (627, 450))
        self.screen.blit(self.heart_form, (620, 325))

        pygame.display.flip()
        while True:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            for event in pygame.event.get():
                if (event.type == QUIT):
                    sys.exit()

                if (x > 90 and x < 190 and y > 125 and y < 225 or x > 92 and x < 185 and y > 250 and y < 275):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.game = 1
                        self.Nbr_player()
                elif (x > 270 and x < 370 and y > 125 and y < 225 or x > 250 and x < 350 and y > 250 and y < 275):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.game = 2
                        self.Nbr_player()
                elif (x > 452 and x < 552 and y > 125 and y < 225 or x > 452 and x < 547 and y > 250 and y < 275):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.game = 3
                        self.Nbr_player()
                elif (x > 620 and x < 720 and y > 125 and y < 225 or x > 625 and x < 712 and y > 250 and y < 275):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.game = 4
                        self.Nbr_player()
                elif (x > 800 and x < 900 and y > 125 and y < 225 or x > 822 and x < 877 and y > 250 and y < 275):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.game = 5
                        self.Nbr_player()
                elif (x > 270 and x < 370 and y > 325 and y < 425 or x > 264 and x < 376 and y > 450 and y < 475):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.game = 6
                        self.Nbr_player()
                elif (x > 620 and x < 720 and y > 325 and y < 425 or x > 627 and x < 715 and y > 450 and y < 475):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.game = 7
                        self.Nbr_player()
                elif (x > 350 and x < 400 and y > 500 and y < 525):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.game = 8
                        self.Nbr_player()

                if (x > 7 and x < 154 and y > 565 and y < 600):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.How_to_play()

    #ecran de selection du nombre de joueurs
    def Nbr_player(self):
        self.screen.blit(self.background,(0, 0))
        self.screen.blit(self.how, (7, 565))
        self.screen.blit(self.back, (5,5))
        self.screen.blit(self.choose_text, (280, 10))
        self.screen.blit(self.nb_players_2, (400, 200))
        self.screen.blit(self.nb_players_3, (400, 300))
        self.screen.blit(self.nb_players_4, (400, 400))
        pygame.display.flip()

        while True:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            for event in pygame.event.get():
                if (event.type == QUIT):
                    sys.exit()

                if (event.type == MOUSEBUTTONDOWN):
                    if (x > 400 and x < 650 and y > 200 and y < 260):
                        self.nb_players = 2
                        self.Choose_character()
                    elif (x > 400 and x < 650 and y > 300 and y < 360):
                        self.nb_players = 3
                        self.Choose_character()
                    elif (x > 400 and x < 650 and y > 400 and y < 460):
                        self.nb_players = 4
                        self.Choose_character()   
                    elif (x > 5 and x < 100 and y > 5 and y < 100):
                        self.Choose_game()
                    if (x > 7 and x < 154 and y > 565 and y < 600):
                        self.How_to_play()
                        
    #ecran de sélection des personnages et lance l'initialisation du terrain
    def Choose_character(self):
        self.screen.blit(self.background,(0, 0))
        self.screen.blit(self.how, (7, 565))
        self.screen.blit(self.select_character,(250, 15))
        self.screen.blit(self.back, (5, 5))
        self.screen.blit(self.rect_red,(120, 110))
        self.screen.blit(self.red_1, (170, 150))
        self.screen.blit(self.red_2, (270, 150))
        self.screen.blit(self.red_3, (370, 150))
        self.screen.blit(self.rect_blue,(530, 110))
        self.screen.blit(self.blue_1, (580, 150))
        self.screen.blit(self.blue_2, (680, 150))
        self.screen.blit(self.blue_3, (780, 150))
        self.screen.blit(self.rect_yellow,(120, 280))
        self.screen.blit(self.yellow_1, (170, 320))
        self.screen.blit(self.yellow_2, (270, 320))
        self.screen.blit(self.yellow_3, (370, 320))
        self.screen.blit(self.rect_green,(530, 280))
        self.screen.blit(self.green_1, (580, 320))
        self.screen.blit(self.green_2, (680, 320))
        self.screen.blit(self.green_3, (780, 320))
        self.player_1_color = "no"
        self.player_2_color = "no"
        self.player_3_color = "no"
        self.player_4_color = "no"
        self.nb_game_read = open("assets/achievements/nb_game.txt", 'r')
        self.nb_game = self.nb_game_read.read()
        self.nb_game_read.close()
        self.nb_game = int(self.nb_game)
        self.board_square_read = open("assets/achievements/board_square.txt", 'r')
        self.board_square = self.board_square_read.read()
        self.board_square_read.close()
        self.board_diamond_read = open("assets/achievements/board_diamond.txt", 'r')
        self.board_diamond = self.board_diamond_read.read()
        self.board_diamond_read.close()
        self.board_circle_read = open("assets/achievements/board_circle.txt", 'r')
        self.board_circle = self.board_circle_read.read()
        self.board_circle_read.close()
        self.board_donut_read = open("assets/achievements/board_donut.txt", 'r')
        self.board_donut = self.board_donut_read.read()
        self.board_donut_read.close()
        self.board_jar_read = open("assets/achievements/board_jar.txt", 'r')
        self.board_jar = self.board_jar_read.read()
        self.board_jar_read.close()
        self.board_cheese_read = open("assets/achievements/board_cheese.txt", 'r')
        self.board_cheese = self.board_cheese_read.read()
        self.board_cheese_read.close()
        self.board_heart_read = open("assets/achievements/board_heart.txt", 'r')
        self.board_heart = self.board_heart_read.read()
        self.board_heart_read.close()
        self.board_slime_read = open("assets/achievements/board_slime.txt", 'r')
        self.board_slime = self.board_slime_read.read()
        self.board_slime_read.close()
        self.score_record_read = open("assets/achievements/score_record.txt", 'r')
        self.score_record = self.score_record_read.read()
        self.score_record_read.close()
        self.all_players_read = open("assets/achievements/all_players.txt", 'r')
        self.all_players = self.all_players_read.read()
        self.all_players_read.close()
        self.equality_read = open("assets/achievements/equality.txt", 'r')
        self.equality = self.equality_read.read()
        self.equality_read.close()
        
        self.screen.blit(self.rect_grey,(250, 440))
        if (self.nb_game >= 5):
            self.screen.blit(self.grey_1,(280, 480))
            self.grey_1_block = "false"
        else:
            self.screen.blit(self.grey_1_lock,(280, 480))
            self.grey_1_block = "true"
        if (self.board_square == "true" and self.board_diamond == "true" and self.board_circle == "true" and self.board_donut == "true" and self.board_jar == "true" and self.board_cheese == "true"):
            self.screen.blit(self.grey_2,(350, 480))
            self.grey_2_block = "false"
        else:
            self.screen.blit(self.grey_2_lock,(350, 480))
            self.grey_2_block = "true"
        if (self.score_record == "true"):
            self.screen.blit(self.grey_3,(425, 480))
            self.grey_3_block = "false"
        else:
            self.screen.blit(self.grey_3_lock,(425, 480))
            self.grey_3_block = "true"
        if (self.all_players == "true"):
            self.screen.blit(self.grey_4,(500, 480))
            self.grey_4_block = "false"
        else:
            self.screen.blit(self.grey_4_lock,(500, 480))
            self.grey_4_block = "true"
        if (self.equality == "true"):
            self.screen.blit(self.grey_5,(580, 480))
            self.grey_5_block = "false"
        else:
            self.screen.blit(self.grey_5_lock,(580, 480))
            self.grey_5_block = "true"
        if (self.board_slime == "true"):
            self.screen.blit(self.grey_6,(660, 480))
            self.grey_6_block = "false"
        else:
            self.screen.blit(self.grey_6_lock,(660, 480))
            self.grey_6_block = "true"
        self.font = pygame.font.Font("assets/verdana.ttf",20)

        self.current_player = 1

        pygame.display.flip() 
 
        while True:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            piont = "null"
            color = "null"
            for event in pygame.event.get():
                if (event.type == QUIT):
                    sys.exit()

                if (x > 120 and x < 470 and y > 110 and y < 240):
                    color = "red"
                    if (x > 170 and x < 220 and y > 150 and y < 200 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.red_1
                        self.screen.blit(self.rect_red_select, (120, 110))
                        self.screen.blit(self.red_select, (162, 142))
                    if (x > 270 and x < 320 and y > 150 and y < 200 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.red_2
                        self.screen.blit(self.rect_red_select, (120, 110))
                        self.screen.blit(self.red_select, (262, 142))
                    if (x > 370 and x < 420 and y > 150 and y < 200 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.red_3
                        self.screen.blit(self.rect_red_select, (120, 110))
                        self.screen.blit(self.red_select, (362, 142))
                if (x > 530 and x < 880 and y > 110 and y < 240):
                    color = "blue"
                    if (x > 580 and x < 630 and y > 150 and y < 200 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.blue_1
                        self.screen.blit(self.rect_blue_select, (530, 110))
                        self.screen.blit(self.blue_select, (572, 142))
                    if (x > 680 and x < 730 and y > 150 and y < 200 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.blue_2
                        self.screen.blit(self.rect_blue_select, (530, 110))
                        self.screen.blit(self.blue_select, (672, 142))
                    if (x > 780 and x < 830 and y > 150 and y < 200 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.blue_3
                        self.screen.blit(self.rect_blue_select, (530, 110))
                        self.screen.blit(self.blue_select, (772, 142))
                if (x > 120 and x < 470 and y > 280 and y < 410):
                    color = "yellow"
                    if (x > 170 and x < 220 and y > 320 and y < 470 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.yellow_1
                        self.screen.blit(self.rect_yellow_select, (120, 280))
                        self.screen.blit(self.yellow_select, (162, 312))
                    if (x > 270 and x < 320 and y > 320 and y < 470 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.yellow_2
                        self.screen.blit(self.rect_yellow_select, (120, 280))
                        self.screen.blit(self.yellow_select, (262, 312))
                    if (x > 370 and x < 420 and y > 320 and y < 470 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.yellow_3
                        self.screen.blit(self.rect_yellow_select, (120, 280))
                        self.screen.blit(self.yellow_select, (362, 312))
                if (x > 530 and x < 880 and y > 280 and y < 410):
                    color = "green"
                    if (x > 580 and x < 630 and y > 320 and y < 470 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.green_1
                        self.screen.blit(self.rect_green_select, (530, 280))
                        self.screen.blit(self.green_select, (572, 312))
                    if (x > 680 and x < 730 and y > 320 and y < 470 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.green_2
                        self.screen.blit(self.rect_green_select, (530, 280))
                        self.screen.blit(self.green_select, (672, 312))
                    if (x > 780 and x < 830 and y > 320 and y < 470 and event.type == MOUSEBUTTONDOWN and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        piont = self.green_3
                        self.screen.blit(self.rect_green_select, (530, 280))
                        self.screen.blit(self.green_select, (772, 312))

                if (x > 250 and x < 750 and y > 440 and y < 570):
                    color = "grey"
                    if (x > 280 and x < 330 and y > 480 and y < 530 and event.type == MOUSEBUTTONDOWN):
                        if (self.grey_1_block == "false"):
                            piont = self.grey_1
                            color = "grey_1"
                            self.screen.blit(self.rect_grey_select, (272, 472))
                        else:
                            self.screen.blit(self.tips_barre, (117, 410))
                            self.screen.blit(self.font.render(open("assets/achievements/tips/tips_grey_1.txt", 'r').read(), True, pygame.Color("#000000")), (360, 410))
                    if (x > 350 and x < 405 and y > 480 and y < 523 and event.type == MOUSEBUTTONDOWN):
                        if (self.grey_2_block == "false"):
                            piont = self.grey_2
                            color = "grey_2"
                            self.screen.blit(self.rect_grey_select, (344, 472))
                        else:
                            self.screen.blit(self.tips_barre, (117, 410))
                            self.screen.blit(self.font.render(open("assets/achievements/tips/tips_grey_2.txt", 'r').read(), True, pygame.Color("#000000")), (335, 410))
                    if (x > 425 and x < 480 and y > 480 and y < 520 and event.type == MOUSEBUTTONDOWN):
                        if (self.grey_3_block == "false"):
                            piont = self.grey_3
                            color = "grey_3"
                            self.screen.blit(self.rect_grey_select, (419, 472))
                        else:
                            self.screen.blit(self.tips_barre, (117, 410))
                            self.screen.blit(self.font.render(open("assets/achievements/tips/tips_grey_3.txt", 'r').read(), True, pygame.Color("#000000")), (335, 410))
                    if (x > 500 and x < 550 and y > 480 and y < 520 and event.type == MOUSEBUTTONDOWN):
                        if (self.grey_4_block == "false"):
                            piont = self.grey_4
                            color = "grey_4"
                            self.screen.blit(self.rect_grey_select, (494, 472))
                        else:
                            self.screen.blit(self.tips_barre, (117, 410))
                            self.screen.blit(self.font.render(open("assets/achievements/tips/tips_grey_4.txt", 'r').read(), True, pygame.Color("#000000")), (325, 410))

                    if (x > 580 and x < 630 and y > 480 and y < 520 and event.type == MOUSEBUTTONDOWN):
                        if (self.grey_5_block == "false"):
                            piont = self.grey_5
                            color = "grey_5"
                            self.screen.blit(self.rect_grey_select, (575, 472))
                        else:
                            self.screen.blit(self.tips_barre, (117, 410))
                            self.screen.blit(self.font.render(open("assets/achievements/tips/tips_grey_5.txt", 'r').read(), True, pygame.Color("#000000")), (325, 410))

                    if (x > 660 and x < 710 and y > 480 and y < 520 and event.type == MOUSEBUTTONDOWN):
                        if (self.grey_6_block == "false"):
                            piont = self.grey_6
                            color = "grey_6"
                            self.screen.blit(self.rect_grey_select, (655, 472))
                        else:
                            self.screen.blit(self.tips_barre, (117, 410))
                            self.screen.blit(self.font.render(open("assets/achievements/tips/tips_grey_6.txt", 'r').read(), True, pygame.Color("#000000")), (325, 410))
                
                if (x > 5 and x < 100 and y > 5 and y < 100 and event.type == MOUSEBUTTONDOWN):
                        self.Nbr_player()
        
                pygame.display.flip()
                
                if (color != "null" and piont != "null"):
                    if (self.current_player == 1):
                        self.player_1_piont = piont
                        self.player_1_color = color
                        self.current_player = self.current_player + 1
                    elif (self.current_player == 2 and color != self.player_1_color):
                        self.player_2_piont = piont
                        self.player_2_color = color
                        self.current_player = self.current_player + 1
                    elif (self.current_player == 3 and color != self.player_1_color and color != self.player_2_color):
                        self.player_3_piont = piont
                        self.player_3_color = color
                        self.current_player = self.current_player + 1
                    elif (self.current_player == 4 and color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
                        self.player_4_piont = piont
                        self.player_4_color = color
                        self.current_player = self.current_player + 1

                if (self.current_player > self.nb_players):
                    self.current_player = 1
                    if (self.nb_players == 2):
                        self.Attribute_player_3()
                    elif(self.nb_players == 3):
                        self.Attribute_player_4()
                        
                    if (self.game == 1):
                        self.Game_square()
                    elif (self.game == 2):
                        self.Game_diamond()
                    elif (self.game == 3):
                        self.Game_circle()
                    elif (self.game == 4):
                        self.Game_donut()
                    elif (self.game == 5):
                        self.Game_pot()
                    elif (self.game == 6):
                        self.Game_fromage()
                    elif (self.game == 7):
                        self.Game_heart()
                    elif (self.game == 8):
                        self.Game_slime()
                if (x > 7 and x < 154 and y > 565 and y < 600):
                    if (event.type == MOUSEBUTTONDOWN):
                        self.How_to_play()

    #definit le player 3 dans une partie à 2 joueurs
    def Attribute_player_3(self):
        color = "red"
        if (color != self.player_1_color and color != self.player_2_color):
            self.player_3_color = color
            self.player_3_piont = self.red_1
        color = "blue"
        if (color != self.player_1_color and color != self.player_2_color):
            self.player_3_color = color
            self.player_3_piont = self.blue_1
        color = "yellow"
        if (color != self.player_1_color and color != self.player_2_color):
            self.player_3_color = color
            self.player_3_piont = self.yellow_1
        color = "green"
        if (color != self.player_1_color and color != self.player_2_color):
            self.player_3_color = color
            self.player_3_piont = self.green_1
        self.Attribute_player_4()

    #definit le player 4 dans une partie à 2 ou 3 joueurs
    def Attribute_player_4(self):
        color = "red"
        if (color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
            self.player_4_color = color
            self.player_4_piont = self.red_1
        color = "blue"
        if (color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
            self.player_4_color = color
            self.player_4_piont = self.blue_1
        color = "yellow"
        if (color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
            self.player_4_color = color
            self.player_4_piont = self.yellow_1
        color = "green"
        if (color != self.player_1_color and color != self.player_2_color and color != self.player_3_color):
            self.player_4_color = color
            self.player_4_piont = self.green_1

    #cas du choix du plateau en 8x8
    def Game_square(self):
        self.nb_column = 8
        self.nb_line = 8
        self.screen.blit(self.background,(0, 0))
        self.line = [15, 85, 155, 225, 295, 365, 435, 505]
        self.column = [15, 85, 155, 225, 295, 365, 435, 505]

        self.color_pionts = []
        for i in range(self.nb_line):
            self.color_pionts.append(["null"] * self.nb_column)

        pygame.display.flip()

        for y in range (len(self.column)):
            for x in range (len(self.line)):
                self.screen.blit(self.hole, (self.line[x], self.column[y]))
        pygame.display.flip()
        self.game_sort = 1
        self.game_board = "square"
        self.Start_game()

    #cas du choix du plateau en diamond
    def Game_diamond(self):
        self.nb_column = 8
        self.nb_line = 8
        self.screen.blit(self.background,(0, 0))
        self.line = [15, 85, 155, 225, 295, 365, 435, 505]
        self.column = [15, 85, 155, 225, 295, 365, 435, 505]
        self.color_pionts = []
        for i in range(self.nb_line):
            self.color_pionts.append(["null"] * self.nb_column)

        self.color_pionts[0][0] = "none"
        self.color_pionts[0][7] = "none"
        self.color_pionts[7][0] = "none"
        self.color_pionts[7][7] = "none"    

        pygame.display.flip()

        for y in range (len(self.column)):
            for x in range (len(self.line)):
                if (self.color_pionts[y][x] == "null"):
                    self.screen.blit(self.hole, (self.line[x], self.column[y]))
        pygame.display.flip()
        self.game_sort = 1
        self.game_board = "diamond"
        self.Start_game()

    #cas du choix du plateau en circle
    def Game_circle(self):
        self.nb_column = 8
        self.nb_line = 8
        self.screen.blit(self.background,(0, 0))
        self.line = [15, 85, 155, 225, 295, 365, 435, 505]
        self.column = [15, 85, 155, 225, 295, 365, 435, 505]
        self.color_pionts = []
        for i in range(self.nb_line):
            self.color_pionts.append(["null"] * self.nb_column)

        self.color_pionts[0][0] = "none"
        self.color_pionts[0][1] = "none"
        self.color_pionts[0][6] = "none"
        self.color_pionts[1][0] = "none"
        self.color_pionts[1][7] = "none"
        self.color_pionts[0][7] = "none"
        self.color_pionts[6][0] = "none"
        self.color_pionts[6][7] = "none"
        self.color_pionts[7][0] = "none"
        self.color_pionts[7][1] = "none"
        self.color_pionts[7][7] = "none"  
        self.color_pionts[7][6] = "none"  

        pygame.display.flip()

        for y in range (len(self.column)):
            for x in range (len(self.line)):
                if (self.color_pionts[y][x] == "null"):
                    self.screen.blit(self.hole, (self.line[x], self.column[y]))
        pygame.display.flip()
        self.game_sort = 1
        self.game_board = "circle"
        self.Start_game()

        #cas du choix du plateau en circle
    
    #cas du choix du plateau en donut
    def Game_donut(self):
        self.nb_column = 8
        self.nb_line = 8
        self.screen.blit(self.background,(0, 0))
        self.line = [15, 85, 155, 225, 295, 365, 435, 505]
        self.column = [15, 85, 155, 225, 295, 365, 435, 505]
        self.color_pionts = []
        for i in range(self.nb_line):
            self.color_pionts.append(["null"] * self.nb_column)

        self.color_pionts[3][3] = "none"
        self.color_pionts[3][4] = "none"
        self.color_pionts[4][3] = "none"
        self.color_pionts[4][4] = "none"

        pygame.display.flip()

        for y in range (len(self.column)):
            for x in range (len(self.line)):
                if (self.color_pionts[y][x] == "null"):
                    self.screen.blit(self.hole, (self.line[x], self.column[y]))
        pygame.display.flip()
        self.game_sort = 2
        self.game_board = "donut"
        self.Start_game()

        #cas du choix du plateau en circle
  
    #cas du choix du plateau en pot
    def Game_pot(self):
        self.nb_column = 8
        self.nb_line = 8
        self.screen.blit(self.background,(0, 0))
        self.line = [15, 85, 155, 225, 295, 365, 435, 505]
        self.column = [15, 85, 155, 225, 295, 365, 435, 505]
        self.color_pionts = []
        for i in range(self.nb_line):
            self.color_pionts.append(["null"] * self.nb_column)

        self.color_pionts[2][0] = "none"
        self.color_pionts[3][0] = "none"
        self.color_pionts[2][7] = "none"
        self.color_pionts[3][7] = "none"

        pygame.display.flip()

        for y in range (len(self.column)):
            for x in range (len(self.line)):
                if (self.color_pionts[y][x] == "null"):
                    self.screen.blit(self.hole, (self.line[x], self.column[y]))
        pygame.display.flip()
        self.game_sort = 1
        self.game_board = "jar"
        self.Start_game()
  
    #cas du choix du plateau en fromage
    def Game_fromage(self):
        self.nb_column = 8
        self.nb_line = 8
        self.screen.blit(self.background,(0, 0))
        self.line = [15, 85, 155, 225, 295, 365, 435, 505]
        self.column = [15, 85, 155, 225, 295, 365, 435, 505]
        self.color_pionts = []
        for i in range(self.nb_line):
            self.color_pionts.append(["null"] * self.nb_column)

        self.color_pionts[2][2] = "none"
        self.color_pionts[2][5] = "none"
        self.color_pionts[5][2] = "none"
        self.color_pionts[5][5] = "none"

        pygame.display.flip()

        for y in range (len(self.column)):
            for x in range (len(self.line)):
                if (self.color_pionts[y][x] == "null"):
                    self.screen.blit(self.hole, (self.line[x], self.column[y]))
        pygame.display.flip()
        self.game_sort = 1
        self.game_board = "cheese"
        self.Start_game()

    #cas du choix du plateau en coeur
    def Game_heart(self):
        self.nb_column = 8
        self.nb_line = 8
        self.screen.blit(self.background,(0, 0))
        self.line = [15, 85, 155, 225, 295, 365, 435, 505]
        self.column = [15, 85, 155, 225, 295, 365, 435, 505]
        self.color_pionts = []
        for i in range(self.nb_line):
            self.color_pionts.append(["null"] * self.nb_column)

        self.color_pionts[0][0] = "none"
        self.color_pionts[0][3] = "none"
        self.color_pionts[0][4] = "none"
        self.color_pionts[0][7] = "none"
        self.color_pionts[4][0] = "none"
        self.color_pionts[4][7] = "none"
        self.color_pionts[5][0] = "none"
        self.color_pionts[5][7] = "none"
        self.color_pionts[5][1] = "none"
        self.color_pionts[5][6] = "none"
        self.color_pionts[6][0] = "none"
        self.color_pionts[6][7] = "none"
        self.color_pionts[6][1] = "none"
        self.color_pionts[6][6] = "none"
        self.color_pionts[6][2] = "none"
        self.color_pionts[6][5] = "none"
        self.color_pionts[7][0] = "none"
        self.color_pionts[7][7] = "none"
        self.color_pionts[7][1] = "none"
        self.color_pionts[7][6] = "none"

        pygame.display.flip()

        for y in range (len(self.column)):
            for x in range (len(self.line)):
                if (self.color_pionts[y][x] == "null"):
                    self.screen.blit(self.hole, (self.line[x], self.column[y]))
        pygame.display.flip()
        self.game_sort = 1
        self.game_board = "heart"
        self.Start_game()

    #cas du choix du plateau en Slime
    def Game_slime(self):
        self.nb_column = 8
        self.nb_line = 8
        self.screen.blit(self.background,(0, 0))
        self.line = [15, 85, 155, 225, 295, 365, 435, 505]
        self.column = [45, 115, 185, 255, 325, 395, 465, 535]
        self.color_pionts = []
        for i in range(self.nb_line):
            self.color_pionts.append(["null"] * self.nb_column)

        self.color_pionts[0][0] = "none"
        self.color_pionts[0][1] = "none"
        self.color_pionts[0][6] = "none"
        self.color_pionts[0][7] = "none"
        self.color_pionts[1][0] = "none"
        self.color_pionts[1][7] = "none"
        
        self.color_pionts[6][0] = "none"
        self.color_pionts[6][7] = "none"
        
        self.color_pionts[3][2] = "none"
        self.color_pionts[3][5] = "none"

        self.color_pionts[7][0] = "none"
        self.color_pionts[7][1] = "none"
        self.color_pionts[7][2] = "none"
        self.color_pionts[7][3] = "none"
        self.color_pionts[7][4] = "none"
        self.color_pionts[7][5] = "none"
        self.color_pionts[7][6] = "none"
        self.color_pionts[7][7] = "none"

        pygame.display.flip()

        for y in range (len(self.column)):
            for x in range (len(self.line)):
                if (self.color_pionts[y][x] == "null"):
                    self.screen.blit(self.hole, (self.line[x], self.column[y]))
        pygame.display.flip()
        self.game_sort = 1
        self.game_board = "slime"
        self.Start_game()

    #affiche les 4pionts de chaque couleur au milieu du plateau
    def Start_game(self):
        if (self.game_sort == 1):
            self.color_pionts[3][3] = self.player_1_color
            self.screen.blit(self.player_1_piont, (self.line[3] + 5, self.column[3] + 10))
            self.color_pionts[3][4] = self.player_2_color
            self.screen.blit(self.player_2_piont, (self.line[4] + 5, self.column[3] + 10))
            self.color_pionts[4][3] = self.player_3_color
            self.screen.blit(self.player_3_piont, (self.line[3] + 5, self.column[4] + 10))
            self.color_pionts[4][4] = self.player_4_color
            self.screen.blit(self.player_4_piont, (self.line[4] + 5, self.column[4] + 10))
        elif (self.game_sort == 2):
            self.color_pionts[2][2] = self.player_1_color
            self.screen.blit(self.player_1_piont, (self.line[2] + 5, self.column[2] + 10))
            self.color_pionts[2][5] = self.player_2_color
            self.screen.blit(self.player_2_piont, (self.line[5] + 5, self.column[2] + 10))
            self.color_pionts[5][2] = self.player_3_color
            self.screen.blit(self.player_3_piont, (self.line[2] + 5, self.column[5] + 10))
            self.color_pionts[5][5] = self.player_4_color
            self.screen.blit(self.player_4_piont, (self.line[5] + 5, self.column[5] + 10))
        
        pygame.display.flip()

        while True:
            self.Verif_click()

    #vérifie si l'emplacement est libre et pose le piont et si un des 8trous autour est rempli et affiche le score
    def Verif_click(self):
        self.screen.blit(self.player_1, (650, 50))
        self.screen.blit(self.player_1_piont, (850, 40))
        self.screen.blit(self.score, (670, 100))
        self.screen.blit(self.carre, (760, 95))
        self.screen.blit(self.police.render(str(self.score_player_1), True, pygame.Color("#000000")), (760, 90))
        self.screen.blit(self.player_2, (650, 200))
        self.screen.blit(self.player_2_piont, (850, 190))
        self.screen.blit(self.score, (670, 250))
        self.screen.blit(self.carre, (760, 245))
        self.screen.blit(self.police.render(str(self.score_player_2), True, pygame.Color("#000000")), (760, 240))
        if (self.nb_players == 3 or self.nb_players == 4):
            self.screen.blit(self.player_3, (650, 350))
            self.screen.blit(self.player_3_piont, (850, 340))
            self.screen.blit(self.score, (670, 400))
            self.screen.blit(self.carre, (760, 395))
            self.screen.blit(self.police.render(str(self.score_player_3), True, pygame.Color("#000000")), (760, 390))
        if (self.nb_players == 4):
            self.screen.blit(self.player_4, (650, 500))
            self.screen.blit(self.player_4_piont, (850, 490))
            self.screen.blit(self.score, (670, 550))
            self.screen.blit(self.carre, (760, 545))
            self.screen.blit(self.police.render(str(self.score_player_4), True, pygame.Color("#000000")), (760, 540))
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        ok = "false"
        if (self.current_player > self.nb_players):
            self.current_player = 1
        if (self.current_player == 1):
            self.piont = self.player_1_piont
            self.color = self.player_1_color
            self.screen.blit(self.player_1_current, (650, 50))
        elif (self.current_player == 2):
            self.color = self.player_2_color
            self.piont = self.player_2_piont
            self.screen.blit(self.player_2_current, (650, 200))
        elif (self.current_player == 3):
            self.color = self.player_3_color
            self.piont = self.player_3_piont
            self.screen.blit(self.player_3_current, (650, 350))
        elif (self.current_player == 4):
            self.color = self.player_4_color
            self.piont = self.player_4_piont
            self.screen.blit(self.player_4_current, (650, 500))
        pygame.display.flip()

        for event in pygame.event.get():
            if (event.type == QUIT):
                    sys.exit()

            if (event.type == MOUSEBUTTONDOWN):
                for i in range (self.nb_line):
                    for j in range (self.nb_column):
                        if (x > self.line[i] and x < self.line[i] + 50 and y > self.column[j] and y < self.column[j] + 50):
                            if (self.color_pionts[j][i] == "null" and self.color_pionts[j][i] != "none"):
                                if (j-1 >= 0):
                                    if (self.color_pionts[j-1][i] != "null" and self.color_pionts[j-1][i] != "none"):
                                        ok = "true"
                                if (j-1 >= 0 and i-1 >= 0):
                                    if (self.color_pionts[j-1][i-1] != "null" and self.color_pionts[j-1][i-1] != "none"):
                                        ok = "true"
                                if (j-1 >= 0 and i+1 < 8):
                                    if (self.color_pionts[j-1][i+1] != "null" and self.color_pionts[j-1][i+1] != "none"):
                                        ok = "true"
                                if (j+1 < 8):
                                    if (self.color_pionts[j+1][i] != "null" and self.color_pionts[j+1][i] != "none"):
                                        ok = "true"
                                if (j+1 <8 and i-1 >= 0):
                                    if (self.color_pionts[j+1][i-1] != "null" and self.color_pionts[j+1][i-1] != "none"):
                                        ok = "true"
                                if (j+1 < 8 and i+1 < 8):
                                    if (self.color_pionts[j+1][i+1] != "null" and self.color_pionts[j+1][i+1] != "none"):
                                        ok = "true"
                                if (i-1 >= 0):
                                    if (self.color_pionts[j][i-1] != "null" and self.color_pionts[j][i-1] != "none"):
                                        ok = "true"
                                if (i+1 < 8):
                                    if (self.color_pionts[j][i+1] != "null" and self.color_pionts[j][i+1] != "none"): 
                                        ok ="true"
                                if (ok =="true"):
                                    self.screen.blit(self.piont, (self.line[i] + 8, self.column[j] + 10))
                                    self.color_pionts[j][i] = self.color
                                    self.j = j
                                    self.i = i
                                    self.Check_colors()
                                    pygame.display.flip()
                                    self.current_player = self.current_player + 1
                                    self.Count_score()
                                    self.End_check()
                                    return
                                else:
                                    return
                            else:
                                return
  
    #verifie les cases alentours de celle posée et change les pionts si necessaires
    def Check_colors(self):
        k = 1
        j = self.j
        i = self.i
        same = "false"
        ### Verification de la ligne gauche
        while (i - k >= 0):
            if (self.color_pionts[j][i-k] == self.color):
                same = "true"
                break
            if (self.color_pionts[j][i-k] == "null" or self.color_pionts[j][i-k] == "none"):
                break
            if (self.color_pionts[j][i-k] != self.color and self.color_pionts[j][i-k] != "null"):
                k = k + 1
        if (same == "true"):
            while (k > 1):
                k = k - 1
                self.color_pionts[j][i-k] = self.color
                self.screen.blit(self.hole, (self.line[i-k], self.column[j]))
                self.screen.blit(self.piont, (self.line[i-k] + 8, self.column[j] + 10))
        ### Verification de la ligne droite
        same = "false"
        k = 1
        while (i + k < 8):
            if (self.color_pionts[j][i+k] == self.color):
                same = "true"
                break
            if (self.color_pionts[j][i+k] == "null" or self.color_pionts[j][i+k] == "none"):
                break
            if (self.color_pionts[j][i+k] != self.color and self.color_pionts[j][i+k] != "null"):
                k = k + 1
        if (same == "true"):
            while (k > 1):
                k = k - 1
                self.color_pionts[j][i+k] = self.color
                self.screen.blit(self.hole, (self.line[i+k], self.column[j]))
                self.screen.blit(self.piont, (self.line[i+k] + 8, self.column[j] + 10))
        ### Verification ligne du haut
        same = "false"
        k = 1
        while (j - k >= 0):
            if (self.color_pionts[j-k][i] == self.color):
                same = "true"
                break
            if (self.color_pionts[j-k][i] == "null" or self.color_pionts[j-k][i] == "none"):
                break
            if (self.color_pionts[j-k][i] != self.color and self.color_pionts[j-k][i] != "null"):
                k = k + 1
        if (same == "true"):
            while (k > 1):
                k = k - 1
                self.color_pionts[j-k][i] = self.color
                self.screen.blit(self.hole, (self.line[i], self.column[j-k]))
                self.screen.blit(self.piont, (self.line[i] + 8, self.column[j-k] + 10))
        ### Verification ligne du bas
        same = "false"
        k = 1
        while (j + k < 8):
            if (self.color_pionts[j+k][i] == self.color):
                same = "true"
                break
            if (self.color_pionts[j+k][i] == "null" or self.color_pionts[j+k][i] == "none"):
                break
            if (self.color_pionts[j+k][i] != self.color and self.color_pionts[j+k][i] != "null"):
                k = k + 1
        if (same == "true"):
            while (k > 1):
                k = k - 1
                self.color_pionts[j+k][i] = self.color
                self.screen.blit(self.hole, (self.line[i], self.column[j+k]))
                self.screen.blit(self.piont, (self.line[i] + 8, self.column[j+k] + 10))
        ### Verification diagonale haut gauche
        same = "false"
        k = 1
        while (j - k >= 0 and i - k >= 0):
            if (self.color_pionts[j-k][i-k] == self.color):
                same = "true"
                break
            if (self.color_pionts[j-k][i-k] == "null" or self.color_pionts[j-k][i-k] == "none"):
                break
            if (self.color_pionts[j-k][i-k] != self.color and self.color_pionts[j-k][i-k] != "null"):
                k = k + 1
        if (same == "true"):
            while (k > 1):
                k = k - 1
                self.color_pionts[j-k][i-k] = self.color
                self.screen.blit(self.hole, (self.line[i-k], self.column[j-k]))
                self.screen.blit(self.piont, (self.line[i-k] + 8, self.column[j-k] + 10))
        ### Verification diagonale haut droite
        same = "false"
        k = 1
        while (j - k >= 0 and i + k < 8):
            if (self.color_pionts[j-k][i+k] == self.color):
                same = "true"
                break
            if (self.color_pionts[j-k][i+k] == "null" or self.color_pionts[j-k][i+k] == "none"):
                break
            if (self.color_pionts[j-k][i+k] != self.color and self.color_pionts[j-k][i+k] != "null"):
                k = k + 1
        if (same == "true"):
            while (k > 1):
                k = k - 1
                self.color_pionts[j-k][i+k] = self.color
                self.screen.blit(self.hole, (self.line[i+k], self.column[j-k]))
                self.screen.blit(self.piont, (self.line[i+k] + 8, self.column[j-k] + 10))
        ### Verification diagonale bas droite
        same = "false"
        k = 1
        while (j + k < 8 and i + k < 8):
            if (self.color_pionts[j+k][i+k] == self.color):
                same = "true"
                break
            if (self.color_pionts[j+k][i+k] == "null" or self.color_pionts[j+k][i+k] == "none"):
                break
            if (self.color_pionts[j+k][i+k] != self.color and self.color_pionts[j+k][i+k] != "null"):
                k = k + 1
        if (same == "true"):
            while (k > 1):
                k = k - 1
                self.color_pionts[j+k][i+k] = self.color
                self.screen.blit(self.hole, (self.line[i+k], self.column[j+k]))
                self.screen.blit(self.piont, (self.line[i+k] + 8, self.column[j+k] + 10))
        ### Verification diagonale bas gauche
        same = "false"
        k = 1
        while (j + k < 8 and i - k >= 0):
            if (self.color_pionts[j+k][i-k] == self.color):
                same = "true"
                break
            if (self.color_pionts[j+k][i-k] == "null" or self.color_pionts[j+k][i-k] == "none"):
                break
            if (self.color_pionts[j+k][i-k] != self.color and self.color_pionts[j+k][i-k] != "null"):
                k = k + 1
        if (same == "true"):
            while (k > 1):
                k = k - 1
                self.color_pionts[j+k][i-k] = self.color
                self.screen.blit(self.hole, (self.line[i-k], self.column[j+k]))
                self.screen.blit(self.piont, (self.line[i-k] + 8, self.column[j+k] + 10))
        
    #Compte le score pour chaque couleur
    def Count_score(self):
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.score_player_3 = 0
        self.score_player_4 = 0

        for i in range(self.nb_line):
            for j in range(self.nb_column):
                if (self.color_pionts[i][j] == self.player_1_color):
                    self.score_player_1 = self.score_player_1 + 1
                elif (self.color_pionts[i][j] == self.player_2_color):
                    self.score_player_2 = self.score_player_2 + 1
                elif (self.color_pionts[i][j] == self.player_3_color):
                    self.score_player_3 = self.score_player_3 + 1
                elif (self.color_pionts[i][j] == self.player_4_color):
                    self.score_player_4 = self.score_player_4 + 1
                    
    #verifie si toutes les cases sont remplis et passe a la fenetre finale
    def End_check(self):
        cases = 0
        for i in range(self.nb_line):
            for j in range(self.nb_column):
                if (self.color_pionts[i][j] != "null"):
                    cases = cases + 1
                if (cases == 64):
                    self.End_screen()

    #affiche l'écran final permettant de rejouer
    def End_screen(self):
        self.screen.blit(self.background,(0, 0))
        self.screen.blit(self.replay, (845, 545))
        self.screen.blit(self.quit, (915, 5))
        self.screen.blit(self.winner, (350, 100))
        self.screen.blit(self.p1_text, (5, 455))
        self.screen.blit(self.police.render(str(self.score_player_1), True, pygame.Color("#000000")), (35, 445))
        self.screen.blit(self.p2_text, (5, 490))
        self.screen.blit(self.police.render(str(self.score_player_2), True, pygame.Color("#000000")), (35, 485))
        self.screen.blit(self.p3_text, (5, 525))
        self.screen.blit(self.police.render(str(self.score_player_3), True, pygame.Color("#000000")), (35, 520))
        self.screen.blit(self.p4_text, (5, 560))
        self.screen.blit(self.police.render(str(self.score_player_4), True, pygame.Color("#000000")), (35, 555))
        if (self.score_player_1 > self.score_player_2 and self.score_player_1 > self.score_player_3 and self.score_player_1 > self.score_player_4): 
            self.screen.blit(self.player_1, (400, 180))
            self.screen.blit(self.player_1_piont, (600, 170))
        elif (self.score_player_2 > self.score_player_1 and self.score_player_2 > self.score_player_3 and self.score_player_2 > self.score_player_4): 
            self.screen.blit(self.player_2, (400, 180))
            self.screen.blit(self.player_2_piont, (600, 170))
        elif (self.score_player_3 > self.score_player_2 and self.score_player_3 > self.score_player_1 and self.score_player_3 > self.score_player_4): 
            self.screen.blit(self.player_3, (400, 180))
            self.screen.blit(self.player_3_piont, (600, 170))
        elif (self.score_player_4 > self.score_player_2 and self.score_player_4 > self.score_player_3 and self.score_player_4 > self.score_player_1): 
            self.screen.blit(self.player_4, (400, 180))
            self.screen.blit(self.player_4_piont, (600, 170))
        else:
            self.screen.blit(self.nobody, (410, 190))
        pygame.display.flip()

        self.nb_game = self.nb_game + 1
        self.nb_game = str(self.nb_game)
        self.nb_game_write = open("assets/achievements/nb_game.txt", 'w')
        self.nb_game_write.write(self.nb_game)
        self.nb_game_write.close()

        if (self.game_board == "square"):
            self.board_square_write = open("assets/achievements/board_square.txt", 'w')
            self.board_square_write.write("true")
            self.board_square_write.close()
        if (self.game_board == "diamond"):
            self.board_diamond = open("assets/achievements/board_diamond.txt", 'w')
            self.board_diamond.write("true")
            self.board_diamond.close()
        if (self.game_board == "circle"):
            self.board_circle = open("assets/achievements/board_circle.txt", 'w')
            self.board_circle.write("true")
            self.board_circle.close()
        if (self.game_board == "donut"):
            self.board_donut = open("assets/achievements/board_donut.txt", 'w')
            self.board_donut.write("true")
            self.board_donut.close()
        if (self.game_board == "cheese"):
            self.board_cheese = open("assets/achievements/board_cheese.txt", 'w')
            self.board_cheese.write("true")
            self.board_cheese.close()
        if (self.game_board == "heart"):
            self.board_heart = open("assets/achievements/board_heart.txt", 'w')
            self.board_heart.write("true")
            self.board_heart.close()
        if (self.game_board == "slime"):
            self.board_slime = open("assets/achievements/board_slime.txt", 'w')
            self.board_slime.write("true")
            self.board_slime.close()
        if (self.score_player_1 > 50 or self.score_player_2 > 50 or self.score_player_3 > 50 or self.score_player_4 > 50):
            self.score_record_write = open("assets/achievements/score_record.txt", 'w')
            self.score_record_write.write("true")
            self.score_record_write.close()
        if (self.nb_players == 4):
            self.all_players_write = open("assets/achievements/all_players.txt", 'w')
            self.all_players_write.write("true")
            self.all_players_write.close()
        self.Score_equality()

        while True:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            for event in pygame.event.get():
                if (event.type == QUIT):
                    sys.exit()

                if (x > 915 and y < 50 and event.type == MOUSEBUTTONDOWN):
                    sys.exit()
                
                if (x > 845 and x < 975 and y > 545 and y < 585 and event.type == MOUSEBUTTONDOWN):
                    self.score_player_1 = 0
                    self.score_player_2 = 0
                    self.score_player_3 = 0
                    self.score_player_4 = 0
                    self.Choose_game()

    #verifie l'achievement des egalites
    def Score_equality(self):
        equality = "false"
        if (self.score_player_1 == self.score_player_2):
            equality = "true"
        if (self.nb_players == 3):
            if (self.score_player_3 == self.score_player_1 or self.score_player_3 == self.score_player_2):
                equality = "true"
        if (self.nb_players == 4):
            if (self.score_player_4 == self.score_player_1 or self.score_player_4 == self.score_player_2 or self.score_player_4 == self.score_player_3):
                equality = "true"
        if (equality == "true"):
            self.equality_write = open("assets/achievements/equality.txt", 'w')
            self.equality_write.write("true")
            self.equality_write.close()
            
Rolit().Set_menu()