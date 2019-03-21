'''
The Object class contain each object who can be find inside any room randomly.
'''


class Object:

    logoFile = ""
    name = ""
    def __init__(self):
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setLogoFile(self, file):
        self.logoFile = file
