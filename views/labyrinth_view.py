'''
The specific view of the map.
This load image of map inside the game view
'''

import time

from components import Wall
from settings import ADJ_X, ADJ_Y, \
                    RED, WHITE, \
                    WIDTH, HEIGHT, \
                    MAX_TIMER_GAME
from views import View


class LabyrinthView(View):
    '''View for the Labyrinth'''

    start_time = int(time.time())

    def __init__(self, controller, model, game_engine):
        super().__init__(controller, model, game_engine)
        self.create_walls()
        self._game_engine.add_sprites_to_group("labyrinth",
                                               self._model.get_elements())
        self.start_timer()
        self.show_key_bindings()

    def wall_exist(self, wall):
        '''Return True if this wall exist'''
        if not self._model.get_elements():
            for old_wall in self._model.get_elements():
                old_rect = old_wall.rect
                new_rect = wall.rect
                if (new_rect.rect.topleft == old_rect.topleft) and \
                        (new_rect.bottomright == old_rect.bottomright):
                    return True
        return False

    def create_walls(self):
        '''Create the walls of the Labyrinth

        by write inside LabyrinthModel variable instance
        _walls all if them (no doubles)'''
        for key, value in self._model.get_walls_bytes().items():
            sides = ("top", "right", "bottom", "left")
            # format the char to be a representation of
            # binary code with 4 default chars long
            bin_code = "{0:b}".format(ord(value)).zfill(4)[::-1]
            # split it with index
            for index, bit in enumerate(bin_code):
                if bit == "1":  # bit high mean that ther is a wall there
                    idd = (key[0], key[1], sides[index])
                    new_wall = Wall(idd, (ADJ_X, ADJ_Y))
                    # we add it only if it doesn't exist allready
                    if not self.wall_exist(new_wall):
                        self._model.get_elements().append(new_wall)
                    else:
                        del new_wall
                else:  # bit down => no wall there
                    # if the exit is not define already
                    if not self._model.get_exit_position():
                        # try to find if this wall is the exit of the labyrinth
                        self.find_exit_position(key, index)

    def find_exit_position(self, key, index):
        '''Find the exit position of enclosure's Labyrinth walls

        From cells key coordonate:tuple(int,int)
        and index:int bit of cell's wall
        And put his coordonates in his instance model'''
        _max_rows = self._model.get_labyrinth_rows()
        _max_columns = self._model.get_labyrinth_columns()
        _top_sides = (key[0] == 0 and index == 0)
        _right_sides = (key[1] == (_max_columns - 1) and index == 1)
        _bottom_sides = (key[0] == (_max_rows - 1) and index == 2)
        _left_sides = (key[1] == 0 and index == 3)
        if _top_sides or _right_sides or _bottom_sides or _left_sides:
            self._model.set_exit_coordonates(key[0], key[1])

    def show_timer(self):
        '''Print on screen the remaining timer's time of the game'''
        timer = MAX_TIMER_GAME - (int(time.time()) -
                                  LabyrinthView.start_time)
        text = "Remaining time:  " + str(timer) + " seconds"
        y_pos = HEIGHT - 50
        self._game_engine.message(text, 24, WHITE, 20, y_pos)

    def time_out(self):
        '''Print the end message for timing out and Game Over'''
        _en = self._game_engine
        text = "Time is over !\nYou loose."
        _en.actions_delayed(tempo=2,
                            action_start=_en.message,
                            sa_args=(text, 38, RED),
                            action_end=_en.end_game)

    def start_timer(self):
        '''Start the timer og the game'''
        _en = self._game_engine
        _en.actions_delayed(tempo=MAX_TIMER_GAME,
                            action_start=self.show_timer,
                            action_end=self.time_out)

    def show_key_bindings(self):
        '''Print on screen keys bindings abilities'''
        _en = self._game_engine
        text = '"q" =>       quit the game\n' \
               '"s" => mute the volume'
        _en.actions_delayed(tempo=MAX_TIMER_GAME,
                            action_start=_en.message,
                            sa_args=(text, 14, WHITE, WIDTH - 150, 20))
