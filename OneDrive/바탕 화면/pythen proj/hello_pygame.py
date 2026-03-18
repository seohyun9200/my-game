import pygame
import sys

# 1. 초기화 및 화면 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("나의 첫 번째 게임")

# 2. 색깔 및 변수 설정
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()

# 원의 초기 상태
circle_x = 400
circle_y = 300
radius = 50
speed = 7

# 3. 게임 루프
running = True
while running:
    # (1) 이벤트 처리 (창 닫기 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # (2) 키보드 입력 확인
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  circle_x -= speed
    if keys[pygame.K_RIGHT]: circle_x += speed
    if keys[pygame.K_UP]:    circle_y -= speed
    if keys[pygame.K_DOWN]:  circle_y += speed

    # (3) 화면 경계 처리 (벽에 가두기)
    if circle_x < radius: circle_x = radius
    if circle_x > WIDTH - radius: circle_x = WIDTH - radius
    if circle_y < radius: circle_y = radius
    if circle_y > HEIGHT - radius: circle_y = radius

    # (4) 화면 그리기
    screen.fill(WHITE) # 배경 지우기
    pygame.draw.circle(screen, BLUE, (int(circle_x), int(circle_y)), radius)
    
    # (5) 화면 업데이트 및 프레임 고정
    pygame.display.flip()
    clock.tick(60)

# 4. 종료
pygame.quit()
sys.exit()