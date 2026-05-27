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
import Utils.constants as constants


# 🎯 Factory tạo toàn bộ systems
def create_systems(screen):
    # Vision
    camera = Camera()
    detector = HandDetector()
    vision_system = VisionSystem(camera, detector)

    # Input
    mapper = CoordinateMapper()
    smoother = Smoother()
    # input_system = InputSystem(mapper, smoother)
    input_system = MouseInputSystemMock()  # Dùng mock để test UI trước

    # Collision
    collision_system = CollisionSystem()

    # Audio
    audio_system = AudioSystem()

    # Gameplay
    spawner = Spawner()
    object_manager = ObjectManager()
    gameplay_state = GameplayState()
    difficulty_system = DifficultySystem()
    gameplay_system = GameplaySystem(
        spawner, object_manager, collision_system, gameplay_state, difficulty_system
    )

    # UI
    menu = Menu()
    pause_menu = PauseMenu()
    game_over_menu = GameOverMenu()
    ui_system = UISystem(menu, pause_menu, game_over_menu)

    # Render
    render_system = RenderSystem(screen, gameplay_system)

    return {
        "vision": vision_system,
        "input": input_system,
        "ui": ui_system,
        "gameplay": gameplay_system,
        "collision": collision_system,
        "render": render_system,
        "audio": audio_system,
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

    # 🧠 Inject vào GameManager
    game_manager = GameManager(
        vision_system=systems["vision"],
        input_system=systems["input"],
        ui_system=systems["ui"],
        gameplay_system=systems["gameplay"],
        collision_system=systems["collision"],
        render_system=systems["render"],
        audio_system=systems["audio"],
    )

    running = True

    # 🔄 MAIN LOOP
    while running:
        delta_time = clock.tick(FPS) / 1000.0  # Convert ms to seconds
        # 1. Handle system-level events (OS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # optional: ESC → pause
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            # if game_manager.state == Mode.PLAYING:
            #     game_manager.state = Mode.PAUSE
            # elif game_manager.state == Mode.PAUSE:
            #     game_manager.state = Mode.PLAYING

        # 2. Update game logic
        game_manager.update(delta_time)

        # 3. Update display
        game_manager.draw()

        # 4. FPS control
        clock.tick(FPS)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
