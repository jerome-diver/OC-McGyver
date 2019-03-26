

import copy

from controllers import Controller


class RoomController(Controller):

    def __init__(self,pyGameEngine, map_):
        super().__init__(pyGameEngine)
        self._rooms = {} # { "model": {(row,column): RoomModel}, "view": {(row,col): RoomView} }
        self.loadRooms(map_)

    def loadRooms(self, _map):
        for row in range (0,14):
            for column in range(0,14):
                co = (row,column)
                wp =_map.wallPosition(co)
                self._rooms["model"][co] = RoomModel(wp, self.gameEngine)
                self._rooms["view"][co] = RoomView(self._roomsModels[co])


    def getRoomType(self, _type, coordinates): 
        self.tryTypeMV(_type)
        return self._rooms[_type][coordinates]

    def getRooms(self): 
        rooms_list = []
        for roomModel in self._rooms["model"].values():
            rooms_list.append(roomModel.getRoom())
        return rooms_list

    def getRoomDictionary(self):
        rooms_dict = { }
        for key in self._rooms["model"].keys():
            rooms_dict[key] = self._rooms["model"][key].getRoom()
        return rooms_dict

    def getRoomAt(self, coordonates): 
        rooms = self.getRoomsDictionary()
        return rooms[coordonates]

    def tryTypeMV(self, _type):# _type should be "view" or "model"
        try:
            _type == "model" or _type == "view"
        except ValueError:
            print('RoomController.getRoomType(_type,...) argument should be '+\
                  '"model" or "view" only')
