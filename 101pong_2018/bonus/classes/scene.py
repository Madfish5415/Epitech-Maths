class Scene:
    def __init__(self):
        self.scene = self
        pass

    def render(self, window):
        raise NotImplementedError

    def events_manager(self, events, pressed_keys):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def switch_to(self, scene):
        self.scene = scene
