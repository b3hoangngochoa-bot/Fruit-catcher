from Utils.load_asset import load_sfx, load_music
from Core.event_type import EventType


class AudioSystem:
    def __init__(self, event_bus, mixer):
        self.event_bus = event_bus
        self.mixer = mixer
        self.name_sfx = {
            "fruit_hit": "catching_sound",
            "bomb_hit": "bomb_explosion",
        }
        self.sfx_cache = {}
        self.music_cache = {}
        self.event_bus.subscribe(EventType.FRUIT_HIT, self._on_fruit_hit)
        self.event_bus.subscribe(EventType.BOMB_HIT, self._on_bomb_hit)
        self.event_bus.subscribe(EventType.LEVEL_UP, self._on_level_up)
        self.event_bus.subscribe(EventType.GAME_START, self._on_game_start)
        self.event_bus.subscribe(EventType.GAME_OVER, self._on_game_over)
        self.event_bus.subscribe(EventType.GAME_PAUSE, self._on_game_pause)
        self.event_bus.subscribe(EventType.GAME_RESUME, self._on_game_resume)
        self.event_bus.subscribe(EventType.GAME_RESTART, self._on_game_restart)
        self.event_bus.subscribe(EventType.GO_TO_MENU, self._on_go_to_menu)
        self.event_bus.subscribe(EventType.BUTTON_CLICK, self._on_button_click)
        self.event_bus.subscribe(EventType.BUTTON_HOVER, self._on_button_hover)
        self.event_bus.subscribe(EventType.BUTTON_HOLD, self._on_button_hold)

    def play_sfx(self, name):
        if name not in self.sfx_cache:
            self.sfx_cache[name] = load_sfx(name, "wav", self.mixer)
        self.sfx_cache[name].play()

    def play_music(self):
        if "background" not in self.music_cache:
            self.music_cache["background"] = load_music("background", "mp3", self.mixer)
        self.mixer.music.play(-1)  # Loop indefinitely

    def stop_music(self):
        self.mixer.music.stop()

    def _on_fruit_hit(self, data):
        name = self.name_sfx[data["name"]]
        self.play_sfx(name)

    def _on_bomb_hit(self, data):
        name = self.name_sfx[data["name"]]
        self.play_sfx(name)

    def _on_level_up(self, data):
        pass

    def _on_game_start(self, data):
        pass

    def _on_game_over(self, data):
        pass

    def _on_game_pause(self, data):
        pass

    def _on_game_resume(self, data):
        # self.play_music()
        pass

    def _on_game_restart(self, data):
        # self.stop_music()
        # self.play_music()
        pass

    def _on_go_to_menu(self, data):
        # self.stop_music()
        pass

    def _on_button_click(self, data):
        # self.play_sfx("button_click")
        pass

    def _on_button_hover(self, data):
        # self.play_sfx("button_hover")
        pass

    def _on_button_hold(self, data):
        # self.play_sfx("button_hold")
        pass
