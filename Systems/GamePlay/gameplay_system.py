from Models.basket_model import Basket
from Core.event_type import EventType
from Utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from Systems.UI.Elements.label import Label


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
    
        self.object_manager = object_manager
        self.object_manager.add_object(self.spawner.basket)  # Add basket to object manager
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

        # 7. check game over
        self._check_game_over()

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
            self._handle_game_over()

    def _handle_game_over(self):
        """
        Handle game over event
        """
        self.event_bus.emit(EventType.GAME_OVER, {})


    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False
    
    def restart(self):
        self.resume()  
        self._handle_reset()  # Reset game state and objects
    
    def reset(self):
        self.pause()
        self._handle_reset()

    def _handle_reset(self):
        self.object_manager.clear()  # Clear existing objects
        self.gameplay_state.reset()
        self.object_manager.add_object(self.spawner.basket)  # Reset object manager with only the basket
        self.multiplier = 1.0
    # ----------------------------
    # Render data
    # ----------------------------

    def get_render_data(self):
        data = []

        data.append(self._get_score_data())
        data.append(self._get_life_data())
        data.append(self._get_level_data())
        data.append(self._get_timer_data())
        for obj in self.object_manager.get_objects():
            rd = obj.get_render_data()
            if rd:
                data.append(rd)
        return data


    def _get_score_data(self):
        text = f"Score: {self.gameplay_state.score}"
        score = Label(x=10, y=10, size=36, text=text, color=(255, 255, 255))
        return score.get_render_data()

    def _get_life_data(self):
        text = f"Lives: {self.gameplay_state.life}"
        life = Label(x=10, y=50, size=36, text=text, color=(255, 255, 255))
        return life.get_render_data()

    def _get_level_data(self):
        text = f"Level: {self.gameplay_state.level}"
        level = Label(x=10, y=90, size=36, text=text, color=(255, 255, 255))
        return level.get_render_data()

    def _get_timer_data(self):
        text = f"Time: {self.gameplay_state.time_elapsed:.1f}s"
        timer = Label(x=SCREEN_WIDTH // 2 - 100, y=10, size=36, text=text, color=(255, 255, 255))
        return timer.get_render_data()

