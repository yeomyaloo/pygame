import pygame

pygame.init() #초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640

pygame.display.set_mode((screen_width, screen_height)) #화면 크기설정


pygame.display.set_caption("Yaloo Game") #게임이름

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()