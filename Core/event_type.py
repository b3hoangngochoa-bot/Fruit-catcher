class EventType:
    # ----------------------------
    # GAME STATE
    # ----------------------------
    GAME_START = "GAME_START"
    GAME_PAUSE = "GAME_PAUSE"
    GAME_RESUME = "GAME_RESUME"
    GAME_OVER = "GAME_OVER"
    GO_TO_MENU = "GO_TO_MENU"

    # ----------------------------
    # UI
    # ----------------------------
    BUTTON_CLICK = "BUTTON_CLICK"
    BUTTON_HOVER = "BUTTON_HOVER"
    BUTTON_HOLD = "BUTTON_HOLD"

    # ----------------------------
    # GAMEPLAY
    # ----------------------------
    FRUIT_HIT = "FRUIT_HIT"
    BOMB_HIT = "BOMB_HIT"

    OBJECT_SPAWNED = "OBJECT_SPAWNED"
    OBJECT_DESPAWNED = "OBJECT_DESPAWNED"

    # ----------------------------
    # PROGRESSION
    # ----------------------------
    LEVEL_UP = "LEVEL_UP"
    TIME_TICK = "TIME_TICK"
