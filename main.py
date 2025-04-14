import pygame
import random

#wywołanie pygame
pygame.init()

#zmienne do uruchomienia

FPS = 60 #FPS gry
run = True #włączenie okna gry
WIDTH = 400 #szerokość okna
HEIGHT = 600 #wysokość okna
game_over = False #czy gameover Jest true lub false
clock = pygame.time.Clock() #wywołanie fps'ów
pygame.display.set_caption("Flappy Duck") #nadanie tutułu okna
window = pygame.display.set_mode((WIDTH, HEIGHT)) #okno gry

#zmienne gracza
duck_x = 100 #miejsce gracza w osi x
duck_y = 250 #miejsce gracza w osi y
duck_speed = 5 #prędkość gracza
duck_gravity = 0.25 #gravitacja
duck_velocity_y = 0 #nwm

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

#skalowanie obrazków
scaled_pipu_image = pygame.transform.scale(pip_u_image, (80, 400))
scaled_pipd_image = pygame.transform.scale(pip_d_image, (100, 400))
scaled_alien_image = pygame.transform.scale(alien_image, (64, 64)) #statek wroga
scaled_duck_image = pygame.transform.scale(duck_image, (64, 64)) #kaczka
scaled_knight_image = pygame.transform.scale(knight_image, (64, 64)) #rycerz wróg
scaled_bocian_image = pygame.transform.scale(bocian_image, (90, 64)) #bocian wróg
scaled_background_image = pygame.transform.scale(background_image, (400, 600)) #tło

#pętla gierki
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pip_x -= pip_speed
    pip2_x -= pip_speed

    keys = pygame.key.get_pressed() #zmienna czy przycisk został naciśnięty
    if keys[pygame.K_SPACE]: #sprawdzanie czy spacja została wciśnięta
        duck_velocity_y = -duck_speed 

    if pip_x <= -100:
        pip_x = 400
        pip_y = random.randint(-200, 0)
        pip2_y = pip_y + pip_gap
        pip2_x = 400 

    #grawitacja gracza
    duck_velocity_y += duck_gravity
    duck_y += duck_velocity_y

    #hitboxy wszystkiego
    pip_hitbox = pygame.Rect(pip_x, pip_y, scaled_pipu_image.get_width(), scaled_pipu_image.get_height())
    pip2_hitbox = pygame.Rect(pip2_x, pip2_y, scaled_pipd_image.get_width() -, scaled_pipd_image.get_height())
    duck_hitbox = pygame.Rect(duck_x, duck_y, 64, 64)

    if duck_hitbox.colliderect(pip_hitbox):
        print("dupa")

    if duck_hitbox.colliderect(pip2_hitbox):
        print("kupa")

    # Rysowanie tła, kaczki i inne
    window.blit(scaled_background_image, (0, 0)) #wklejenie tła na okno
    window.blit(scaled_duck_image, (duck_x, duck_y)) #wklejenie kaczki na okno
    window.blit(scaled_pipu_image, (pip_x, pip_y))
    window.blit(scaled_pipd_image, (pip2_x, pip2_y))

    # Odświeżenie ekranu
    clock.tick(FPS) #ustawianie fps'ów
    pygame.display.flip() #aktualizacja okna
