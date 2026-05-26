from Core.game_state import Mode

class UISystem:
    def __init__(self, menu, pause_menu, game_over_menu):
        self.menu = menu
        self.pause_menu = pause_menu
        self.game_over_menu = game_over_menu

    def update(self, cursor, state: Mode):
        """
        Route update based on game state
        Return Event or None
        """
        if state.name == "MENU":
            return self.menu.update(cursor)

        elif state.name == "PAUSE":
            return self.pause_menu.update(cursor)

        elif state.name == "GAME_OVER":
            return self.game_over_menu.update(cursor)

        return None

    def draw(self, screen, state: Mode):
        """
        Route draw based on state
        """
        if state.name == "MENU":
            self.menu.draw(screen)

        elif state.name == "PAUSE":
            self.pause_menu.draw(screen)

        elif state.name == "GAME_OVER":
            self.game_over_menu.draw(screen)
