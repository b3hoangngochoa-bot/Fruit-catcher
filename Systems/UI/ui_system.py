from Core.game_state import Mode


class UISystem:
    def __init__(self, menu, pause_menu, game_over_menu, event_bus):
        self.menu = menu
        self.pause_menu = pause_menu
        self.game_over_menu = game_over_menu
        self.event_bus = event_bus

    def update(self, input_data, cursor, state: Mode, delta_time):
        """
        Route update based on game state
        Return Event or None
        """
        if state == Mode.MENU:
            self.menu.update(input_data, self.event_bus, cursor, delta_time)

        elif state == Mode.PAUSE:
            self.pause_menu.update(input_data, self.event_bus, cursor, delta_time)

        elif state == Mode.GAME_OVER:
            self.game_over_menu.update(input_data, self.event_bus, cursor, delta_time)

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
