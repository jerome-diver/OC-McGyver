from views import Object


class ObjectView(View):

  def __init__(self, object_model):
    super().__init__(object_model)
    self._object_view.set_positions_objects()
