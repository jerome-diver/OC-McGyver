from views.view import View


class GuardView(View):

  def __init__(self, guardModel):
    super().__init__(guardModel)


class HeroView(View):

  def __init__(self, controller, model, gameEngine):
    super().__init__(controller, model, gameEngine)
    self._gameEngine.createGroup("hero")
    hero = self._model.getHero()
    hero.setPosition(
        self._controller.getLabyrinthModel().getbestHeroPosition())
    self._gameEngine.addSpritesToGroup([hero], "hero")
    hero.canCollidWith("labyrinth", self._gameEngine.getGroup("labyrinth"))
