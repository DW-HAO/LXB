import random
import time
import pygame
from pygame.constants import *

class HeroPlane(object):
    def __init__(self, screen):
        # 添加飞机
        self.player = pygame.image.load("./飞机大战/me1.png")

        # 飞机坐标初始位置
        self.x = 480 / 2 - 102 / 2
        self.y = 500
        # 飞机速度
        self.speed = 8
        # 记录当前窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = []


    def key_control(self):
        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        elif key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed
        elif key_pressed[K_SPACE]:
            # 按下空格发射子弹
            bullet = Bullet(self.screen, self.x, self.y)
            # 把子弹放到列表里
            self.bullets.append(bullet)




    def display(self):
        # 将飞机图片粘贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            # 让子弹飞 修改子弹y坐标
            bullet.auto_move()
            # 子弹显示在窗口
            bullet.display()


class EnemyPlane(object):
    def __init__(self, screen):
        # 添加飞机
        self.player = pygame.image.load("./飞机大战/enemy1.png") # 57*43

        # 飞机坐标初始位置
        self.x = 0
        self.y = 0
        # 飞机速度
        self.speed = 3
        # 记录当前窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = []
        # 敌机移动方向
        self.direction = 'right'

    def display(self):
        # 将飞机图片粘贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            # 让子弹飞 修改子弹y坐标
            bullet.auto_move()
            # 子弹显示在窗口
            bullet.display()

    def auto_move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed

        if self.x > 480 - 57:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def auto_fire(self):
        '''自动发射子弹 创建子弹对象 添加进列表'''
        random_num = random.randint(1, 25)
        if random_num == 8:
            bullet = EnemyBullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)


# 敌机子弹类
# 属性
class EnemyBullet(object):
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 58/2 - 10/2
        self.y = y + 45
        # 图片
        self.image = pygame.image.load("./飞机大战/bullet2.png") # 5*11
        # 窗口
        self.screen = screen
        self.speed = 10

    def display(self):
        '''显示子弹到窗口'''
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        '''让子弹飞 修改子弹y坐标'''
        self.y += self.speed

# 子弹类
# 属性
class Bullet(object):
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 123/2 - 23/2
        self.y = y - 22
        # 图片
        self.image = pygame.image.load("./飞机大战/bullet1.png")
        # 窗口
        self.screen = screen
        self.speed = 10

    def display(self):
        '''显示子弹到窗口'''
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        '''让子弹飞 修改子弹y坐标'''
        self.y -= self.speed




def main():
    '''完成整个程序的控制'''
    # 创建一个窗口
    screen = pygame.display.set_mode((480, 700), 0, 32)
    # 给窗口添加图片 当做背景
    background = pygame.image.load("./飞机大战/background.png")
    # 创建一个飞机对象
    player = HeroPlane(screen)
    # 创建一个地方飞机对象
    enemy = EnemyPlane(screen)

    while True:
        # 将背景图片粘贴到窗口中
        screen.blit(background, (0, 0))

        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == pygame.QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序退出
                exit()

        # 执行飞机的键盘监听
        player.key_control()
        # 飞机的显示
        player.display()
        # 敌方飞机的显示
        enemy.display()
        # 敌方飞机自动移动
        enemy.auto_move()
        # 敌方飞机自动开火
        enemy.auto_fire()



        # 显示窗口中内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
