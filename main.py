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

# Gameplay
from Systems.GamePlay.spawner import Spawner
from Systems.GamePlay.gameplay_system import GamePlaySystem

# UI
from Systems.UI.ui_system import UISystem

# Other Systems
from Systems.Collision.collision_system import CollisionSystem
from Systems.Render.render_system import RenderSystem
from Systems.Audio.audio_system import AudioSystem


# 🎯 Factory tạo toàn bộ systems
def create_systems(screen):
    # Vision
    camera = Camera()
    detector = HandDetector()
    vision_system = VisionSystem(camera, detector)

    # Input
    mapper = CoordinateMapper()
    smoother = Smoother()
    input_system = InputSystem(mapper, smoother)

    # Gameplay
    spawner = Spawner()
    gameplay_system = GamePlaySystem(spawner)

    # UI
    ui_system = UISystem()

    # Others
    collision_system = CollisionSystem()
    render_system = RenderSystem(screen)
    audio_system = AudioSystem()

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

    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fruit Catching Game")

    clock = pygame.time.Clock()
    FPS = 60

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
        # game_manager.update()

        # 3. Update display
        pygame.display.flip()

        # 4. FPS control
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
