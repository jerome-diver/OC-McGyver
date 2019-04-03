"""
This class is inherited by all the base classes
And it has to wash/delete all the attributes at the end of the game
i hope for no memory weak
"""


class Washer:

  def __del__(self):
    if self.__dict__:
      print("from", self.__class__.__name__)
      for attr_keys in list(self.__dict__.keys()):
        print("\t => ", attr_keys, "attributes has been deleted")
        del(self.__dict__[attr_keys])
