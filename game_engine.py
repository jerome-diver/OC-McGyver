'''
PyGame engine should run the game when all objects/models/views

and controllers are loaded.
'''

import time
from pygame.sprite import Group
import pygame as pg

from settings import CLK, BLACK, WIDTH, HEIGHT, JINGLE_FILE
from washer import Washer


class SpritesGroupNamed(Group, Washer):
    '''Own Sprite's Groups with a self _name'''

    def __init__(self, name):
        super().__init__()
        self._name = name

    def get_name(self):
        '''REturn his _name:str'''
        return self._name


class GameEngine(Washer):
    '''This is the engine of the game with PyGame'''

    def __init__(self):
        self._crashed = False  # to finish the pygame loop
        self._sprites_groups = []  # list of Sprites (to show)
        self._background_jobs = []  # list of job to run in background
        pg.mixer.init()
        self.volume = pg.mixer.music.get_volume()
        pg.init()
        self._window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("OpenClassRoom -- project3 -- Mac Gyver")
        self._clk = pg.time.Clock()  # the refresh frequency counter

    def start(self):
        '''The loop of execution of pygame'''
        while not self._crashed:
            self.keys_down_events()
            # the frequency in FPS
            self._clk.tick(CLK)
            # paint the screen in black at each loop turn
            self._window.fill(BLACK)
            self.update_sprites_groups()
            self.exec_jobs_background()
            # print the result
            pg.display.flip()
        pg.quit()

    #
    def keys_down_events(self):
        '''When a keyboard key is pressed down...'''
        for _ev in pg.event.get():
            if _ev.type == pg.KEYDOWN:
                # "q" key is pressed down
                if _ev.key == pg.K_q:
                    print("bye bye, see you soon !")
                    self._crashed = True
                    # "s" key is pressed down
                if _ev.key == pg.K_s:
                    self.toggle_jingle_volume()
                    # X icon of the GUI window's game is clicked
            if _ev.type == pg.QUIT:
                self._crashed = True

    def create_group(self, name):
        '''Create the group of sprite and give him a name'''
        self._sprites_groups.append(SpritesGroupNamed(name))

    def add_sprites_to_group(self, group_name, sprites):
        '''Add a list of sprites:pygame.sprite.Sprite

        to the group with the name group_name:str'''
        for group in self._sprites_groups:
            if group.get_name() == group_name:
                #for sprite in sprites:
                group.add(sprites)

    def update_sprites_groups(self):
        '''All groups of sprites are update.

        When i update the pygame.sprite.Group, all the contained
        sprites of this group are updated.'''
        for group in self._sprites_groups:
            group.update()
            group.draw(self._window)

    def get_group(self, name):
        '''Return the group with this name:str'''
        for group in self._sprites_groups:
            if group.get_name() == name:
                return group
        return None

    def message(self, text, size, color, pos_x=None, pos_y=None):
        '''Print multi-lines messages on screen

        text:str, size:int, color:tuple(R:int, G:int, B:int), x:int; y:int'''
        _x_arg, _y_arg = False, False
        # the first time only... because after, pos_x will have a value
        if pos_x is not None:
            _x_arg = True
        if pos_y is not None:
            _y_arg = True
        lines = text.splitlines()
        font = pg.font.Font("fonts/Ubuntu-M.ttf", size)
        for _index, _line in enumerate(reversed(lines)):
            if not _x_arg:
                # in the center
                pos_x = int((WIDTH - font.size(_line)[0]) / 2)
            if not _y_arg:
                pos_y = int((HEIGHT - font.size(text)[1]) / 2)
            # print the resulted text inside an image
            self._window.blit(font.render(_line, 0, color),
                              (pos_x, pos_y - font.get_linesize() * _index))

    def actions_delayed(self, tempo,
                        action_start=None, sa_args=None,
                        action_end=None, e_args=None):
        '''Create a job in background of game engine

        to execute a start function and a end function,
        with a delay between them
        tempo:int(seconds), action_start:function, sa_args:arguments,
        action_end:function, e_args:arguments'''
        new_background_job = {}
        # if there is a function to call there
        if action_start:
            new_background_job["start_job"] = {"action": action_start}
            if sa_args:
                new_background_job["start_job"]["args"] = sa_args
            new_background_job["time_start"] = int(time.time())
            new_background_job["delay"] = tempo
            if action_end:
                new_background_job["end_job"] = {"action": action_end}
                if e_args:
                    new_background_job["end_job"]["args"] = e_args
            # add the formed data inside the list of background jobs to do
            self._background_jobs.append(new_background_job)

    def exec_jobs_background(self):
        '''Execute all jobs in the background

        and delete the time left exit one's '''
        finished_jobs = []
        # only if have one or any background_jobs
        if self._background_jobs:
            # for each job in the list
            for index, job in enumerate(self._background_jobs):
                # and igf the is "start_job" argument(s)
                if "args" in job["start_job"]:
                    job["start_job"]["action"](*job["start_job"]["args"])
                # if no argument for "start_job"
                else:
                    job["start_job"]["action"]()
                # get the count timer reference (now !)
                now = int(time.time())
                # and when out of delay for this start_job
                if job["delay"] <= now - job["time_start"]:
                    # give the inormation in the list of finished_job
                    finished_jobs.append(index)
                    # and if there is a "end_job" to do...
                    if "end_job" in job:
                        # with some arguments...
                        if "args" in job["end_job"]:
                            job["end_job"]["action"](*job["end_job"]["args"])
                        else:
                            job["end_job"]["action"]()
            # test because we don't want crash at end_game
            if self._background_jobs:
                # delete the finished jobs in the list
                for job_to_remove in finished_jobs:
                    del self._background_jobs[job_to_remove]

    def play_jingle(self):
        '''Play the jingle music'''
        pg.mixer.music.load(JINGLE_FILE)
        pg.mixer.music.play()
        pg.mixer.music.set_volume(self.volume)

    def toggle_jingle_volume(self):
        '''Mut / unmute the volume of the jingle'''
        volume = pg.mixer.music.get_volume()
        if volume == 0:
            pg.mixer.music.set_volume(self.volume)
        else:
            pg.mixer.music.set_volume(0)

    def end_game(self):
        '''End of the game'''
        self._crashed = True
        self._background_jobs = None
