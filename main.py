#importowanie bibliotek
import pygame #pyagme
import random #random

#wywołanie pygame
pygame.init()

#zmienne do uruchomienia
FPS = 60 #FPS gry
run = True #włączenie okna gry
WIDTH = 400 #szerokość okna
HEIGHT = 600 #wysokość okna
clock = pygame.time.Clock() #wywołanie fps'ów
pygame.display.set_caption("Flappy Duck") #nadanie tutułu okna
window = pygame.display.set_mode((WIDTH, HEIGHT)) #okno gry

#stany gry
pauze = False
menu = True
game = False
game_over = False #czy gameover Jest true lub false

#zmienne gracza
duck_x = 100 #miejsce gracza w osi x
duck_y = 250 #miejsce gracza w osi y
duck_speed = 5 #prędkość gracza
duck_gravity = 0.25 #gravitacja
duck_velocity_y = 0 #nwm
point = 0 #punkty

#zmienne obu rur
pip_x = 400
pip_y = -70
pip_speed = 3
pip2_x = 400
pip2_y = 500
pip_gap = 450

#ładowanie obrazków
pip_u_image = pygame.image.load('assets/images/rurson_g.png') #obrazek dolnej rury
pip_d_image = pygame.image.load('assets/images/rurson_d.png')#obrazek górnej rury
alien_image = pygame.image.load('assets/images/ufo.png') #obrazek statku wroga
duck_image = pygame.image.load('assets/images/Ptaszor.png') #obrazek kaczki
knight_image = pygame.image.load('assets/images/rycerz.png') #obrazek rycerza wroga
bocian_image = pygame.image.load('assets/images/bocian.png') #obrazek bociana wroga
space_background_image = pygame.image.load('assets/images/tło1.png') #obrazek kosmiczne tło
background_image = pygame.image.load('assets/images/podstawowe_tlo.png') #obrazek podstawowe tło
gray_background_image = pygame.image.load('assets/images/podstawowe_tlo_stare.webp') #obrazek podstawowe tło

#skalowanie obrazków
scaled_pipu_image = pygame.transform.scale(pip_u_image, (100, 400))
scaled_pipd_image = pygame.transform.scale(pip_d_image, (100, 400))
scaled_alien_image = pygame.transform.scale(alien_image, (64, 64)) #statek wroga
scaled_duck_image = pygame.transform.scale(duck_image, (64, 64)) #kaczka
scaled_knight_image = pygame.transform.scale(knight_image, (64, 64)) #rycerz wróg
scaled_bocian_image = pygame.transform.scale(bocian_image, (90, 64)) #bocian wróg
scaled_background_image = pygame.transform.scale(background_image, (400, 600)) #tło
scaled_gray_background_image = pygame.transform.scale(gray_background_image, (400, 600)) #tło

#kolory
WHITE = (255, 255, 255) #kolor biały
RED = (255, 0, 0) #kolor czerwony

#czcionki
czcionka = pygame.font.Font('assets/font/wendy.ttf', 70) #robienie czcionki
game_over_teskt = czcionka.render("PRZEGRALES!", True, RED) 
points_tekst = czcionka.render(f"Punkty: {point}", True, RED)

#pozycja kursora
mouse_pos = pygame.mouse.get_pos() #pobueranie pozycji myszy

