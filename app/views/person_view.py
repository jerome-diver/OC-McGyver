from views import View


class GuardView(View):

    def __init__(self, guardModel):
        super().__init__(guardModel)

    def setHeroOnGame(self):
        # load image from app/img/MacGyver.png
        cwd = os.path.dirname(__file__)
        img = os.path.join(cwd, "img/MacGyver.png")
        self._model.setImage(img)


class HeroView(View):

    def __init__(self,heroModel):
        super().__init__(heroModel)