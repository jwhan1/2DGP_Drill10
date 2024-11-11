
from pico2d import get_time, load_image, load_font, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from state_machine import *
import game_world
import game_framework
import time
import random

BIRDWEIGHT=100
BIRDHEIGHT=100

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel당 30 cm
RUN_SPEED_KMPH = 100.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
FRAMES_PER_ACTION = 8#팔을 휘두르는 프레임의 갯수
ACTION_PER_TIME = 3#초당 팔을 휘두르는 횟수



class Fly:
    @staticmethod
    def enter(boy, e):
        if start_event(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
            boy.frame = 0

    @staticmethod
    def exit(boy, e):
        if space_down(e):
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame =  (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8#실수
        boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        if boy.x < BIRDWEIGHT/2:
            boy.dir = 1
            boy.face_dir = 1
        elif boy.x > 1600-BIRDWEIGHT/2:
            boy.dir = -1
            boy.face_dir = -1


    @staticmethod
    def draw(boy):
        if boy.face_dir == 1:
            boy.image.clip_composite_draw(int(boy.frame% 5) * 183, int(boy.frame / 3) * 168, 183, 168, 0, '', boy.x, boy.y, BIRDWEIGHT, BIRDHEIGHT)
        else:
            boy.image.clip_composite_draw(int(boy.frame% 5) * 183, int(boy.frame / 3) * 168, 183, 168, 3.141592, 'v', boy.x, boy.y, BIRDWEIGHT, BIRDHEIGHT)




class Bird:

    def __init__(self):
        self.x, self.y = random.randint(int(BIRDWEIGHT/2),1600-int(BIRDWEIGHT/2)), random.randint(90+int(BIRDHEIGHT/2),600-int(BIRDHEIGHT/2))
        self.face_dir = 1
        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Fly)
        
    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.state_machine.draw()