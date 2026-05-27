import pygame
from Models.basket_model import Basket
from Core.event_type import EventType
from Utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class GameplaySystem:
    def __init__(
        self,
        spawner,
        object_manager,
        collision_system,
        gameplay_state,
        difficulty_system,
        event_bus,
    ):
        # core systems
        self.spawner = spawner
        self.basket = (
            Basket()
        )  # Temporary, should be created by spawner and managed by object_manager
        self.object_manager = object_manager
        self.object_manager.add_object(self.basket)  # Add basket to object manager
        self.collision_system = collision_system
        # Event
        self.event_bus = event_bus
        self.event_bus.subscribe(EventType.FRUIT_HIT, self._on_fruit_hit)
        self.event_bus.subscribe(EventType.BOMB_HIT, self._on_bomb_hit)
        self.event_bus.subscribe(EventType.LEVEL_UP, self._on_level_up)
        print(id(self.event_bus))

        # state
        self.gameplay_state = gameplay_state
        self.difficulty_system = difficulty_system
        self.multiplier = 1.0

        # control
        self.is_paused = False

    # ----------------------------
    # UPDATE LOOP
    # ----------------------------
    def update(self, input_data, delta_time):
        """
        Main gameplay update loop
        """
        # 0. check pause
        if self.is_paused:
            return

        # 1. update time
        self._update_time(delta_time)

        # 2. update difficulty (level scaling)
        self._update_difficulty()

        # 3. spawn objects
        self._handle_spawning(delta_time)

        # 4. update all entities
        self._update_objects(delta_time, input_data)

        # 5. collision handling
        self._handle_collision()

        # 6. cleanup inactive objects
        self._cleanup_objects()

        # # 7. check game over
        # self._check_game_over()

    # ----------------------------
    # TIME & LEVEL
    # ----------------------------
    def _update_time(self, delta_time):
        """
        Increase elapsed time
        """
        self.gameplay_state.time_elapsed += delta_time

    def _update_difficulty(self):
        """
        Update level based on time
        """
        self.difficulty_system.update(self.gameplay_state.time_elapsed)
        self.gameplay_state.level = self.difficulty_system.current_level

    # ----------------------------
    # SPAWNING
    # ----------------------------
    def _handle_spawning(self, delta_time):
        """
        Spawn fruit / bomb based on difficulty
        """
        self.spawner.update(self.object_manager, delta_time, self.multiplier)

    # ----------------------------
    # OBJECT UPDATE
    # ----------------------------
    def _update_objects(self, delta_time, input_data=None):
        """
        Update all active entities
        """
        self.object_manager.update(delta_time, input_data, screen_height=SCREEN_HEIGHT)

    # ----------------------------
    # COLLISION
    # ----------------------------
    def _handle_collision(self):
        """
        Handle collision results and update state
        """
        self.collision_system.check(self.object_manager.get_objects())

    def _on_fruit_hit(self, data):
        fruit = data["fruit"]
        # print(f"Fruit hit: {fruit}")
        self.gameplay_state.add_score(fruit.score_value)
        # print(f"Score updated: {self.gameplay_state.score}")
        fruit.destroy()

    def _on_bomb_hit(self, data):
        bomb = data["bomb"]
        # print(f"Bomb hit: {bomb}")
        self.gameplay_state.lose_life(bomb.damage)
        # print(f"Lives remaining: {self.gameplay_state.life}")
        bomb.destroy()

    def _on_level_up(self, data):
        """
        Handle level up event
        """
        level = data["level"]
        self.gameplay_state.level = level
        self.multiplier = self.difficulty_system.get_spawn_speed_multiplier()

    # ----------------------------
    # CLEANUP
    # ----------------------------
    def _cleanup_objects(self):
        """
        Remove inactive or out-of-screen objects
        """
        self.object_manager.cleanup()

    # ----------------------------
    # GAME STATE
    # ----------------------------
    def _check_game_over(self):
        """
        Check if game over condition met
        """
        if self.gameplay_state.is_game_over():
            self._on_game_over()

    def _on_game_over(self):
        """
        Handle game over event
        """
        pass

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    # ----------------------------
    # DRAW
    # ----------------------------
    def draw(self, screen):
        """
        Draw gameplay world + HUD
        """

        # 1. draw game objects
        self.object_manager.draw(screen)

        # 2. draw HUD
        self._draw_hud(screen)
        # 3. draw basket (on top of everything)
        # self.basket.draw(screen)

    def _draw_hud(self, screen):
        """
        Draw score, life, level, time
        """
        self._draw_score(screen)
        self._draw_life(screen)
        self._draw_level(screen)
        self._draw_timer(screen)

    def _draw_score(self, screen):
        text = f"Score: {self.gameplay_state.score}"
        font = pygame.font.SysFont("Arial", 36)
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

    def _draw_life(self, screen):
        text = f"Lives: {self.gameplay_state.life}"
        font = pygame.font.SysFont("Arial", 36)
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 50))

    def _draw_level(self, screen):
        text = f"Level: {self.gameplay_state.level}"
        font = pygame.font.SysFont("Arial", 36)
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 90))

    def _draw_timer(self, screen):
        text = f"Time: {self.gameplay_state.time_elapsed:.1f}s"
        font = pygame.font.SysFont("Arial", 36)
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(
            text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 10)
        )
