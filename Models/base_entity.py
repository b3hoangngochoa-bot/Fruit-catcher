from abc import ABC, abstractmethod
from Systems.Render.render_layer import RenderLayer


class BaseEntity(ABC):
    def __init__(
        self,
        x=0,
        y=0,
        width=0,
        height=0,
        vx=0,
        vy=0,
        image=None,
        tag=None,
        color=(255, 255, 255),
    ):
        # Transform
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Movement
        self.velocity_x = vx
        self.velocity_y = vy

        # Render
        self.image = image
        self.color = color

        # Lifecycle
        self.active = True  # Indicates if the object is still falling

        # Identify
        self.tag = tag

        # Default render layer for game objects, can be overridden by subclasses
        self.render_layer = RenderLayer.GAME_OBJECT

    # Render method to be implemented by subclasses
    @abstractmethod
    def get_render_data(self):
        # Abstract method to return data for rendering the entity on the screen
        pass

    # Update method to be called every frame
    def update(self, delta_time):
        if not self.active:
            return

        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time

    # Lifecycle method
    def destroy(self):
        # Mark the object as inactive when it is caught or hits the ground
        self.active = False

    def is_out_of_screen(self, screen_height):
        # Check if the object has fallen below the bottom of the screen
        return self.y > screen_height
