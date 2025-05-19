import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255, 255, 255)

class Ball():
    def __init__(self, screen, color, radius, pos, velocity):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = list(pos)
        self.velocity = list(velocity)

    def update_ball(self, screen_width, screen_height):
        # 更新位置
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # 檢查左右邊界，若碰到則反轉 x 軸速度
        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= screen_width:
            self.velocity[0] = -self.velocity[0]

        # 檢查上下邊界，若碰到則反轉 y 軸速度
        if self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= screen_height:
            self.velocity[1] = -self.velocity[1]

    def draw_ball(self):
        # add your code here
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)


def main():
    # add your code here
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('BouncyBall')
    
    ball_1 = Ball(screen, (255, 255, 255), 30, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], [4, 3])
    ball_2 = Ball(screen, (210, 30, 152), 16, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], [9, 5])

    clock = pygame.time.Clock()
    running = True

    # 主迴圈：持續更新與繪製
    while running:
        # 處理事件，當使用者關閉視窗時結束程式
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # add your code here
        screen.fill((0,0,0))
        

        # 更新球的位置及反彈邏輯
        ball_1.update_ball (SCREEN_WIDTH, SCREEN_HEIGHT)
        ball_2.update_ball (SCREEN_WIDTH, SCREEN_HEIGHT)

        # add your code here
        ball_1.draw_ball()
        ball_2.draw_ball()

        pygame.display.flip()

        clock.tick(60)

    # add your code here
    pygame.quit()

if __name__ == "__main__":
    main()
