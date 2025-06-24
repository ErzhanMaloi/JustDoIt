import pygame
import random

pygame.init

def neudaza(music_num):
    match music_num:
        case 1:
            pygame.mixer.music.load("music 1.mp3")
        case 2:
            pygame.mixer.music.load("music 2.mp3")
        case 3:
            pygame.mixer.music.load("music 3.mp3")
        case 4:
            pygame.mixer.music.load("music 4.mp3")
       
def play():
    pygame.mixer.init()
    print (neudaza(random.randint(1,4)))
    pygame.mixer.music.play()
    input("Нажмите Enter, чтобы остановить...") # Чтобы программа не завершилась сразу:
    pygame.mixer.music.stop()
    
print (play())