from Core.game_state import Mode

class UISystem:
    def __init__(self, menu, pause_menu, game_over_menu, event_bus):
        self.menu = menu
        self.pause_menu = pause_menu
        self.game_over_menu = game_over_menu
        self.event_bus = event_bus

    def update(self, cursor, state: Mode):
        """
        Route update based on game state
        Return Event or None
        """
        if state.name == "MENU":
            return self.menu.update(self.event_bus, cursor)

        elif state.name == "PAUSE":
            return self.pause_menu.update(self.event_bus, cursor)

        elif state.name == "GAME_OVER":
            return self.game_over_menu.update(self.event_bus, cursor)

        return None

    def get_render_data(self, state):
        ui = self._get_current_ui(state)
        if ui:
            return ui.get_render_data()
        return []

    def _get_current_ui(self, state):
        if state == Mode.MENU:
            return self.menu
        elif state == Mode.PAUSE:
            return self.pause_menu
        elif state == Mode.GAME_OVER:
            return self.game_over_menu
        return None