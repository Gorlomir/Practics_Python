import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong Game Ultimate Ninja Storm Universal Edition'


class Score_Zone_1(arcade.Sprite):
    def __init__(self):
        super().__init__('score_zone.png',1 )

class Score_Zone_2(arcade.Sprite):

    def __init__(self):
        super().__init__('score_zone_enemy.png', 1)


class Ball(arcade.Sprite):
    def reset(self):
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.change_x = 5
        self.change_y = 5
    def __init__(self):
        super().__init__('ball.png', 0.1)
        self.change_x = 5
        self.change_y = 5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.2)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0


class Enemy_Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('enemy_bar.png', 0.2)
        self.change_x = 5

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x


class Game(arcade.Window):
    def reset_ball(self):
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

        self.ball.change_x = 6
        self.ball.change_y = random.uniform(-10, 10)
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.enemy_bar = Enemy_Bar()
        self.ball = Ball()
        self.score_player = 0
        self.score_enemy = 0
        self.score_zone = Score_Zone_1()
        self.score_zone_enemy = Score_Zone_2()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 9

        self.score_zone.center_x = SCREEN_WIDTH / 2
        self.score_zone.center_y = 10

        self.score_zone_enemy.center_x = SCREEN_WIDTH / 2
        self.score_zone_enemy.center_y = SCREEN_HEIGHT / 1

        self.enemy_bar.center_x = SCREEN_WIDTH / 2
        self.enemy_bar.center_y = SCREEN_HEIGHT / 1.1

        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.enemy_bar.draw()
        self.ball.draw()
        self.score_zone.draw()
        self.score_zone_enemy.draw()

        score_text = f"Игрок: {self.score_player}, Противник: {self.score_enemy}"
        arcade.draw_text(score_text, 10, SCREEN_HEIGHT - 50, arcade.color.BLACK, 24)

    def update(self, delta_time: float):
        if arcade.check_for_collision(self.ball, self.score_zone_enemy):
            self.reset_ball()
            self.score_player += 1
        if arcade.check_for_collision(self.ball, self.score_zone):
            self.reset_ball()
            self.score_enemy += 1
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        if arcade.check_for_collision(self.enemy_bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()
        self.enemy_bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
