# pygame

---
# pygame_basic
## 1. pygame 라이브러리 다운

## 2. 뼈대 작성
- 1_create_frame.py

## 3. 배경 넣기
- 2_background.py
- 해당 작업은 fill() rgb 값 설정해서 배경 채우기 가능
- 해당 작업은 blit() 메소드 사용으로 배경지정 가능

## 4. 캐릭터 만들기
- 3_main_sprite.py
- 배경과 마찬가지로 해당 작업을 진행한다.
- 이때 캐릭터가 그려지는 위치는 위에서 아래로 왼쪽에서 오른쪽으로 그려지기에 해당 캐릭터를 놓을 위치를 구하는 방식은 조금 다름
![img_1.png](img_1.png)
``` python
character = pygame.image.load("C:/Users/Yeomyaloo/Documents/GitHub/pygame/pygame_basic/cr.png")
#캐릭터의 경우엔 계속 움직이기에 추가작업 진행해주어야 한다.
character_size = character.get_rect().size
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1]#캐릭터 세로 크기
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height-character_height
``` 
## 5. 키보드 이벤트
- 4_keyboard_event
