"""
This class is inherited by all the base classes
And it has to wash/delete all the attributes at the end of the game
i hope for no memory weak
"""


class Washer:
    '''Delete own inherited instances arguments'''

    def __del__(self):
        '''Delete own arguments'''
        if self.__dict__:
            print(" ==> ", end='')
            print("attributes deleted inside",
                  self.__class__.__name__, "[", end='')
            for i, attr_keys in enumerate(list(self.__dict__.keys())):
                print(",", end='') if i != 0 else print("", end='')
                print(attr_keys, end='')
                del self.__dict__[attr_keys]
            print("]")