#pętla gierki
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #sprawdzanie czy gracz żyje
    if game == True:

        #poruszanie się rur
        pip_x -= pip_speed
        pip2_x -= pip_speed

        #sprawdzanie naciśniętych przycisków
        keys = pygame.key.get_pressed() #zmienna czy przycisk został naciśnięty
        if keys[pygame.K_SPACE]: #sprawdzanie czy spacja została wciśnięta
            duck_velocity_y = -duck_speed 
        if keys[pygame.K_ESCAPE]:
            pauze = True

        if pip_x <= -100:
            pip_x = 400
            pip_y = random.randint(-200, 0)
            pip2_y = pip_y + pip_gap
            pip2_x = 400 
            point += 1

        #grawitacja gracza
        duck_velocity_y += duck_gravity
        duck_y += duck_velocity_y

        #hitboxy wszystkiego
        pip_hitbox = pygame.Rect(pip_x, pip_y, 90, 335) #hitboxy rury
        pip2_hitbox = pygame.Rect(pip2_x, pip2_y + 70, 90, 100) #hitboxy rury 2
        duck_hitbox = pygame.Rect(duck_x, duck_y, 64, 64) #hitboxy kaczki

        #sprawdzanie kolizji
        if duck_hitbox.colliderect(pip_hitbox): #sprawdzanie czy kaczka nie dotkneła rury
            game_over = True
        if duck_hitbox.colliderect(pip2_hitbox): #sprawdzanie czy kaczka nie dotkneła rury 2
            game_over = True

    # Rysowanie tła, kaczki i inne
    window.blit(scaled_gray_background_image, (0, 0)) #wklejenie tła na okno
    # Obracanie kaczki w zależności od prędkości
    rotation_angle = -duck_velocity_y * 5  # negatywny mnożnik, żeby przy unoszeniu obracała się do góry
    rotation_angle = max(-30, min(60, rotation_angle))  # ograniczenie kąta między -30 a 60 stopni

    #przewracanie kaczki
    rotated_duck_image = pygame.transform.rotate(scaled_duck_image, rotation_angle) #sprawianie że kaczka się przewraca
    duck_rect = rotated_duck_image.get_rect(center=(duck_x + 32, duck_y + 32))  #nwm

    #rysowanie obiektów
    window.blit(rotated_duck_image, duck_rect.topleft) #rysowanie kaczki
    window.blit(scaled_pipu_image, (pip_x, pip_y)) #rysowanie rury górnej
    window.blit(scaled_pipd_image, (pip2_x, pip2_y)) #rysowanie rury dolnej
    window.blit(points_tekst, (20, 10)) #rysowanie liczby punktów

    #tryb gry menu
    if menu == True:
        window.fill((0, 0, 0))
        play_button_hitbox = pygame.Rect(WIDTH//2 -50, 350, 100, 64)
        play_button = pygame.draw.rect(window, (0, 255, 0), play_button_hitbox)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #sprawdzanie czy lewy przycisk myszy wciśnięty
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                game = True
                menu = False

    if pauze == True:
        window.fill((0, 0, 0))
        game = False
        unpause_button_hitbox = pygame.Rect(150, 250, 100, 64)
        pygame.draw.rect(window, (0, 255, 0), (unpause_button_hitbox))
        menu_button_hitbox = pygame.Rect(150, 350, 100, 64)
        pygame.draw.rect(window, (0, 255, 0), (menu_button_hitbox))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #sprawdzanie czy lewy przycisk myszy wciśnięty
            if unpause_button_hitbox.collidepoint(mouse_pos):
                pauze = False
                game = True
            elif menu_button_hitbox.collidepoint(mouse_pos):
                game = False
                menu = True

    #tryb game over
    if game_over == True:
        window.fill((0, 0, 0)) #wypełnienie tła czarnym kolorem
        window.blit(game_over_teskt, (50, 100)) #wyświetlanie napisu game over
        window.blit(points_tekst, (50, 200)) #wyświetlanie napisu z punktami
        restart_button_hitbox = pygame.Rect(150, 350, 64, 64) #htboxy przycisku restartującego
        pygame.draw.rect(window, (0, 255, 0), (restart_button_hitbox)) #rysowanie przycisku restartującego

        #sprawdzanie czy przycisk został wciśnięty
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #sprawdzanie czy lewy przycisk myszy wciśnięty
            if restart_button_hitbox.collidepoint(mouse_pos): #sprawdzanie czy wciśnięto w obrębie przycisku
                game_over = False #game over jest False
                duck_x = 100 #restart pozycji x kaczki
                duck_y = 250 #restart pozycji y kaczki
                pip_x = 400 #restart pozycji x rury
                pip2_x = 400 #restart pozycji x rury 2
                pip_y = -70 #restart pozycji y rury
                pip2_y = pip_y + pip_gap #restart pozycji y rury 2
                point = 0 #restart punktów
                duck_velocity_y = 0 #dalej nwm

    # Odświeżenie ekranu
    clock.tick(FPS) #ustawianie fps'ów
    pygame.display.flip() #aktualizacja okna
