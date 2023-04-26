import pygame

pygame.init() #초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기설정


pygame.display.set_caption("Yaloo Game") #게임이름

background = pygame.image.load("C:/Users/Yeomyaloo/Documents/GitHub/pygame/pygame_basic/bg.png")


character = pygame.image.load("C:/Users/Yeomyaloo/Documents/GitHub/pygame/pygame_basic/cr.png")
character_size = character.get_rect().size
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1]#캐릭터 세로 크기
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height-character_height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터
    pygame.display.update()#게임화면 다시 그리기

pygame.quit()