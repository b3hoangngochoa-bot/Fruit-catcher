import pygame
from Core.game_manager import GameManager
from Core.game_state import Mode

# Vision
from Systems.Vision.camera import Camera
from Systems.Vision.hand_detector import HandDetector
from Systems.Vision.vision_system import VisionSystem

# Input
from Systems.Input.mapper import CoordinateMapper
from Systems.Input.smoother import Smoother
from Systems.Input.input_system import InputSystem
from Systems.Input.gesture_detector import GestureDetector
from Mocks.input_system_mouse import MouseInputSystemMock

# Gameplay
from Systems.GamePlay.spawner import Spawner
from Systems.GamePlay.gameplay_state import GameplayState
from Systems.GamePlay.difficulty_system import DifficultySystem
from Systems.GamePlay.object_manager import ObjectManager
from Systems.GamePlay.gameplay_system import GameplaySystem

# UI
from Systems.UI.ui_system import UISystem
from Systems.UI.Menu.menu import Menu
from Systems.UI.Menu.pause_menu import PauseMenu
from Systems.UI.Menu.game_over_menu import GameOverMenu

# Other Systems
from Systems.Collision.collision_system import CollisionSystem
from Systems.Render.render_system import RenderSystem
from Systems.Audio.audio_system import AudioSystem
from Core.observer import EventBus
from Utils import constants
from Core.event_type import EventType


# 🎯 Factory tạo toàn bộ systems
def create_systems(screen):
    # Event bus
    event_bus = EventBus()

    # Vision
    camera = Camera()
    detector = HandDetector()
    vision_system = VisionSystem(camera, detector)

    # Input
    mapper = CoordinateMapper()
    smoother = Smoother()
    gesture_detector = GestureDetector()   
    input_system = InputSystem(mapper, smoother, event_bus, gesture_detector)  # Dùng Vision thật
    # input_system = MouseInputSystemMock()  # Mock dùng chuột để test UI

    # Collision
    collision_system = CollisionSystem(event_bus)

    # Audio
    audio_system = AudioSystem(event_bus, pygame.mixer)

    # Gameplay
    spawner = Spawner()
    object_manager = ObjectManager()
    gameplay_state = GameplayState()
    difficulty_system = DifficultySystem(event_bus)
    gameplay_system = GameplaySystem(
        spawner,
        object_manager,
        collision_system,
        gameplay_state,
        difficulty_system,
        event_bus,
    )

    # UI
    menu = Menu()
    pause_menu = PauseMenu()
    game_over_menu = GameOverMenu()
    ui_system = UISystem(menu, pause_menu, game_over_menu, event_bus)

    # Render
    render_system = RenderSystem(screen)

    return {
        "vision": vision_system,
        "input": input_system,
        "ui": ui_system,
        "gameplay": gameplay_system,
        "collision": collision_system,
        "render": render_system,
        "audio": audio_system,
        "event_bus": event_bus,
    }


def main():
    # 🎮 Init pygame
    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Fruit Catching Game")

    clock = pygame.time.Clock()
    FPS = constants.FPS

    # 🧩 Create systems
    systems = create_systems(screen)

    # 🎥 Khởi động camera
    systems["vision"].start()  # 🎥 Khởi động camera

    # 🧠 Inject vào GameManager
    game_manager = GameManager(
        vision_system=systems["vision"],
        input_system=systems["input"],
        ui_system=systems["ui"],
        gameplay_system=systems["gameplay"],
        collision_system=systems["collision"],
        render_system=systems["render"],
        audio_system=systems["audio"],
        event_bus=systems["event_bus"],
    )

    running = True

    # 🔄 MAIN LOOP
    while running:
        delta_time = clock.tick(FPS) / 1000.0  # Convert ms to seconds
        # 1. Handle system-level events (OS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_manager.state == Mode.QUIT:
                running = False
            # optional: ESC → pause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_p:
                    if game_manager.state == Mode.PLAYING:
                        systems["event_bus"].emit(EventType.GAME_PAUSE, {"name": "pause_game"})
                    elif game_manager.state == Mode.PAUSE:
                        systems["event_bus"].emit(EventType.GAME_RESUME, {"name": "resume_game"})
                if event.key == pygame.K_o:
                    if game_manager.state == Mode.PLAYING:
                        systems["event_bus"].emit(EventType.GAME_OVER, {"name": "game_over"})

        # 2. Update Vision (camera + hand detect)
        systems["vision"].update()

        # 3. Update game logic
        game_manager.update(delta_time)

        # 3. Update display
        game_manager.draw()

        # 4. FPS control
        clock.tick(FPS)

        pygame.display.flip()

    # 🎥 Giải phóng camera
    systems["vision"].release()  # 🎥 Giải phóng camera
    pygame.quit()


if __name__ == "__main__":
    main()
