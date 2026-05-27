import pygame
from Models.basket_model import Basket
from Core.event_type import EventType


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
        print(id(self.event_bus))

        # state
        self.gameplay_state = gameplay_state
        self.difficulty_system = difficulty_system

        # control
        self.is_paused = False

    # ----------------------------
    # UPDATE LOOP
    # ----------------------------
    def update(self, input_data, delta_time):
        """
        Main gameplay update loop
        """
        # print(
        #     f"GameplaySystem.update called with input: {input_data}, delta_time: {delta_time}"
        # )
        # self.basket.update(input_data)
        # 0. check pause
        if self.is_paused:
            return

        # 1. update time
        self._update_time(delta_time)

        # # 2. update difficulty (level scaling)
        # self._update_difficulty()

        # 3. spawn objects
        self._handle_spawning(delta_time)

        # 4. update all entities
        self._update_objects(delta_time, input_data)

        # 5. collision handling
        self._handle_collision()

        # # 6. cleanup inactive objects
        # self._cleanup_objects()

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
        return self.gameplay_state.time_elapsed

    def _update_difficulty(self):
        """
        Update level based on time
        """
        self.difficulty_system.update(self.gameplay_state.time_elapsed)
        self.gameplay_state.level = self.difficulty_system.level

    # ----------------------------
    # SPAWNING
    # ----------------------------
    def _handle_spawning(self, delta_time):
        """
        Spawn fruit / bomb based on difficulty
        """
        self.spawner.update(self.object_manager, delta_time)

    # ----------------------------
    # OBJECT UPDATE
    # ----------------------------
    def _update_objects(self, delta_time, input_data=None):
        """
        Update all active entities
        """
        self.object_manager.update(delta_time, input_data)

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
        print(f"Fruit hit: {fruit}")
        self.gameplay_state.add_score(fruit.score_value)
        fruit.destroy()

    def _on_bomb_hit(self, data):
        bomb = data["bomb"]
        print(f"Bomb hit: {bomb}")
        self.gameplay_state.lose_life(bomb.damage)
        bomb.destroy()

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

        # # 2. draw HUD
        # self._draw_hud(screen)
        # 3. draw basket (on top of everything)
        self.basket.draw(screen)

    def _draw_hud(self, screen):
        """
        Draw score, life, level, time
        """
        self._draw_score(screen)
        self._draw_life(screen)
        self._draw_level(screen)
        self._draw_timer(screen)

    def _draw_score(self, screen):
        pass

    def _draw_life(self, screen):
        pass

    def _draw_level(self, screen):
        pass

    def _draw_timer(self, screen):
        pass
