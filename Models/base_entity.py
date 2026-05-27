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
        radius=None,
        image=None,
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
        self.radius = radius
        self.image = image
        self.color = color
        self.render_layer = RenderLayer.GAME_OBJECT

        # Life cycle
        self.active = True  # Indicates if the object is still falling

    # Update method to be called every frame
    def update(self, delta_time):
        if not self.active:
            return
        
        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time
        # Update the object's position based on its speed and the elapsed time
        pass

    # Life cycle method
    def destroy(self):
        # Mark the object as inactive when it is caught or hits the ground
        self.active = False
    
    # Collision detection method
    def get_rect(self):
        # Return the bounding rectangle for collision detection
        return (self.x, self.y, self.width, self.height)
    
    # Render method to be implemented by subclasses
    @abstractmethod
    def draw(self, screen):
        # Abstract method to draw the entity on the screen
        pass
