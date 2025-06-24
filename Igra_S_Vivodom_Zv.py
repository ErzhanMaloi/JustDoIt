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
    # pygame.mixer.music.stop()
    
            
rand_num = random.randint(1 , 100)
popitka = 0
num = 0
kol = random.randint(1 , 20)
print ('vam dano popitok ',kol)
while int(popitka) <= int(kol):
    
    num = int(input('Vvedite vashe predpologaemoe zislo ot 1 do 100 '))
    popitka += 1
    ost_popitok = kol - popitka
    print('ostalos popitor ',ost_popitok)
    
    if (num == rand_num):
        print('Vi ugadali zislo s popitki ',popitka)
        break
    elif (kol == popitka):
        print('vi proigrali')
        break
    elif (num > rand_num):
        bolshee = num - rand_num
        print('Vi vveli zislo bolshee zadannogo loshara na kol', bolshee)
        print (play())
    elif (num < rand_num):
        menshee = rand_num - num
        print ('Vi vveli zislo menshe zadannogo loshara na kol', menshee)
        print (play())
