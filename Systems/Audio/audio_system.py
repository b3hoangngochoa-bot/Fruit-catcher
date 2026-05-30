from Utils.constants import PATH_TO_MUSIC
from Utils.load_asset import load_sfx, load_music
from Core.event_type import EventType


class AudioSystem:
    def __init__(self, event_bus, mixer):
        self.event_bus = event_bus
        self.mixer = mixer
        self.name_sfx = {
            "fruit_hit": ["catching_sound", "wav"],
            "bomb_hit": ["bomb_explosion", "wav"],
            "button_click": ["button_click", "mp3"],
            "button_hover": ["button_hover", "mp3"],
            "button_hold": ["button_hold", "mp3"],
            "level_up": ["level_up", "mp3"],
            "game_start": ["game_start", "mp3"],
            "game_over": ["game_over", "wav"],
            "pause_game": ["pause_game", "mp3"],
            "resume_game": ["resume", "mp3"],
            "restart_game": ["resume", "mp3"],
            "go_to_menu": ["go_to_menu", "mp3"],
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

        self.play_music("background_music_menu", "mp3")

    def play_sfx(self, name, extension="wav"):
        if name not in self.sfx_cache:
            self.sfx_cache[name] = load_sfx(name, extension, self.mixer)
        self.sfx_cache[name].set_volume(1)  # Adjust volume as needed
        self.sfx_cache[name].play()

    def play_music(self, name="background", extension="mp3"):

        path = PATH_TO_MUSIC + f"{name}.{extension}"
        self.mixer.music.load(path)
        self.mixer.music.set_volume(0.5)
        self.mixer.music.play(-1)

    def stop_music(self):
        self.mixer.music.stop()

    def _on_fruit_hit(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.play_sfx(name, extension)

    def _on_bomb_hit(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.play_sfx(name, extension)

    def _on_level_up(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.play_sfx(name, extension)

    def _on_game_start(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.stop_music()
        self.play_sfx(name, extension)
        self.play_music("background_music_gameplay", "mp3")

    def _on_game_over(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.stop_music()
        self.play_sfx(name, extension)

    def _on_game_pause(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.stop_music()
        self.play_sfx(name, extension)

    def _on_game_resume(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.play_sfx(name, extension)
        self.play_music("background_music_gameplay", "mp3")

    def _on_game_restart(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.play_sfx(name, extension)
        self.play_music("background_music_gameplay", "mp3")

    def _on_go_to_menu(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.stop_music()
        self.play_sfx(name, extension)
        self.play_music("background_music_menu", "mp3")

    def _on_button_click(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.play_sfx(name, extension)

    def _on_button_hover(self, data):
        name = self.name_sfx[data["name"]][0]
        extension = self.name_sfx[data["name"]][1]
        self.play_sfx(name, extension)

    def _on_button_hold(self, data):
        pass
